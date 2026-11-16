"""Synthetic world for the benchmark, step 1: invented people, families and names (week 6).

BENCHMARK_PROTOCOL.md §2.1-2.2 and §2.4. Reality enters as patterns with sources, never as
people: name elements are drawn from the naming profiles (elements seen 5+ times, aggregates
only) in proportion to their counts, and the share of names a profile does not cover is filled
with INVENTED elements (character trigrams of that slot's listed elements). Christian given
names are a closed set, so they are never invented: uncovered slots draw from the corridor-wide
pool of the same sex. No full name is ever copied, because no real full name is held.

Every parameter, with its source and confidence, is in data/benchmark/params-*.json. The size
is a parameter (`people`), so the world can be regenerated when gate G4 fixes the tolerances.
Nothing about ethnicity, clan, tribe or religion is generated (C12); the output is checked with
the schema's multilingual field guard.

Run: python -m namebridge.benchmark.world [--people N] [--seed S] [--out build/benchmark]
"""

import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

from namebridge.benchmark.sample_size import design_effect, minimum_people
from namebridge.schema import forbidden_keys

ROOT = Path(__file__).resolve().parents[3]
PARAMS = ROOT / "data" / "benchmark" / "params-2026.1.json"
PROFILES = ROOT / "data" / "profiles"
SEXES = ("F", "M")


def _load(name):
    return json.loads((PROFILES / name).read_text(encoding="utf-8"))


class Pool:
    """Weighted elements for one slot, with the share of real names they cover."""

    def __init__(self, items, coverage, source):
        self.items = [(e, w) for e, w in items if w > 0]
        self.coverage = max(0.0, min(1.0, coverage))
        self.source = source

    def draw(self, rng):
        elems, weights = zip(*self.items)
        return rng.choices(elems, weights)[0]


class Inventor:
    """Character-trigram chain over one slot's listed elements; never returns a listed element."""

    def __init__(self, elements):
        self.listed = {e for e, _ in elements}
        self.next = defaultdict(Counter)
        lengths = []
        for e, w in elements:
            s = "^^" + e + "$"
            lengths.append(len(e))
            for i in range(len(s) - 2):
                self.next[s[i:i + 2]][s[i + 2]] += w
        self.min_len, self.max_len = max(3, min(lengths)), max(lengths)

    def invent(self, rng, tries=200):
        for _ in range(tries):
            s = "^^"
            while len(s) < self.max_len + 3:
                options = self.next.get(s[-2:])
                if not options:
                    break
                ch = rng.choices(list(options), list(options.values()))[0]
                if ch == "$":
                    break
                s += ch
            word = s[2:]
            if self.min_len <= len(word) <= self.max_len and word not in self.listed:
                return word
        raise RuntimeError("could not invent a new element")


def build_pools():
    """Pools per (origin, slot, sex), from the profiles. Coverage = listed counts / records."""
    ceni, nec, nisr = _load("bi-ceni-2026.1.json"), _load("rw-nec-2026.1.json"), _load("rw-nisr-2026.1.json")
    derived, cd = _load("bi-derived-2026.1.json"), _load("cd-congonames-2026.1.json")
    pools = {}

    def by_sex(rows, sex):
        return [(r["element"], r["count"]) for r in rows if r.get("sex") == sex]

    def coverage(rows, total):
        return sum(r["count"] for r in rows) / total

    ceni_rows = ceni["structure"]["rows_parsed"]
    ceni_prenoms = sum(int(k) * v for k, v in ceni["structure"]["number_of_prenom_tokens"].items())
    nec_rows = nec["structure"]["rows_parsed"]
    cd_rows = cd["structure"]["records"]
    births = nisr["births_registered_in_year"]
    nisr_cov = sum(sum(r["count"] for r in rows) for rows in nisr["elements"].values()) / sum(births.values())

    for sex in SEXES:
        low = sex.lower()
        pools["BI", "kirundi", sex] = Pool(by_sex(ceni["elements_by_sex"]["nom"], sex),
                                           coverage(ceni["elements"]["nom"], ceni_rows), "bi-ceni-2026.1")
        pools["BI", "christian", sex] = Pool(by_sex(ceni["elements_by_sex"]["prenom"], sex),
                                             coverage(ceni["elements"]["prenom"], ceni_prenoms), "bi-ceni-2026.1")
        young_bi = [(r["element"], r["count"]) for k, rows in derived["elements"].items()
                    if k.split("_")[-2] == {"F": "female", "M": "male"}[sex] for r in rows]
        # bi-derived is converted from Rwanda's newborn lists, so it borrows their coverage (low confidence)
        pools["BI", "kirundi_young", sex] = Pool(young_bi, nisr_cov, "bi-derived-2026.1")
        pools["RW", "kinyarwanda", sex] = Pool(by_sex(nec["elements_by_sex"]["first_position"], sex),
                                               coverage(nec["elements"]["first_position"], nec_rows), "rw-nec-2026.1")
        pools["RW", "christian", sex] = Pool(by_sex(nec["elements_by_sex"]["last_position"], sex),
                                             coverage(nec["elements"]["last_position"], nec_rows), "rw-nec-2026.1")
        young_rw = [(r["element"], r["count"]) for k, rows in nisr["elements"].items()
                    if k.split("_")[-2] == {"F": "female", "M": "male"}[sex] for r in rows]
        pools["RW", "kinyarwanda_young", sex] = Pool(young_rw, nisr_cov, "rw-nisr-2026.1")
        pools["CD", "nom", sex] = Pool([(r["element"], r[low]) for r in cd["elements"]["first_token_top50"]],
                                       coverage(cd["elements"]["first_token_top50"], cd_rows), "cd-congonames-2026.1")
        pools["CD", "christian", sex] = Pool([(r["element"], r[low]) for r in cd["elements"]["last_token_top50"]],
                                             coverage(cd["elements"]["last_token_top50"], cd_rows), "cd-congonames-2026.1")
    # NEC's middle position mixes sexes (jean, marie, de, jeanne). Compounds follow the given name's
    # sex (Jean Claude, Marie Claire, Jeanne d'Arc), so the pool is split by that rule; "de" is
    # dropped because it only occurs inside compounds such as "Jean de Dieu".
    middle = {r["element"]: r["count"] for r in nec["elements"]["middle_position"]}
    for sex, keep in (("F", ("marie", "jeanne")), ("M", ("jean",))):
        pools["RW", "middle", sex] = Pool([(e, middle[e]) for e in keep if e in middle], 1.0, "rw-nec-2026.1")

    # corridor-wide Christian pool per sex: each profile's shares, weighted equally
    for sex in SEXES:
        merged = Counter()
        for origin in ("BI", "RW", "CD"):
            p = pools[origin, "christian", sex]
            total = sum(w for _, w in p.items)
            for e, w in p.items:
                merged[e] += w / total
        pools["ALL", "christian", sex] = Pool(sorted(merged.items()), 1.0, "all three profiles")
    return pools


def build_inventors(pools):
    inv = {}
    for (origin, slot, sex), pool in pools.items():
        if slot in ("christian", "middle") or origin == "ALL":
            continue
        key = (origin, slot.replace("_young", ""))
        inv.setdefault(key, []).extend(pool.items)
    return {k: Inventor(v) for k, v in inv.items()}


class World:
    def __init__(self, params, seed=None, people=None, prefix=""):
        self.prefix = prefix  # e.g. "h" for the temporal holdout, so ids never collide
        self.p = params["params"]
        self.year = params["reference_year"]
        self.seed = params["seed"] if seed is None else seed
        self.target = self.p["people"]["value"] if people is None else people
        self.rng = random.Random(self.seed)
        self.pools = build_pools()
        self.inventors = build_inventors(self.pools)
        self.people, self.families, self.by_id = [], [], {}
        self.provinces = self._provinces()
        self.lookalike_swaps = _lookalike_swaps()

    # --- names -------------------------------------------------------------------------------
    def _element(self, origin, slot, sex):
        """Draw from the profile with its coverage, otherwise invent (or use the corridor pool)."""
        pool = self.pools[origin, slot, sex]
        if self.rng.random() < pool.coverage:
            return {"text": pool.draw(self.rng), "slot": slot.replace("_young", ""), "basis": "profile", "source": pool.source}
        if slot == "christian":
            alt = self.pools["ALL", "christian", sex]
            return {"text": alt.draw(self.rng), "slot": "christian", "basis": "corridor_pool", "source": alt.source}
        word = self.inventors[origin, slot.replace("_young", "")].invent(self.rng)
        return {"text": word, "slot": slot.replace("_young", ""), "basis": "invented", "source": pool.source}

    def _count(self, dist):
        keys = list(dist)
        return int(self.rng.choices(keys, [dist[k] for k in keys])[0])

    def _christian(self, origin, sex, avoid=()):
        for _ in range(50):
            e = self._element(origin, "christian", sex)
            if e["text"] not in avoid:
                return e
        return e

    def name(self, origin, sex, birth_year, father=None, mother=None, siblings=()):
        young = birth_year >= self.p["young_child_birth_year"]["value"]
        father_texts = {e["text"] for e in father["name"]} if father else set()
        if origin == "RW":
            if father and self.rng.random() < self.p["rw_father_element_q"]["value"]:
                kiny = dict(next(e for e in father["name"] if e["slot"] == "kinyarwanda"), basis="inherited")
            else:
                kiny = self._element("RW", "kinyarwanda_young" if young else "kinyarwanda", sex)
            n = min(3, self._count(self.p["rw_names_per_person"]["value"]))
            elems = [kiny]
            if n == 3:
                mid = self.pools["RW", "middle", sex]
                elems.append({"text": mid.draw(self.rng), "slot": "christian", "basis": "profile", "source": mid.source})
            elems.append(self._christian("RW", sex, avoid=father_texts))
            return elems  # civil order: Kinyarwanda name first (surname-first records)
        if origin == "BI":
            if father and sex == "M" and self.rng.random() < self.p["bi_son_father_name_p"]["value"]:
                nom = dict(next(e for e in father["name"] if e["slot"] == "kirundi"), basis="inherited")
            else:
                nom = self._element("BI", "kirundi_young" if young else "kirundi", sex)
            n = self._count(self.p["bi_prenom_tokens"]["value"])
            prenoms, used = [], set(father_texts)
            for _ in range(n):
                e = self._christian("BI", sex, avoid=used)
                used.add(e["text"])
                prenoms.append(e)
            return [nom] + prenoms  # civil order: Nom then Prénoms
        # CD: nom, postnom, prénom (Family Code arts 56-62)
        parent = father or mother
        n = self._count(self.p["cd_token_count"]["value"])
        taken = {e["text"] for s in siblings for e in s["name"] if e["slot"] == "postnom"}
        if parent and self.rng.random() < self.p["cd_parent_nom_t"]["value"]:
            nom = dict(next(e for e in parent["name"] if e["slot"] == "nom"), basis="inherited")
        else:
            nom = self._element("CD", "nom", sex)
        elems = [nom]
        if n >= 3:
            for _ in range(50):
                post = dict(self._element("CD", "nom", sex), slot="postnom")
                if post["text"] != nom["text"] and post["text"] not in taken:
                    break
            elems.append(post)
        elems.append(self._christian("CD", sex, avoid=father_texts))
        if n >= 4:
            elems.append(self._christian("CD", sex, avoid={e["text"] for e in elems}))
        return elems

    # --- people and families ------------------------------------------------------------------
    def _provinces(self):
        ceni, nec, cd = _load("bi-ceni-2026.1.json"), _load("rw-nec-2026.1.json"), _load("cd-congonames-2026.1.json")
        return {
            "BI": ceni["structure"]["by_province"],
            "RW": nec["structure"]["by_province"],
            "CD": {r["province"]: r["total"] for r in cd["by_province"] if r["province"] != "autre"},
        }

    def _person(self, family, origin, sex, birth_year, role, **kin):
        pid = f"{self.prefix}p{len(self.people) + 1:06d}"
        person = {"id": pid, "family": family["id"], "origin": origin, "sex": sex, "birth_year": birth_year,
                  "role": role, "minor": self.year - birth_year < 18,
                  "name": self.name(origin, sex, birth_year, **kin)}
        self.people.append(person)
        self.by_id[pid] = person
        family["members"].append(pid)
        return person

    def lookalike_family(self):
        """Hard negatives (§2.3): a different family built to look like an existing one.

        Each member mirrors a source member: same origin and province, birth year within 2,
        and either the SAME name (homonyms: the Eloi example in DECISIONS_OPEN.md) or a name
        one attested step away, from the negative constraints in attested-variants (Ishimwe /
        Nishimwe, Jean / Jeanne...). A sex-marked swap flips the mirror's sex to match."""
        src = self.rng.choice([f for f in self.families if not f.get("lookalike_of")])
        members = [self.by_id[m] for m in src["members"]]
        fam = {"id": f"{self.prefix}f{len(self.families) + 1:05d}", "origin": src["origin"],
               "province_of_origin": src["province_of_origin"], "members": [], "lookalike_of": src["id"],
               "mother": None, "father": None, "older_household": src.get("older_household", False)}
        self.families.append(fam)
        for m in members:
            sex, name = m["sex"], [dict(e) for e in m["name"]]
            if self.rng.random() < self.p["lookalike_near_share"]["value"]:
                for i, e in enumerate(name):
                    swap = self.lookalike_swaps.get(e["text"])
                    if swap:
                        name[i] = dict(e, text=swap[0], basis="lookalike")
                        if swap[1]:
                            sex = swap[1]
                        break
            year = min(self.year, m["birth_year"] + self.rng.randint(-2, 2))
            pid = f"{self.prefix}p{len(self.people) + 1:06d}"
            person = {"id": pid, "family": fam["id"], "origin": m["origin"], "sex": sex, "birth_year": year,
                      "role": m["role"], "minor": self.year - year < 18, "name": name, "lookalike_of": m["id"]}
            self.people.append(person)
            self.by_id[pid] = person
            fam["members"].append(pid)
            if m["role"] in ("mother", "father") and sex == m["sex"]:
                fam[m["role"]] = pid
        return fam

    def family(self):
        if self.families and self.rng.random() < self.p["lookalike_family_share"]["value"]:
            return self.lookalike_family()
        origins = self.p["origin_shares"]["value"]
        origin = self.rng.choices(list(origins), list(origins.values()))[0]
        prov = self.provinces[origin]
        fam = {"id": f"{self.prefix}f{len(self.families) + 1:05d}", "origin": origin,
               "province_of_origin": self.rng.choices(list(prov), list(prov.values()))[0], "members": []}
        self.families.append(fam)
        older = self.rng.random() < self.p["older_household_share"]["value"]
        lo, hi = self.p["older_parent_birth_years" if older else "parent_birth_years"]["value"]
        mother_year = self.rng.randint(lo, hi)
        mother = self._person(fam, origin, "F", mother_year, "mother")
        father = None
        if self.rng.random() < self.p["two_parent_share"]["value"]:
            father = self._person(fam, origin, "M", max(lo - 10, mother_year - self.rng.randint(0, 10)), "father")
        a, b = self.p["mother_age_at_first_child"]["value"]
        s1, s2 = self.p["birth_spacing_years"]["value"]
        year = mother_year + self.rng.randint(a, b)
        children = []
        for _ in range(self._count(self.p["children_per_family"]["value"])):
            if year > self.year:
                break
            sex = self.rng.choice(SEXES)
            children.append(self._person(fam, origin, sex, year, "child", father=father, mother=mother, siblings=children))
            year += self.rng.randint(s1, s2)
        fam["mother"], fam["father"] = mother["id"], father["id"] if father else None
        fam["older_household"] = older
        return fam

    def generate(self):
        while len(self.people) < self.target:
            self.family()
        return self

    def size_check(self):
        """Is this world big enough for the §7 targets, given its REALISED minors and family size?"""
        n = len(self.people)
        minors, per_family = sum(p["minor"] for p in self.people) / n, n / len(self.families)
        need = minimum_people(minors, design_effect(per_family))
        return {"needed": need["total"], "binding": need["binding"], "design_effect": round(design_effect(per_family), 3),
                "ok": n >= need["total"]}

    # --- report --------------------------------------------------------------------------------
    def summary(self):
        n = len(self.people)
        basis = Counter((p["origin"], e["slot"], e["basis"]) for p in self.people for e in p["name"] if "lookalike_of" not in p)
        slots = Counter((o, s) for o, s, _ in basis.elements())
        return {
            "people": n, "families": len(self.families),
            "people_per_family": round(n / len(self.families), 2),
            "lookalike_people": sum("lookalike_of" in p for p in self.people),
            "minor_share": round(sum(p["minor"] for p in self.people) / n, 3),
            "age_bands": dict(sorted(Counter(min(70, (self.year - p["birth_year"]) // 10 * 10) for p in self.people).items())),
            "origin_counts": dict(Counter(p["origin"] for p in self.people)),
            "sex_counts": dict(Counter(p["sex"] for p in self.people)),
            "size_check": self.size_check(),
            "element_basis_share": {f"{o}/{s}/{b}": round(c / slots[o, s], 3) for (o, s, b), c in sorted(basis.items())},
        }


def _lookalike_swaps():
    """Element -> (other element, sex of the other or None), from the attested negative constraints."""
    data = json.loads((ROOT / "data" / "variants" / "attested-variants-2026.1.json").read_text(encoding="utf-8"))
    forms = {f["id"]: f["text"].lower() for f in data["forms"]}
    sexed = {"françoise": "F", "francoise": "F", "justine": "F", "jeanne": "F", "claudine": "F",
             "françois": "M", "francois": "M", "justin": "M", "jean": "M", "claude": "M"}
    swaps = {}
    for r in data["relations"]:
        if r["relation_type"] == "not_equivalent_to":
            a, b = forms[r["from"]], forms[r["to"]]
            swaps.setdefault(a, (b, sexed.get(b)))
            swaps.setdefault(b, (a, sexed.get(a)))
    for a, b in (("francoise", "francois"),):  # profiles are folded (no cedilla)
        swaps.setdefault(a, (b, "M"))
        swaps.setdefault(b, (a, "F"))
    return swaps


def full_name(person):
    """The civil-order full name, surname-first in capitals where records write it so (§2.2)."""
    e = person["name"]
    if person["origin"] in ("RW", "BI"):
        return " ".join([e[0]["text"].upper()] + [x["text"].capitalize() for x in e[1:]])
    return " ".join(x["text"].upper() if x["slot"] in ("nom", "postnom") else x["text"].capitalize() for x in e)


def write(world, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    problems = [k for p in world.people for k in forbidden_keys(p)]
    if problems:
        raise ValueError(f"forbidden fields in generated people: {sorted(set(problems))}")
    with open(out / "people.jsonl", "w", encoding="utf-8") as f:
        for p in world.people:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    with open(out / "families.jsonl", "w", encoding="utf-8") as f:
        for fam in world.families:
            f.write(json.dumps(fam, ensure_ascii=False) + "\n")
    manifest = {"generator": "namebridge.benchmark.world", "params": PARAMS.name, "seed": world.seed,
                "target_people": world.target, "summary": world.summary()}
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main(argv):
    opt = lambda flag, default=None: argv[argv.index(flag) + 1] if flag in argv else default
    params = json.loads(PARAMS.read_text(encoding="utf-8"))
    people = opt("--people")
    seed = opt("--seed")
    world = World(params, seed=int(seed) if seed else None, people=int(people) if people else None).generate()
    manifest = write(world, opt("--out", ROOT / "build" / "benchmark"))
    print(json.dumps(manifest["summary"], ensure_ascii=False, indent=2))
    check = manifest["summary"]["size_check"]
    if not check["ok"]:
        sys.exit(f"too small: {len(world.people)} people, the targets need {check['needed']} ({check['binding']})")


if __name__ == "__main__":
    main(sys.argv[1:])
