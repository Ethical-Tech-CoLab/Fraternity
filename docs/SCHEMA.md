# NameBridge — data schema in plain language

For reviewers who don't read Python: the professor, linguists and community experts. The code is in `namebridge/src/namebridge/schema/`; every rule below is checked automatically by the validators and by the test suite, which runs on GitHub on every push. Written 28 Oct 2026 (week 3).

There are **two separate graphs** (`CONCEPT-IDEA.md` §5.1). They never mix.

## 1. The public name dictionary (Name Knowledge Graph)

Knowledge about names, **never about people**. Public, CC BY 4.0. Files: `namebridge/data/graph/nodes.jsonl` and `edges.jsonl`.

**Things in it (nodes):** a written name form (`NameForm`, e.g. *Havyarimana* in Latin script), a name concept, a morpheme (a meaningful part, e.g. *-imana*), a script, a language, a locale, a region, a rule, and a source.

**Links (edges)** say how two names relate: spelling variant, sound variant, romanisation, transliteration, nickname, formal form, historical cognate (*Jean* / *Yohana*), derived from, contains a morpheme, inflected form, previous or married form (as a general rule only), commonly confused with, and **not equivalent to** (a negative rule).

**Every link must have:**

| Field | Meaning |
| --- | --- |
| source name, URL, excerpt or page | where the claim comes from |
| languages and regions | where it applies |
| confidence (0–1) and its basis | attested, statistical, expert, generated or disputed |
| reversible | whether it works both ways |
| review status | proposed, reviewed or deprecated |
| reviewer role | required once reviewed: linguist, community expert, investigator or data steward |
| licence | of the source |

**Rules the validator enforces:**

1. **No link without a source**, even a proposed one.
2. **AI-generated links stay "proposed"** until a person reviews them.
3. **Spelling and sound variants must look alike.** The similarity score (Jaro-Winkler) must be at least 0.8; that threshold gave the best results in a real-world study (Grannis et al. 2004). Real variants pass (*Habyarimana* / *Havyarimana* 0.95; *Kakolele* / *Kakorere* 0.90; *Ciza* / *Tchiza* 0.89). Unrelated names fail (*Jean* / *Hamisi* 0.47). A real variant below 0.8 is accepted only if it is reviewed, has an attested or expert source, and gives a reason.
4. **An adopted name is never a variant.** There is no link type for "changed name", and rule 3 blocks disguising one as a spelling variant (`NAME_CHANGE.md` rule 1). The restricted name-change layer (G5) is separate and never in this public dictionary.
5. **Links join the right kinds of thing**: a morpheme link points to a morpheme; a transliteration joins two different scripts.
6. **No duplicates and no contradictions**: two names cannot be both "variant" and "not equivalent".
7. **Names are stored in one Unicode form (NFC)**, so the same accented name is never stored two invisible ways (W3C recommendation).
8. **No ethnicity, clan, tribe, caste, race or religion attribute anywhere.**

## 2. The protected case data (Case graph)

Records about people: **schema only this semester**, kept empty; tested with invented records.

**Every case record must have:** a legal basis (vital interest, public interest, consent or legal obligation; Malawi Data Protection Act s. 8); with whom it may be shared; its protection flags and route; the other names the person uses; whether a name change is possible; and **when it was created and when it must be deleted**.

**Every name as observed** keeps the exact text, the script, the source type (oral report, form, passport, registry, flyer…), the label of the field it came from, and the order as written; names are never reordered. **If the name was told aloud** (an oral report), the record also says which spelling habits the person who wrote it down used (French, English, Kirundi…), so the search can work back to the sounds (`CONCEPT-IDEA.md` §5.4A).

**Every fact** says who asserted it, when, under what authority, how sensitive it is, how sure, and with whom it may be shared.

**Rules the validator enforces:**

1. **Minors are always protected:** a minor's case must be flagged and take the protected route.
2. **A possible name change is protected:** flagged, protected route (`NAME_CHANGE.md` rule 2).
3. **Any flag means the protected route.**
4. **Consent for a minor comes from a parent or guardian** (Malawi DPA s. 17).
5. **Only a person can confirm a match**; never the system.
6. **A name alone never confirms a match**: a confirmation needs at least one piece of non-name evidence (age, date of birth, sex, family, place, event, document, photo check, or a question only the family can answer).
7. **Family relationships are reported by someone, never inferred.**
8. **Biometrics only as a pointer** to an authorised system; raw fingerprints, iris data or face images are refused.
9. **Contact and location data are always high sensitivity.**
10. **No ethnicity, clan or religion field.**

## 3. Reading CPIMS+ / Primero records

Only listed fields are read: name, other names, nickname, date of birth, age, sex, relationship, relatives' names, nicknames and ages (also inside Primero's nested family section), and consent for tracing.

- **A case without consent for tracing is refused whole**, as in Primero's own matching.
- **Ethnicity, sub-ethnicity and religion are refused at any depth.** Only the field name is reported; the value is never copied.
- **Anything else is dropped**, including allowed fields that unexpectedly hold nested data.
- The names read are turned into "observed names" that must pass the case schema above.

## 4. Language packs

One file per language (`namebridge/data/packs/`, starting from `TEMPLATE.json`). A pack describes name structure, name order, morphemes, spelling and sound rules, administrative forms, the **sound layer** (sound inventory, spelling habits by writer language, sounds listeners confuse), what shared surnames mean for kinship, known failure modes, and test cases.

**Every rule needs a source and a confidence** (high, medium, low, unknown, disputed, or hypothesis). Structure and order rules also say whether they describe cultural practice, legal documents or database convention. "Unknown" and "disputed" are allowed instead of forcing a rule. **No pack encodes ethnicity, clan or religion.**

## Sources

- Grannis, S. J. et al. (2004), "Real world performance of approximate string comparators for use in patient matching", [PubMed 15360771](https://pubmed.ncbi.nlm.nih.gov/15360771): Jaro-Winkler at 0.8 gave the highest linkage sensitivity.
- W3C, [Character Model for the World Wide Web: String Matching](https://www.w3.org/TR/charmod-norm): "Content authors SHOULD use Unicode Normalization Form C (NFC)".
- Primero, `db/dev_fixtures/cases.rb` and `doc/api/traces/id/get.md` ([github.com/primeroIMS/primero](https://github.com/primeroIMS/primero), checked 28 Oct 2026): relatives nested in `family_details_section` for cases; flat `relation_name` for traces.
- Zorc, R. D. & Nibagwire, L. (2007), *Kinyarwanda and Kirundi Comparative Grammar*, Dunwoody Press (authors confirmed via [Stanford SearchWorks](https://searchworks.stanford.edu/view/7513422) and [WorldCat](https://search.worldcat.org/title/Kinyarwanda-and-Kirundi-comparative-grammar/oclc/182537195)).
