# NameBridge — intake guide for names and relationship evidence

**Status:** draft, 9 Nov 2026 (week 5). Derived from the language packs, the DPIA and the data rules. **Not yet tested with caseworkers or communities**: that needs a partner and ethics review (phase 3, `IRB_DETERMINATION.md`). For the professor's and a partner's review.

**Who it is for:** a caseworker, volunteer or interpreter taking a tracing request or registering a person, in Dzaleka or elsewhere in the corridor (Burundi, Rwanda, DRC, Malawi).

**What it is for:** recording names and relationships so that a search can find the right family later. Names in this corridor change with the language of whoever writes them, with age, with marriage and with exile; a careful record keeps every form and says who wrote it.

Each instruction cites its basis: a pack rule (`pack:rule-id`), a data rule (`DATA_RULES.md` DR-x) or a document.

---

## 1. Never record

- **Ethnicity, clan, tribe or religion**, as a field or a note, even if the person offers it or an old document shows it (`DATA_RULES.md` DR-1.6, DR-1.7; `DPIA.md` (d)).
- **Photographs, fingerprints or iris scans** in NameBridge (`DPIA.md` (d)).
- The enquirer's **phone number or address**: the partner holds those, not NameBridge (`DPIA.md` (d)).

And never **infer**:

- **sex from a name**: most common Kinyarwanda and Kirundi names are given to both sexes (`rw-kiny:kinyarwanda-names-unisex`);
- **credibility from names**: different names in different records are normal, never a sign of lying (`NAME_CHANGE.md` rule 4).

## 2. Before you start

1. **Use the person's language** or an interpreter they trust.
2. Note **who will write the names**, because spelling depends on the writer (§5).
3. If the person **can write**, ask them to write their own names. Record `written_by: self`.
4. Tell them they may give **the names they choose**. Do not press for a "real" or "original" name (`NAME_CHANGE.md` rule 6; DR-1.8).

## 3. The person's own names

Record **every name as given, in the order given**, exactly as said or written (`observed_full_name`, `source_order`). Do not reorder, shorten or "correct" it. Then ask for **other names used** (`other_names_used`): baptismal names, nicknames, names used at school or work, names used before or after leaving home.

What to expect by origin:

| Origin | What a name usually looks like | Ask or note |
| --- | --- | --- |
| **DRC** | prénom + nom + postnom; official lists write **nom, postnom, prénom** (Christian name last) | All three parts; which part is which; whether a prénom was used only in daily life (people registered 1972–1997 may have no prénom on papers) (`cd-swc-ln:structure-prenom-nom-postnom`, `order-exam-lists-nom-first-prenom-last`, `authenticite-prenom-gap`) |
| **Rwanda** | Kinyarwanda name + Christian name; official documents put the **Kinyarwanda name first** | Both; brothers and sisters usually have **different** Kinyarwanda names, so a different name is not evidence against kinship (`rw-kiny:structure-law-71-2024`, `order-surname-first-uppercase`) |
| **Burundi** | Kirundi name + Christian name; lists put the Kirundi name in a "Nom" column first | Both; whether the family shares a name or each child has their own (both happen) (`bi-kirundi:structure-kirundi-first-then-christian`, `structure-inheritance-disputed`) |

**Compound Christian names** are often written in two or three words: Jean-Marie Vianney, Jean de Dieu, Jean Bosco, Dieu Donné. Record the full form and do not drop parts (`rw-kiny:compound-christian-name-split`, `cd-swc-ln:compound-prenom-split`).

**Names that look like "no name"** (Kirundi *Ntazina* "no name", *Busabusa* "nothing") are **real names**: record them (`bi-kirundi:name-means-no-name`).

## 4. Children

A young child is often the only witness. Their account is valuable even when incomplete.

- **They may not know a parent's own name.** Children usually do not call parents by name; expect "Mama", "Papa" or "Mama X" (`rw-kiny:child-avoids-parent-name`).
- **"Mama X" has two meanings.** X may be the mother's **own** name ("Ms. X") **or** the name of one of her **children** ("mother of X"). Record exactly what the child said and do not decide which it is (`rw-kiny:mama-x-two-readings`, `cd-swc-ln:mama-x-two-readings`).
- **They may not want to say their own name.** In Rwanda, children under about 15 are taught not to; a child who gives no name, or only a nickname, is not hiding anything (`rw-kiny:child-withholds-own-name`).
- **Young children's pronunciation:** r may be said as l, and long names may be cut to their last syllables (*Nshimirimana* heard as "Mana"). Record what you heard, mark it as **heard from a child** (`oral_report`), and add your best spelling as a separate note (`cd-swc-ln:child-r-to-l`, `child-weak-syllable-deletion`).
- **A child registered without known parents** may carry a name **given by a civil registrar** (DRC Family Code art. 60), unrelated to the family's names. Record it, and record any name the child remembers being called at home (`cd-swc-ln:structure-foundling-name`).
- Mark the record **`subject_is_minor`**. Minors are protected cases (`DATA_RULES.md` DR-4.4).

## 5. Who wrote the name

Spelling changes with the writer's language. Record:

- **`written_by`**: self, other, or unknown;
- **`recorded_by_convention`**: the writer's language habits (Kirundi, Kinyarwanda, French, English, Swahili, Chichewa).

Examples the matcher uses, so the writer's habits must be known:

- A **French** writer may write *ou* for w, *ch* for sh, *tch* or *tsh* for the "ch" sound, *dj* for j (`*:spelling_conventions`).
- A **Chichewa** writer (Malawian clerk) writes **r only after i or e and l elsewhere**, and **l at the start of a word**: *Rukundo* may become "Lukundo" (`*:spelling_conventions` writer `ny`).
- A **Kinyarwanda** writer writes *by* where Kirundi writes *vy* (Habyarimana / Havyarimana) (`bi-kirundi:rw-to-rn-by`).

If you are not sure how a name is spelled, **write it as you heard it and say so**; never guess a "standard" spelling in its place.

## 6. Relatives and relationship evidence

Record **parents' and caregivers' names** (`DPIA.md` (d)): in Rwanda and Burundi, parents' names show kinship better than surnames.

- **"X mwene Y"** (Kirundi) means "X, child of Y": Y is the father's name (`bi-kirundi:structure-mwene-filiation`).
- **Titles are not names:** *Nyirababiri* "mother of twins", *Sebabiri* "father of twins" (`bi-kirundi:structure-twin-parent-titles`); "Mama"/"Papa" used as respect for any adult (§4).
- **A wife may not say her husband's name**, or her parents-in-law's (Rwanda, *gutsinda*). Let her give a title, a teknonym ("father of X") or have someone else say it; this is not a sign of a false claim (`rw-kiny:wife-avoids-husband-name`).
- **Married names:** in Rwanda (since 2024) and the DRC a spouse may **add** the other's name; record names with and without it (`rw-kiny:structure-spouse-name-added`, `cd-swc-ln:structure-married-woman`).
- **Birth-order and twin names** (Burundi: *Nyandwi* 7th child, *Bukuru*/*Butoyi* twins) are common names; record them, but they are not on their own evidence of a family link (`bi-kirundi:structure-birth-order-names`).
- Record relationships **as reported** (`reported_parent_of`, `reported_sibling_of`, `reported_spouse_of`), not as facts.

## 7. Places

Record the place **as the person names it**, even if it has since been renamed (Usumbura for Bujumbura; Gitarama for Muhanga; former provinces): the place graph links old and new names (`places-2026.1`). Ask for the place where the family **was last together** and where the person **was born**, at the level the person knows (province, town, hill).

The country of origin does **not** fix the language of the name: Burundi has long-settled Kinyarwanda- and Swahili-speaking communities (`bi-kirundi:origin-country-not-naming-language`).

## 8. People who may not want to be found, and changed names

- If the person says they changed their name, or someone may be looking for them to harm them, mark **`may_not_wish_to_be_found`** or **`possible_name_change`**. These are protected cases, routed to a senior caseworker (`NAME_CHANGE.md` rules 2 and 5; `DATA_RULES.md` DR-4.4).
- A formal change of name leaves **documents under the old name valid** (Rwanda Law 71/2024 art. 43): record both if the person gives both (`rw-kiny:documents-under-former-name`).

## 9. Checklist

| Field | Required | Notes |
| --- | --- | --- |
| `observed_full_name` + `source_order` | yes | exactly as given |
| `other_names_used` | yes (ask) | baptismal, nickname, school or work names; names before or after exile |
| `written_by`, `recorded_by_convention` | yes | §5 |
| `oral_report` | when told aloud | especially from children |
| parents' and caregivers' names | yes | as given, including "Mama X" as said |
| approximate age or date of birth | yes | a range is fine |
| place of origin as named then; place last seen | yes, minimal | §7 |
| `subject_is_minor`, protected flags | when they apply | §4, §8 |
| ethnicity, clan, tribe, religion | **never** | §1 |

## Sources

The language packs (`namebridge/data/packs/`), with every rule's own source; `DPIA.md` (d); `DATA_RULES.md` DR-1, DR-4; `NAME_CHANGE.md`; DRC Family Code arts 56–67; Rwanda Law 71/2024 arts 36–43; `RESEARCH_LOG.md` entries of 26 Oct–9 Nov 2026.
