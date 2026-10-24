from common import *
import collections
rr=json.loads((p/'selected.json').read_text());out=p/'release';out.mkdir(exist_ok=True);h=collections.defaultdict(set);sizes=collections.defaultdict(list)
rawseq={r.id:str(r.seq).upper() for r in SeqIO.parse(p/'target.fasta','fasta')}
meta={r['accession']:r for r in csv.DictReader((p/'metadata.tsv').open(),delimiter='\t')}
for r in csv.DictReader((p/'verify/independent_hits.tsv').open(),delimiter='\t'):
 for k in ['exact','le2last3','le2','le3','le4']:
  if r[k]=='1':h[r['name'],r['role'],r['model'],k].add(r['accession'])
 if r['role']=='target' and r['sizes']:sizes[r['name']]+=[int(x) for x in r['sizes'].split(',')]
ol={r['id']:r for r in json.loads((p/'oligos.json').read_text())};al={r.id.removeprefix('_R_'):str(r.seq).upper() for r in SeqIO.parse(p/'target_aligned.fasta','fasta')};ref=json.loads((p/'config.json').read_text())['reference'];cols=[i for i,c in enumerate(al[ref]) if c!='-']
comp=[];miss=[];checks=[];bgchecks=[];detail=[];bgrows=[]
for scheme in dict.fromkeys(x['scheme'] for x in rr):
 pp=[x for x in rr if x['scheme']==scheme];names=[x['name'] for x in pp]
 def union(role,model,k):return set().union(*(h[n,role,model,k] for n in names))
 cv=union('target','WC','le2last3');ex=union('target','WC','exact');cvv=[a['accession'] in cv for a in panel];exv=[a['accession'] in ex for a in panel];sz=sum([sizes[n] for n in names],[])
 eligible=set()
 for acc,s in al.items():
  for pair in pp:
   f,r=ol[pair['F_id']],ol[pair['R_id']];left=cols[f['start']-1];right=cols[r['end']-1]
   present=[i for i,c in enumerate(s) if c!='-']
   if present and min(present)<=left and max(present)>=right:eligible.add(acc)
 eligible|=cv|ex
 labels=collections.defaultdict(list)
 seen=set()
 for acc in sorted(eligible):
  key=(meta[acc]['organism'],rawseq[acc])
  if key not in seen:labels[key[0]].append(acc);seen.add(key)
 def rate(hits):return 100*np.mean([np.mean([a in hits for a in aa]) for aa in labels.values()]) if labels else 0
 row=dict(scheme=scheme,region=pp[0]['region'],chemistry=pp[0]['chemistry'],pairs=len(pp),coverage_pct=100*float(w@cvv),exact_pct=100*float(w@exv),evaluable_records=len(eligible),evaluable_labels=len(labels),evaluable_coverage_pct=rate(cv),evaluable_exact_pct=rate(ex),WC3=len(union('background','WC','le3')),GT2=len(union('background','GT','le2')),WC4=len(union('background','WC','le4')),product_min=min(sz) if sz else '',product_max=max(sz) if sz else '')
 assert row['WC3']<=5 and row['GT2']<=5
 comp.append(row)
 for x in panel:
  if x['accession'] not in cv:miss.append(dict(scheme=scheme,**x))
 for acc in al:detail.append(dict(scheme=scheme,accession=acc,label=meta[acc]['organism'],evaluable=acc in eligible,covered=acc in cv,exact=acc in ex))
 for model,k in [('WC','le3'),('GT','le2'),('WC','le4')]:
  for acc in sorted(union('background',model,k)):bgrows.append(dict(scheme=scheme,model=model,threshold=k,**meta[acc]))
for x in rr:
 for mode,flag in [('cv','le2last3'),('ex','exact')]:
  for i,a in enumerate(panel):checks.append(dict(name=x['name'],mode=mode,accession=a['accession'],prediction=x[mode][i],full_scan=a['accession'] in h[x['name'],'target','WC',flag]))
 for model,col,flag in [('WC','WC3','le3'),('GT','GT2','le2')]:bgchecks.append(dict(name=x['name'],model=model,agree=set(x[col])==h[x['name'],'background',model,flag]))
for name,data in [('comparison.csv',comp),('primer_pairs.csv',[{k:x[k] for k in ['scheme','region','chemistry','name','F','R','degeneracy_F','degeneracy_R','reference_span']} for x in rr]),('missed_references.csv',miss),('thermal.csv',[dict(name=x['name'],**t) for x in rr for t in x['thermal']]),('target_evaluation.csv',detail),('background_hits.csv',bgrows)]:
 if data:write(out/name,data)
(out/'primers.fasta').write_text(''.join(f">MiLily-{x['name']}_{side}\n{x[side]}\n" for x in rr for side in ['F','R']))
bad=[x for x in checks if x['prediction']!=x['full_scan']];bb=[x for x in bgchecks if not x['agree']];(out/'verification.json').write_text(json.dumps(dict(checks=len(checks),disagreements=len(bad),details=bad,background_checks=len(bgchecks),background_disagreements=len(bb),background_details=bb),indent=2));print(json.dumps(comp,indent=2));print('disagreements',len(bad),len(bb));assert not bb
