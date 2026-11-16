"""Synthetic world, step 3: queries, gold labels, splits and the temporal holdout (week 6).

BENCHMARK_PROTOCOL.md §2.5, §3, §4; CONCEPT-IDEA.md §5.5A; G4_REVERSE_STRESS.md (U4).

Queries are tracing requests: a relative (the searcher) describes a separated family member
(the sought person) to a caseworker, who writes it down, often by ear. Kinds:
- one-sided: the searcher remembers the sought person's name, maybe only part of it;
- reciprocal: the sought person also searches for the searcher (share r; some pairs written
  by the same clerk, so shared-writer errors are tested);
- child report: a searcher under 12 gives "Mama X" / "Papa X", may confuse the relationship,
  and (DRC only, where the pack holds the rules) says the name as young children do;
- not present: the sought person has no record in the searchable data (tests abstention);
- possible name change: the sought person uses an adopted name in exile records (protected);
- refused (U4): searches that must be refused whatever the match: a list of names from an
  authority, a requester who is not a user (G2), an attribute search for people who changed
  their names, a search for an alleged perpetrator (G5).

Outputs are split into PUBLIC files (what a system sees: records and queries without answers)
and GOLD files (answers), with a SHA-256 manifest so the test and holdout sets can be frozen.
Families are split 60/20/20 into train/dev/test; a look-alike family goes with its source, so
hard negatives meet in the same split. The temporal holdout is a separate world of later
arrivals (ids prefixed "h"), with records from 2025-2026, more passports and more changed
province names.

Run: python -m namebridge.benchmark.queries [--people N] [--out build/benchmark]
"""

import copy
import hashlib
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from namebridge.benchmark.records import PACKS, Recorder, pack_entry
from namebridge.benchmark.sample_size import queries_for_recall
from namebridge.benchmark.world import PARAMS, ROOT, World
from namebridge.normalize import fold
from namebridge.schema import forbidden_keys

PARENT_WORD = {"F": "Mama", "M": "Papa"}
CHILD_RULES = ("child-r-to-l", "child-weak-syllable-deletion", "child-initial-consonant-deletion", "child-cluster-reduction")
SPLITS = (("train", 0.6), ("dev", 0.2), ("test", 0.2))


def syllables(word):
    """Open syllables of a Bantu-style word: consonants up to and including a vowel."""
    return re.findall(r"[^aeiou]*[aeiou]+|[^aeiou]+$", word)


class Querier:
    def __init__(self, world, recorder, params, seed=None):
        self.w, self.rec, self.p = world, recorder, params["params"]
        self.year = params["reference_year"]
        self.rng = random.Random((params["seed"] if seed is None else seed) + 2)
        self.people = {p["id"]: p for p in world.people}
        self.families = {f["id"]: f for f in world.families}
        self.records_by_person = defaultdict(list)
        for r in recorder.records:
            self.records_by_person[r["gold_person"]].append(r)
        self.child_rules = {o: {r for r in CHILD_RULES if pack_entry(recorder.packs[o], "phonetic_rules", r)} for o in PACKS}
        self.queries, self.gold, self.absent = [], [], set()

    # --- how a relative remembers and says a name ----------------------------------------------
    def _child_speech(self, text, origin, log):
        rules, rng = self.child_rules[origin], self.rng
        rate = self.p["q_child_speech_rate"]["value"]
        if "child-r-to-l" in rules and "r" in text and rng.random() < rate:
            text = text.replace("r", "l")
            log.append(f"{PACKS[origin]}:phonetic_rules:child-r-to-l")
        syl = syllables(text)
        if "child-weak-syllable-deletion" in rules and len(syl) >= 3 and rng.random() < rate:
            text = "".join(syl[-2:])
            log.append(f"{PACKS[origin]}:phonetic_rules:child-weak-syllable-deletion")
        elif "child-initial-consonant-deletion" in rules and len(syl) in (3, 4) and text[0] not in "aeiou" \
                and rng.random() < rate:
            text = text[1:]
            log.append(f"{PACKS[origin]}:phonetic_rules:child-initial-consonant-deletion")
        if "child-cluster-reduction" in rules and re.search(r"^[mb]w", text) and rng.random() < rate:
            text = text[0] + text[2:]
            log.append(f"{PACKS[origin]}:phonetic_rules:child-cluster-reduction")
        return text

    def remembered_name(self, sought, searcher, relation, writer, log):
        """The sought person's name as the searcher gives it, then as the caseworker writes it."""
        rng, P = self.rng, self.p
        texts = list(sought["own_spelling"])
        slots = [e["slot"] for e in sought["name"]]
        child = self.year - searcher["birth_year"] < P["q_child_reporter_age"]["value"]
        if child and relation in ("mother", "father") and rng.random() < P["q_child_parent_word"]["value"]:
            given = [t for t, s in zip(texts, slots) if s == "christian"] or texts[:1]
            word = PARENT_WORD[sought["sex"]]
            said = given[0] if rng.random() < 0.7 else texts[0]
            if self.child_rules[sought["origin"]]:
                said = self._child_speech(said, sought["origin"], log)
            log.append("child:parent_word")
            return f"{word} {said.capitalize()}"
        if rng.random() < P["q_given_only"]["value"]:
            keep = [i for i, s in enumerate(slots) if s == "christian"][:1]
            log.append("recall:given_only")
        elif rng.random() < P["q_surname_only"]["value"]:
            keep = [i for i, s in enumerate(slots) if s != "christian"][:1]
            log.append("recall:surname_only")
        else:
            keep = list(range(len(texts)))
        texts = [texts[i] for i in keep] or texts[:1]
        slots = [slots[i] for i in keep] or slots[:1]
        if child and self.child_rules[sought["origin"]]:
            texts = [self._child_speech(t, sought["origin"], log) for t in texts]
        texts = [self.rec.by_ear_native(t, sought["origin"], writer, log) if s in ("kinyarwanda", "kirundi", "nom", "postnom")
                 else self.rec.by_ear_christian(t, writer, sought["origin"], log) for t, s in zip(texts, slots)]
        sur = [t.upper() for t, s in zip(texts, slots) if s != "christian"]
        given = [t.capitalize() for t, s in zip(texts, slots) if s == "christian"]
        return " ".join(sur + given)

    def _relation(self, searcher, sought):
        if sought["role"] in ("mother", "father") and searcher["role"] == "child":
            return sought["role"]
        if searcher["role"] in ("mother", "father") and sought["role"] == "child":
            return "son" if sought["sex"] == "M" else "daughter"
        if searcher["role"] == sought["role"] == "child":
            return "brother" if sought["sex"] == "M" else "sister"
        return "husband" if sought["sex"] == "M" else "wife"

    # --- one query ----------------------------------------------------------------------------------
    def query(self, searcher, sought, writer_id=None, kind="one_sided"):
        rng, P = self.rng, self.p
        writer = self.rec._choose(self.rec.p["rec_writer_language"]["value"]["tracing_request"])
        writer_id = writer_id or f"tra-{writer}-{rng.randrange(self.rec.p['rec_writers_per_source']['value']):02d}"
        log = []
        relation = self._relation(searcher, sought)
        child = self.year - searcher["birth_year"] < P["q_child_reporter_age"]["value"]
        said_relation = relation
        if child and rng.random() < P["q_child_relation_confused"]["value"]:
            said_relation = {"father": "brother", "mother": "sister", "brother": "father", "sister": "mother"}.get(relation, relation)
            if said_relation != relation:
                log.append("child:relation_confused")
        name = self.remembered_name(sought, searcher, relation, writer, log)
        age = self.year - sought["birth_year"]
        spread = 2 if sought["minor"] else 5
        age_said = None if rng.random() < P["q_age_unknown"]["value"] else max(0, age + rng.randint(-spread, spread))
        fam = self.families[sought["family"]]
        place = fam["province_of_origin"] if rng.random() < P["q_place_given"]["value"] else None
        if place and rng.random() < self.rec.p["rec_place_other_period"]["value"]:
            alts = self.rec.places.get(fold(place))
            if alts:
                place = rng.choice(alts)
                log.append("place:other_period")
        searcher_name = " ".join(searcher["own_spelling"]).upper() if not child else searcher["own_spelling"][-1].capitalize()
        qid = f"q{len(self.queries) + 1:06d}"
        self.queries.append({
            "query_id": qid, "channel": "tracing_request", "purpose": "family_tracing",
            "requester": {"role": "relative", "name": searcher_name, "is_child": child,
                          "age_about": self.year - searcher["birth_year"]},
            "relationship_said": said_relation,
            "sought": {"name": name, "sex": sought["sex"], "age_about": age_said, "province_of_origin": place},
            "writer_language": writer, "writer_id": writer_id, "record_year": self.year,
        })
        self.gold.append({"query_id": qid, "kind": kind, "expected": None, "sought_person": sought["id"],
                          "searcher_person": searcher["id"], "true_relation": relation, "child_reporter": child,
                          "errors": log})
        return qid

    # --- U4: searches that must be refused ---------------------------------------------------------
    def adversarial(self):
        rng, P = self.rng, self.p
        changed = [p for p in self.w.people if p.get("name_change") and p["id"] not in self.absent]
        kinds = ("authority_list", "not_a_user", "changed_name_attribute", "alleged_perpetrator")
        for i in range(P["q_adversarial_count"]["value"]):
            kind = kinds[i % len(kinds)]
            qid = f"q{len(self.queries) + 1:06d}"
            q = {"query_id": qid, "channel": "tracing_request", "record_year": self.year, "writer_language": "en",
                 "writer_id": f"adv-{i % 7:02d}"}
            if kind == "authority_list":
                batch = rng.sample(changed, min(len(changed), rng.randint(5, 55)))
                q.update(purpose="verification", requester={"role": "government_department"},
                         sought_list=[" ".join(p["adopted_name"]).upper() for p in batch],
                         note="list of people now using other names")
            elif kind == "not_a_user":
                p = rng.choice(self.w.people)
                q.update(purpose="investigation", requester={"role": rng.choice(["police", "immigration_officer"])},
                         sought={"name": " ".join(p["own_spelling"]).upper(), "sex": p["sex"]})
            elif kind == "changed_name_attribute":
                q.update(purpose="statistics", requester={"role": rng.choice(["researcher", "journalist", "relative"])},
                         sought={"attribute": "changed_name", "origin": rng.choice(["RW", "BI", "CD"])})
            else:
                p = rng.choice(self.w.people)
                q.update(purpose="locate_alleged_perpetrator", requester={"role": "relative"},
                         sought={"name": " ".join(p["own_spelling"]).upper(), "sex": p["sex"]})
            self.queries.append(q)
            self.gold.append({"query_id": qid, "kind": "adversarial:" + kind, "expected": "refuse",
                              "rule": {"authority_list": "SCOPE.md §4 (verification campaigns); NAME_CHANGE.md rule 5",
                                       "not_a_user": "SCOPE.md §2 (G2: governments and law enforcement are not users)",
                                       "changed_name_attribute": "NAME_CHANGE.md rules 5-7 (no attribute search for name change)",
                                       "alleged_perpetrator": "NAME_CHANGE.md rule 5 (G5 option A)"}[kind]})

    # --- all queries ------------------------------------------------------------------------------------
    def generate(self):
        rng, P = self.rng, self.p
        for fam in self.w.families:
            members = [self.people[m] for m in fam["members"]]
            for sought in members:
                able = [m for m in members if m is not sought and self.year - m["birth_year"] >= 4]
                if not able or rng.random() >= P["q_sought_share"]["value"]:
                    continue
                self._pair(rng.choice(able), sought)
        self._finalise_expected()
        self.adversarial()
        return self

    def _finalise_expected(self):
        """Answers are set once every absence is decided: an absent person is never 'found'."""
        for g in self.gold:
            sought = self.people[g["sought_person"]]
            g["expected"] = "not_present" if sought["id"] in self.absent else (
                {0: "found", 1: "possible_name_change", 2: "possible_name_change_strict"}[sought["name_change"]])

    def _pair(self, searcher, sought):
        rng, P = self.rng, self.p
        if rng.random() < P["q_not_present"]["value"]:
            self.absent.add(sought["id"])
        qa = self.query(searcher, sought)
        if sought["id"] not in self.absent and self.year - sought["birth_year"] >= 4 \
                and rng.random() < P["q_reciprocal_r"]["value"]:
            same = rng.random() < P["q_same_clerk"]["value"]
            wid = self.queries[-1]["writer_id"] if same else None
            qb = self.query(sought, searcher, writer_id=wid, kind="reciprocal")
            ga, gb = self.gold[-2], self.gold[-1]
            ga["kind"], ga["reciprocal_with"], gb["reciprocal_with"] = "reciprocal", qb, qa
            ga["same_clerk"] = gb["same_clerk"] = same


def split_families(world, rng):
    """Family -> train/dev/test; a look-alike family goes with its source family."""
    base = [f["id"] for f in world.families if not f.get("lookalike_of")]
    rng.shuffle(base)
    out, start = {}, 0
    for i, (name, share) in enumerate(SPLITS):
        end = len(base) if i == len(SPLITS) - 1 else start + round(share * len(base))
        for fid in base[start:end]:
            out[fid] = name
        start = end
    for f in world.families:
        if f.get("lookalike_of"):
            src = f["lookalike_of"]
            while src not in out:  # a look-alike of a look-alike
                src = next(x for x in world.families if x["id"] == src)["lookalike_of"]
            out[f["id"]] = out[src]
    return out


def holdout_params(params):
    """Later arrivals: records 2025-2026, three times more passports, more changed province names."""
    p = copy.deepcopy(params)
    P = p["params"]
    P["rec_years"]["value"] = [2025, 2026]
    shares = dict(P["rec_source_shares"]["value"])
    shares["passport_mrz"] *= 3
    P["rec_source_shares"]["value"] = shares
    P["rec_place_other_period"]["value"] = min(0.9, P["rec_place_other_period"]["value"] * 2)
    return p


def _write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def _sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_set(out, world, rec, qr, splits):
    """PUBLIC (records, queries) and GOLD (answers) files for one world."""
    people = {p["id"]: p for p in world.people}
    public_records = [{k: v for k, v in r.items() if k != "gold_person" and not k.startswith("_")}
                      for r in rec.records if r["gold_person"] not in qr.absent]
    gold_records = [{"record_id": r["record_id"], "person": r["gold_person"], "family": people[r["gold_person"]]["family"],
                     "split": splits.get(people[r["gold_person"]]["family"]), "searchable": r["gold_person"] not in qr.absent,
                     "errors": r["errors"]} for r in rec.records]
    relations = []
    for fam in world.families:
        ms = [people[m] for m in fam["members"]]
        for i, a in enumerate(ms):
            for b in ms[i + 1:]:
                rel = "spouse" if {a["role"], b["role"]} == {"mother", "father"} else \
                      "sibling" if a["role"] == b["role"] == "child" else "parent_child"
                relations.append({"a": a["id"], "b": b["id"], "relation": rel, "family": fam["id"]})
    hard = [{"a": p["id"], "b": p["lookalike_of"], "kind": "lookalike",
             "same_name": [e["text"] for e in p["name"]] == [e["text"] for e in people[p["lookalike_of"]]["name"]]}
            for p in world.people if "lookalike_of" in p]
    gold_people = [{"id": p["id"], "family": p["family"], "origin": p["origin"], "sex": p["sex"],
                    "birth_year": p["birth_year"], "minor": p["minor"], "name_change": p.get("name_change", 0),
                    "split": splits.get(p["family"])} for p in world.people]
    for g in qr.gold:
        if g.get("sought_person"):
            g["split"] = splits.get(people[g["sought_person"]]["family"])
    for row in public_records + qr.queries:
        if forbidden_keys(row):
            raise ValueError(f"forbidden field in public output: {forbidden_keys(row)}")
    files = {
        "public/records.jsonl": public_records, "public/queries.jsonl": qr.queries,
        "gold/records.jsonl": gold_records, "gold/queries.jsonl": qr.gold, "gold/people.jsonl": gold_people,
        "gold/relations.jsonl": relations, "gold/hard_negatives.jsonl": hard,
    }
    for name, rows in files.items():
        _write_jsonl(out / name, rows)
    return {name: _sha(out / name) for name in files}


def query_size_check(qr, splits):
    """Test queries with a findable answer per key slice (origin x child/adult), against the
    number needed to show recall@20 >= 0.95 on that slice (sample_size.queries_for_recall)."""
    need = queries_for_recall()
    counts = Counter()
    for g in qr.gold:
        if g["expected"] == "found" and splits.get(qr.people[g["sought_person"]]["family"]) == "test":
            p = qr.people[g["sought_person"]]
            counts[f"{p['origin']}/{'child' if p['minor'] else 'adult'}"] += 1
    return {"needed_per_slice": need, "test_found_queries": dict(sorted(counts.items())),
            "ok": len(counts) == 6 and min(counts.values()) >= need}


def summary(qr):
    g = qr.gold
    return {
        "queries": len(g),
        "kinds": dict(Counter(x["kind"].split(":")[0] for x in g)),
        "expected": dict(Counter(x["expected"] for x in g)),
        "child_reporters": sum(x.get("child_reporter", False) for x in g),
        "reciprocal_same_clerk_pairs": sum(x.get("same_clerk", False) for x in g) // 2,
        "by_split": dict(Counter(x.get("split") for x in g if "split" in x)),
    }


def build(params, out, people=None):
    out = Path(out)
    world = World(params, people=people).generate()
    rec = Recorder(world, params).generate()
    qr = Querier(world, rec, params).generate()
    splits = split_families(world, random.Random(params["seed"] + 3))
    checks = write_set(out, world, rec, qr, splits)
    _write_jsonl(out / "gold" / "splits.jsonl", [{"family": f, "split": s} for f, s in sorted(splits.items())])
    checks["gold/splits.jsonl"] = _sha(out / "gold" / "splits.jsonl")

    hp = holdout_params(params)
    n_hold = round((people or params["params"]["people"]["value"]) * params["params"]["holdout_share"]["value"])
    hworld = World(hp, seed=params["seed"] + 100, people=n_hold, prefix="h").generate()
    hrec = Recorder(hworld, hp, seed=params["seed"] + 100).generate()
    hq = Querier(hworld, hrec, hp, seed=params["seed"] + 100).generate()
    hsplits = {f["id"]: "holdout" for f in hworld.families}
    for name, sha in write_set(out / "holdout", hworld, hrec, hq, hsplits).items():
        checks["holdout/" + name] = sha

    manifest = {
        "generator": ["namebridge.benchmark.world", "namebridge.benchmark.records", "namebridge.benchmark.queries"],
        "params": PARAMS.name, "seed": params["seed"], "frozen": False,
        "freeze_note": "Test and holdout are frozen only after gate G4 fixes the tolerances (BENCHMARK_PROTOCOL.md §3, §8)",
        "world": world.summary(), "records": rec.summary(), "queries": summary(qr),
        "query_size_check": query_size_check(qr, splits),
        "holdout": {"people": len(hworld.people), "records": len(hrec.records), "queries": summary(hq)},
        "sha256": checks,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main(argv):
    opt = lambda flag, default=None: argv[argv.index(flag) + 1] if flag in argv else default
    params = json.loads(PARAMS.read_text(encoding="utf-8"))
    people = opt("--people")
    m = build(params, opt("--out", ROOT / "build" / "benchmark"), int(people) if people else None)
    print(json.dumps({k: m[k] for k in ("queries", "query_size_check", "holdout")}, ensure_ascii=False, indent=2))
    if not m["query_size_check"]["ok"] or not m["world"]["size_check"]["ok"]:
        sys.exit("too small for the targets: see size_check and query_size_check in manifest.json")


if __name__ == "__main__":
    main(sys.argv[1:])
