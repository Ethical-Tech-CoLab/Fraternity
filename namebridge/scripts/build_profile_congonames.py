"""Build the DRC naming profile from the CongoNames authors' PUBLISHED AGGREGATE tables.

No individual record is read: run it in a folder holding only the aggregate CSVs from
reports/name_analysis/ of https://github.com/bernard-ng/drc-names-corpus, after deleting
the two tables that list full names (normalized_duplicate_names.csv, unusual_names.csv),
as DATA_RULES.md DR-1 requires.

Run: python scripts/build_profile_congonames.py <repo-commit-sha> data/profiles/cd-congonames-2026.1.json
"""
import csv,json,sys,hashlib,os
sha=sys.argv[1]; out=sys.argv[2]
def rows(f): return list(csv.DictReader(open(f+'.csv')))
def num(v):
    for t in (int,float):
        try: return t(v) if t is int else round(t(v),6)
        except ValueError: pass
    return v
first=rows('first_token_frequency'); last=rows('last_token_frequency')
src={"name":"Tshabu Ngandu, B., Cansa Kayembe, A. & Mpyana Mwamba, M. (2026), 'CongoNames Corpus: A Large-Scale Labeled Dataset of Congolese Personal Names', Data 11(7): 169, doi:10.3390/data11070169 (MDPI, CC BY 4.0)",
     "aggregates":f"Published aggregate tables in the authors' repository, reports/name_analysis/*.csv (https://github.com/bernard-ng/drc-names-corpus, commit {sha}); the repository itself declares no licence",
     "underlying_data":"National secondary-school examination result lists (palmarès) 2008-2023, DRC Ministry of Education; 8,053,983 records, 12 provinces"}
files={f:hashlib.sha256(open(f+'.csv','rb').read()).hexdigest()[:16] for f in sorted(x[:-4] for x in os.listdir('.') if x.endswith('.csv'))}
ov=rows('names_overview')[0]; st=rows('name_structure_summary')[0]
profile={
 "profile_id":"cd-congonames-2026.1","version":"0.1.0","origin":"CD",
 "method":"Built only from aggregate tables published by the corpus authors; no individual record was downloaded or read. Two published tables listing full names (normalized_duplicate_names, unusual_names) were deleted unread (DATA_RULES DR-1). Built 9 Nov 2026 by scripts/build_profile_congonames.py",
 "sources":[src],"source_file_checksums_sha256_16":files,"confidence":"high",
 "population_note":"Secondary-school exam candidates (mostly adolescents and young adults), 2008-2023; not representative of older adults, of people who did not reach the exam, or of refugees specifically",
 "structure":{
   "records":int(ov['total_rows']),"unique_full_names":int(ov['unique_names_exact']),
   "singleton_share_of_unique_full_names":round(float(rows('long_tail_overall')[0]['singleton_share']),4),
   "token_count_distribution":{(r['token_count'] or "empty"):int(r['count']) for r in rows('token_count_distribution')},
   "chars":{k:num(st[k]) for k in ('mean_chars','median_chars','p90_chars','p95_chars')},
   "tokens":{k:num(st[k]) for k in ('mean_tokens','median_tokens','p90_tokens','p95_tokens')},
   "morphology_flags":{r['metric']:{"count":int(r['count']),"share":round(float(r['share']),6)} for r in rows('name_morphology_flags')},
   "order_observed":"In the exam lists the first token is mostly a Bantu name (nom) and the last token mostly a Christian/French given name (prénom): order nom, postnom, prénom"},
 "elements":{
   "first_token_top50":[{"element":r['first_token'],"count":int(r['count']),"m":int(r['m']),"f":int(r['f'])} for r in first],
   "last_token_top50":[{"element":r['last_token'],"count":int(r['count']),"m":int(r['m']),"f":int(r['f'])} for r in last]},
 "ngrams":{f:[{"ngram":r['ngram'],"count":int(r['count'])} for r in rows(f)] for f in ('probable_native_ngrams_2','probable_native_ngrams_3','probable_surname_ngrams_2','probable_surname_ngrams_3')},
 "letters":{r['letter']:int(r['count']) for r in rows('letter_frequency_full_name')},
 "by_province":[{k:num(v) for k,v in r.items()} for r in rows('names_by_province')],
 "by_year":[{k:num(v) for k,v in r.items()} for r in rows('names_by_year')],
 "diversity_by_province":[{k:num(v) for k,v in r.items()} for r in rows('diversity_by_province')],
 "variant_pairs_observed":[
   {"forms":["ngoy","ngoyi","ngoie"],"basis":"all three in the first-token top 50 (58,229 / 20,600 / 14,157)","status":"proposed"},
   {"forms":["mwamba","muamba"],"basis":"both in the first-token top 50 (16,052 / 11,265): w written w or u","status":"proposed"}],
 "never":"No ethnicity, clan, tribe or religion pattern; province, sex and year only (BENCHMARK_PROTOCOL.md §2.4; C12)"}
json.dump(profile,open(out,'w'),ensure_ascii=False,indent=2); open(out,'a').write('\n')
print('written; min element count', min(e['count'] for e in profile['elements']['first_token_top50']+profile['elements']['last_token_top50']))
