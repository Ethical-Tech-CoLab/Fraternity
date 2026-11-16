"""Synthetic world, step 2: records and errors (week 6; BENCHMARK_PROTOCOL.md §2.3).

Each invented person is observed through a few simulated records (registration form, camp
distribution list, school list, tracing request, passport MRZ). A record's name is either the
person's own spelling (written or shown by the person) or written BY EAR by a clerk or
interpreter in another language. By-ear writing applies the language packs' sourced spelling
conventions for that writer's language and the packs' listener confusions; every change is
logged with the pack entry it came from (`errors`), so results can be sliced by error type.

Other errors (GeCo-style, rates in data/benchmark/params-*.json, scaled by one calibration
factor so that about 22% of name values differ between records of one person [B14]): name
order, DRC postnom dropped or swapped, married name added, Christian names in another
language (from the crosspack), typos, OCR, free variation, age heaping and estimation, old or
new province names (from the places data), and adopted names in exile (NAME_CHANGE.md: step 1
the given name, step 2 also the surname). The adopted given name is another given name from
the corridor pool: which names people actually adopt (often Muslim names) waits for the legal
check (DECISIONS_OPEN.md), so only the mechanism is generated.

The gold person id stays on each record here; step 3 moves it to separate gold files.

Run: python -m namebridge.benchmark.records [--world build/benchmark] [--out build/benchmark]
"""

import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from namebridge.benchmark.world import PARAMS, ROOT, World
from namebridge.normalize import fold

PACKS = {"RW": "rw-kiny-2026.1", "BI": "bi-kirundi-2026.1", "CD": "cd-swc-ln-2026.1"}
NAME_LANG = {"RW": "rw", "BI": "rn", "CD": "sw"}
NATIVE_SLOTS = {"kinyarwanda", "kirundi", "nom", "postnom"}
CONFIDENCE_WEIGHT = {"high": 1.0, "medium": 0.5, "disputed": 0.5, "low": 0.25, "hypothesis": 0.25}
VOWELS = "aeiou"

# Every by-ear transform names the pack entry it implements: (pack section, key, writer).
# test_benchmark_records checks that each entry exists in the pack, so no rule is unsourced.
CONVENTIONS = [
    # (packs, section, sound, writer, pattern, replacements)
    (("RW", "BI"), "spelling_conventions", "/ʃ/", "fr", r"sh", ["ch"]),
    (("CD",), "spelling_conventions", "/ʃ/", "fr", r"sh", ["ch"]),
    (("RW", "BI"), "spelling_conventions", "/tʃ/", "fr", r"c(?![hy])", ["tch"]),
    (("RW", "BI"), "spelling_conventions", "/tʃ/", "en", r"c(?![hy])", ["ch"]),
    (("RW", "BI"), "spelling_conventions", "/tʃ/", "sw", r"c(?![hy])", ["ch"]),
    (("RW", "BI"), "spelling_conventions", "/tʃ/", "ny", r"c(?![hy])", ["ch", "tch"]),
    (("CD",), "spelling_conventions", "/tʃ/", "fr", r"ch", ["tsh", "tch"]),
    (("RW", "BI"), "spelling_conventions", "/ʒ/", "fr", r"j(?=[ei])", ["g"]),
    (("RW", "BI"), "spelling_conventions", "/ɲ/", "fr", r"ny", ["gn"]),
    (("RW", "BI", "CD"), "spelling_conventions", "/w/", "fr", r"(?<=[^aeiou])w|^w", ["ou"]),
    (("CD",), "spelling_conventions", "/s/", "fr", r"(?<=[aeiou])s(?=[aeiou])", ["ss"]),
]
# Chichewa writers: r after i or e, l after a, o or u, l word-initially (rule given in prose)
CHICHEWA_RL = ("spelling_conventions", "/ɾ/", "ny")
CONFUSIONS = [
    # (packs, sounds key as in the pack, listener scope, pattern, replacements)
    (("RW", "BI"), ["/r/", "/l/"], "any", r"[rl]", None),  # None = swap r <-> l
    (("CD",), ["/r/", "/l/"], "any", r"[rl]", None),
    (("RW",), ["/ɾw/", "/ɾɡw/"], "non-native", r"rw", ["rgw"]),
    (("BI",), ["/rw/", "/rgw/"], "non-native", r"rw", ["rgw"]),
    (("RW", "BI"), ["/sw/", "/skw/"], "non-native", r"sw", ["skw"]),
    (("RW", "BI"), ["/tw/", "/tkw/"], "non-native", r"tw", ["tkw"]),
    (("RW",), ["/bw/", "/bɡ/"], "non-native", r"bw", ["bg"]),
    (("BI",), ["/vy/", "/vz/"], "non-native", r"vy", ["vz"]),
    (("RW",), ["/ᵐb/", "/b/"], "non-native", r"mb", ["b"]),
    (("BI",), ["/ᵐb/", "/b/"], "non-native", r"mb", ["b"]),
    (("CD",), ["/ᵐp/", "/p/"], "any", r"mp", ["p"]),
    (("CD",), ["/m/", "/n/"], "any", r"[mn]$", None),
    (("CD",), ["/o/", "/u/"], "any", r"[ou]", None),
]
SWAP = {"r": "l", "l": "r", "m": "n", "n": "m", "o": "u", "u": "o"}
# French-form (Christian) names written by others: pack rules applied to foreign names
FOREIGN_RULES = {
    "silent_h": ("spelling_conventions", "(silent h)", "fr"),
    "double_letter": ("spelling_conventions", "(double letter)", "fr"),
    "final_vowel": ("phonetic_rules", "foreign-name-final-vowel", None),
    "i_to_y": ("listener_confusions", "/i/", None),
}
OCR = [("rn", "m"), ("m", "rn"), ("cl", "d"), ("li", "h"), ("vv", "w"), ("i", "l")]


def load_packs():
    return {o: json.loads((ROOT / "data" / "packs" / f"{p}.json").read_text(encoding="utf-8")) for o, p in PACKS.items()}


def pack_entry(pack, section, key, writer=None):
    """The pack entry a transform implements, or None (the tests require it to exist)."""
    for e in pack.get(section, []):
        if section == "spelling_conventions" and e["sound"] == key and e["writer_language"] == writer:
            return e
        if section == "listener_confusions" and (e["sounds"] == key or (isinstance(key, str) and e["sounds"][0] == key)):
            return e
        if section == "phonetic_rules" and e.get("id") == key:
            return e
    return None


def christian_variants():
    """French form (folded) -> {language: [forms]} from the crosspack (attested translations)."""
    data = json.loads((ROOT / "data" / "crosspack" / "christian-names-2026.1.json").read_text(encoding="utf-8"))
    out = {}
    for concept in data["concepts"]:
        by_lang = defaultdict(list)
        for f in concept["forms"]:
            by_lang[f["lang"]].append(f["text"])
        for fr in by_lang.get("fr", []):
            out[fold(fr)] = dict(by_lang)
    return out


def place_alternatives():
    """Province name (folded) -> names of the same area in another period (renamed, merged, split)."""
    data = json.loads((ROOT / "data" / "places" / "places-2026.1.json").read_text(encoding="utf-8"))
    units = {u["key"]: u for u in data["units"]}
    alt = defaultdict(set)
    for ch in data["changes"]:
        a, b = units.get(ch["from"]), units.get(ch["to"])
        if a and b and a["level"] == b["level"] == "province" and ch["relation"] in ("renamed_to", "merged_into", "split_into"):
            alt[fold(a["name"])].add(b["name"])
            alt[fold(b["name"])].add(a["name"])
    return {k: sorted(v) for k, v in alt.items()}


class Recorder:
    def __init__(self, world, params, seed=None):
        self.world, self.p = world, params["params"]
        self.year = params["reference_year"]
        self.rng = random.Random((params["seed"] if seed is None else seed) + 1)
        self.packs = load_packs()
        self.christian = christian_variants()
        self.places = place_alternatives()
        self.scale = self.p["rec_error_scale"]["value"]
        # a foreign-name rule applies only where that origin's pack holds its entry
        self.foreign = {o: {k for k, (sec, key, w) in FOREIGN_RULES.items() if pack_entry(self.packs[o], sec, key, w)}
                        for o in PACKS}
        self.people = {p["id"]: p for p in world.people}
        self.records = []
        self._prepare_people()

    # --- per-person traits ---------------------------------------------------------------------
    def _prepare_people(self):
        fv = self.p["rec_free_variation_person"]["value"]
        s1, s2 = self.p["rec_name_change_s1"]["value"], self.p["rec_name_change_s2"]["value"]
        for p in self.world.people:
            own = [e["text"] for e in p["name"]]
            if self.rng.random() < fv * self.scale:
                i = self.rng.randrange(len(own))
                own[i] = self._free_variation(own[i])
                p["own_spelling_varies"] = True
            p["own_spelling"] = own
            change = 0
            if not p["minor"] and self.rng.random() < s1:
                change = 2 if self.rng.random() < s2 / s1 else 1
            p["name_change"] = change
            if change:
                adopted = list(own)
                gi = next((i for i, e in enumerate(p["name"]) if e["slot"] == "christian"), None)
                if gi is not None:
                    pool = self.world.pools["ALL", "christian", p["sex"]]
                    for _ in range(20):
                        new = pool.draw(self.rng)
                        if new not in own:
                            break
                    adopted[gi] = new
                if change == 2:
                    other = self.rng.choice([o for o in ("RW", "BI", "CD") if o != p["origin"]])
                    slot = {"RW": "kinyarwanda", "BI": "kirundi", "CD": "nom"}[other]
                    adopted[0] = self.world.inventors[other, slot].invent(self.rng)
                p["adopted_name"] = adopted

    def _free_variation(self, text):
        i = self.rng.randrange(len(text))
        op = self.rng.choice(("insert", "double", "substitute", "delete"))
        if op == "double" or (op == "delete" and len(text) < 4):
            return text[:i] + text[i] + text[i:]
        if op == "insert":
            return text[:i] + self.rng.choice("hy" + VOWELS) + text[i:]
        if op == "substitute":
            c = text[i]
            return text[:i] + ({"i": "y", "y": "i", "s": "z", "z": "s", "e": "a"}.get(c, c)) + text[i + 1:]
        return text[:i] + text[i + 1:]

    # --- by-ear writing --------------------------------------------------------------------------
    def _apply(self, text, pattern, replacements, prob, log, label):
        def sub(m):
            if self.rng.random() >= prob:
                return m.group(0)
            log.append(label)
            if replacements is None:
                return "".join(SWAP.get(c, c) for c in m.group(0))
            return self.rng.choice(replacements)
        return re.sub(pattern, sub, text)

    def by_ear_native(self, text, origin, writer, log):
        """A native (Bantu) name element heard and written by a writer of language `writer`."""
        native = writer == NAME_LANG[origin] or (writer == "rw" and origin in ("RW", "BI"))
        p_conv = self.p["rec_convention_rate"]["value"]
        for packs, section, sound, w, pattern, repl in CONVENTIONS:
            if origin in packs and w == writer:
                text = self._apply(text, pattern, repl, p_conv, log, f"{PACKS[origin]}:{section}:{sound}:{w}")
        if writer == "ny":
            text = self._chichewa_rl(text, log, origin)
        rate = self.p["rec_confusion_rate"]["value"] * self.scale
        for packs, sounds, scope, pattern, repl in CONFUSIONS:
            if origin not in packs or (scope == "non-native" and native):
                continue
            entry = pack_entry(self.packs[origin], "listener_confusions", sounds)
            prob = rate * CONFIDENCE_WEIGHT.get(entry.get("confidence"), 0.25)
            text = self._apply(text, pattern, repl, prob, log, f"{PACKS[origin]}:listener_confusions:{'~'.join(sounds)}")
        return text

    def _chichewa_rl(self, text, log, origin):
        out = []
        for i, c in enumerate(text):
            if c in "rl" and self.rng.random() < self.p["rec_convention_rate"]["value"]:
                prev = text[i - 1] if i else ""
                new = "l" if not prev or prev in "aou" else ("r" if prev in "ie" else c)
                if new != c:
                    log.append(f"{PACKS[origin]}:spelling_conventions:/ɾ/:ny")
                c = new
            out.append(c)
        return "".join(out)

    def by_ear_christian(self, text, writer, origin, log):
        """A French-form given name written by someone else (pack rules for foreign names)."""
        rate = self.p["rec_foreign_name_rate"]["value"] * self.scale
        pk = PACKS[origin]
        allowed = self.foreign[origin]
        if "silent_h" in allowed and writer == "fr" and self.rng.random() < rate:
            text = (text[:-1] if text.endswith("h") else text + "h") if text[-1] in VOWELS + "h" else text
            log.append(f"{pk}:spelling_conventions:(silent h):fr")
        if "double_letter" in allowed and writer == "fr" and self.rng.random() < rate * 0.5:
            i = self.rng.randrange(1, len(text)) if len(text) > 1 else 0
            text = text[:i] + text[i] + text[i:]
            log.append(f"{pk}:spelling_conventions:(double letter):fr")
        if "final_vowel" in allowed and writer in ("sw", "ny", "rw") and text[-1] not in VOWELS and self.rng.random() < rate * 2:
            text = text + ("i" if text[-1] in "lnmrs" else "u")
            log.append(f"{pk}:phonetic_rules:foreign-name-final-vowel")
        if "i_to_y" in allowed and "i" in text[1:] and self.rng.random() < rate * CONFIDENCE_WEIGHT["hypothesis"]:
            i = text.index("i", 1)
            text = text[:i] + "y" + text[i + 1:]
            log.append(f"{pk}:listener_confusions:/i/~y")
        return text

    # --- one record --------------------------------------------------------------------------------
    def _choose(self, dist):
        keys = list(dist)
        return self.rng.choices(keys, [dist[k] for k in keys])[0]

    def _literate(self, person, record_year):
        age = record_year - person["birth_year"]
        if age < 15:
            return False
        lit = self.p["rec_literacy"]["value"][person["origin"]][person["sex"]]
        if age < 25:
            lit = max(lit, self.p["rec_literacy"]["value"][person["origin"]].get("youth", lit))
        if age >= 50:
            lit *= self.p["rec_older_literacy_factor"]["value"]
        return self.rng.random() < lit

    def record(self, person, source):
        P, rng = self.p, self.rng
        record_year = rng.randint(max(person["birth_year"] + (6 if source == "school_list" else 0), P["rec_years"]["value"][0]),
                                  P["rec_years"]["value"][1])
        writer = self._choose(P["rec_writer_language"]["value"][source])
        writer_id = f"{source[:3]}-{writer}-{rng.randrange(P['rec_writers_per_source']['value']):02d}"
        log = []
        literate = self._literate(person, record_year)
        by_ear = source != "passport_mrz" and (not literate or rng.random() < P["rec_by_ear_if_literate"]["value"])
        in_exile = source in ("registration", "distribution_list", "school_list")
        texts = list(person["own_spelling"])
        if person["name_change"] and in_exile and rng.random() < P["rec_adopted_name_used"]["value"]:
            texts = list(person["adopted_name"])
            log.append(f"name_change:step{person['name_change']}")
        if by_ear:
            texts = [self.by_ear_native(t, person["origin"], writer, log) if e["slot"] in NATIVE_SLOTS
                     else self.by_ear_christian(t, writer, person["origin"], log)
                     for t, e in zip(texts, person["name"])]
        slots = [e["slot"] for e in person["name"]]
        # Christian name in the writer's language (attested forms only)
        for i, s in enumerate(slots):
            forms = self.christian.get(fold(texts[i]), {}).get(writer)
            if s == "christian" and forms and writer != "fr" and rng.random() < P["rec_christian_language_rate"]["value"] * self.scale:
                texts[i] = rng.choice(forms).lower()
                log.append(f"crosspack:christian-names:{writer}")
        if person["origin"] == "CD" and "postnom" in slots:
            j = slots.index("postnom")
            if rng.random() < P["rec_postnom_dropped"]["value"] * self.scale:
                del texts[j], slots[j]
                log.append("cd:postnom_dropped")
            elif rng.random() < P["rec_nom_postnom_swapped"]["value"] * self.scale:
                texts[0], texts[j] = texts[j], texts[0]
                log.append("cd:nom_postnom_swapped")
        if person["origin"] == "CD" and person["role"] == "mother" and person.get("husband_nom") \
                and rng.random() < P["rec_married_name_added"]["value"]:
            texts.insert(1, person["husband_nom"])
            slots.insert(1, "married")
            log.append("cd:married_name_added")
        if rng.random() < P["rec_typo_rate"]["value"] * self.scale:
            i = rng.randrange(len(texts))
            texts[i] = self._free_variation(texts[i])
            log.append("typo")
        if source == "distribution_list" and rng.random() < P["rec_ocr_rate"]["value"] * self.scale:
            i = rng.randrange(len(texts))
            for a, b in rng.sample(OCR, len(OCR)):
                if a in texts[i]:
                    texts[i] = texts[i].replace(a, b, 1)
                    log.append("ocr")
                    break
        given_first = rng.random() < P["rec_given_first"]["value"][source]
        name = self._format(texts, slots, person["origin"], source, given_first)
        fields = {"surname": " ".join(t.upper() for t, s in zip(texts, slots) if s != "christian"),
                  "given_names": " ".join(t.capitalize() for t, s in zip(texts, slots) if s == "christian")}
        if given_first:
            log.append("order:given_first")
        return {
            "record_id": f"r{len(self.records) + 1:07d}",
            "gold_person": person["id"],
            "source": source, "record_year": record_year,
            "writer_language": writer, "writer_id": writer_id,
            "written_by": "ear" if by_ear else "self_or_document",
            "name": name,
            # forms with separate fields keep them; lists and requests hold one free-text name
            "name_fields": fields if source in ("registration", "school_list", "passport_mrz") else None,
            "_fields": fields,
            "sex": None if rng.random() < P["rec_missing_sex"]["value"] else person["sex"],
            "age_or_birth": self._age(person, record_year, log),
            "province_of_origin": self._place(person, log),
            "claimed_origin": self._origin(person, log),
            "errors": log,
        }

    def _format(self, texts, slots, origin, source, given_first):
        if source == "passport_mrz":
            sur = [t for t, s in zip(texts, slots) if s != "christian"]
            given = [t for t, s in zip(texts, slots) if s == "christian"]
            mrz = "<".join(sur).upper() + "<<" + "<".join(given).upper()
            return re.sub(r"[^A-Z<]", "", fold(mrz).upper())[:39]
        sur = [t.upper() for t, s in zip(texts, slots) if s != "christian"]
        given = [t.capitalize() for t, s in zip(texts, slots) if s == "christian"]
        return " ".join(given + sur if given_first else sur + given)

    def _age(self, person, record_year, log):
        P, rng = self.p, self.rng
        age = record_year - person["birth_year"]
        if rng.random() < P["rec_missing_age"]["value"]:
            log.append("age:missing")
            return None
        if person["minor"] and age < 18 and rng.random() < P["rec_child_age_estimated"]["value"]:
            age = max(0, age + rng.choice((-2, -1, 1, 2)))
            log.append("age:estimated")
            return {"age_about": age, "at_year": record_year}
        if age >= 18 and rng.random() < P["rec_age_heaping"]["value"]:
            heaped = 5 * round(age / 5)
            if heaped != age:
                log.append("age:heaped")
            return {"age_about": heaped, "at_year": record_year}
        return {"birth_year": person["birth_year"]}

    def _place(self, person, log):
        fam = self.families[person["family"]]
        prov = fam["province_of_origin"]
        if self.rng.random() < self.p["rec_missing_place"]["value"]:
            return None
        alts = self.places.get(fold(prov))
        if alts and self.rng.random() < self.p["rec_place_other_period"]["value"]:
            log.append("place:other_period")
            return self.rng.choice(alts)
        return prov

    def _origin(self, person, log):
        if self.rng.random() < self.p["rec_false_nationality"]["value"]:
            log.append("false_nationality")
            return self.rng.choice([o for o in ("RW", "BI", "CD") if o != person["origin"]])
        return person["origin"]

    # --- all records ------------------------------------------------------------------------------
    def generate(self):
        self.families = {f["id"]: f for f in self.world.families}
        for fam in self.world.families:
            if fam["origin"] == "CD" and fam["father"] and fam["mother"]:
                self.people[fam["mother"]]["husband_nom"] = self.people[fam["father"]]["name"][0]["text"]
        shares = self.p["rec_source_shares"]["value"]
        for person in self.world.people:
            n = int(self._choose(self.p["rec_records_per_person"]["value"]))
            for _ in range(n):
                options = {s: w for s, w in shares.items()
                           if not (s == "school_list" and not 6 <= self.year - person["birth_year"] <= 24)
                           and not (s == "passport_mrz" and person["minor"])}
                rec = self.record(person, self._choose(options))
                self.records.append(rec)
        return self

    def summary(self):
        by_person = defaultdict(list)
        for r in self.records:
            by_person[r["gold_person"]].append(r)
        # [B14]: share of name VALUES (surname, given names) that differ between linked records
        differ = total = 0
        for recs in by_person.values():
            recs = [r for r in recs if r["source"] != "passport_mrz"]
            for i in range(len(recs)):
                for j in range(i + 1, len(recs)):
                    for f in ("surname", "given_names"):
                        a, b = fold(recs[i]["_fields"][f]), fold(recs[j]["_fields"][f])
                        if a or b:
                            total += 1
                            differ += a != b
        kinds = Counter(e.split(":")[0] if not e.startswith(tuple(PACKS.values())) else "pack:" + e.split(":")[1]
                        for r in self.records for e in r["errors"])
        return {
            "records": len(self.records),
            "records_per_person": round(len(self.records) / len(self.world.people), 2),
            "name_values_differ_between_linked_records": round(differ / total, 3),
            "written_by_ear": round(sum(r["written_by"] == "ear" for r in self.records) / len(self.records), 3),
            "sources": dict(Counter(r["source"] for r in self.records)),
            "error_kinds": dict(kinds.most_common()),
            "people_with_name_change": dict(Counter(p["name_change"] for p in self.world.people)),
        }


def write(recorder, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "records.jsonl", "w", encoding="utf-8") as f:
        for r in recorder.records:
            f.write(json.dumps({k: v for k, v in r.items() if not k.startswith("_")}, ensure_ascii=False) + "\n")
    summary = recorder.summary()
    (out / "records_manifest.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def main(argv):
    opt = lambda flag, default=None: argv[argv.index(flag) + 1] if flag in argv else default
    params = json.loads(PARAMS.read_text(encoding="utf-8"))
    people = opt("--people")
    world = World(params, people=int(people) if people else None).generate()
    rec = Recorder(world, params).generate()
    print(json.dumps(write(rec, opt("--out", ROOT / "build" / "benchmark")), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main(sys.argv[1:])
