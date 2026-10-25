"""Validate current D assays against independently verified raw-sequence evidence."""
from pathlib import Path
import csv,json,collections,math,re
p=Path(__file__).resolve().parents[1];d=p/'results/D_optimization'
def read(f,sep=','):return list(csv.DictReader(f.open(),delimiter=sep))
chosen=json.loads((d/'selected_D.json').read_text());verified={r['name']:r for r in read(d/'verified_comparison.csv')};seq={r['name']:r for r in read(p/'sequences/primer_pairs.csv')};coords={r['name']:r for r in read(p/'results/binding_positions.csv')};panel=read(d/'panel.csv');orders={r['order'] for r in panel};assert len(orders)==4 and len(panel)==27
h=collections.defaultdict(set)
for r in read(p/'results/independent_hits.tsv','\t'):
 for flag in ['exact','le2last3','le2','le3','le4']:
  if r[flag]=='1':h[r['name'],r['role'],r['model'],flag].add(r['accession'])
macro={r['scheme']:r for r in read(p/'results/taxonomic_comparison.csv')}
for x in chosen:
 n=x['name'];r=verified[x['source_candidate']];b=verified[n+'-before'];q=seq[n]
 for k in ['F','R','degeneracy_F','degeneracy_R']:assert str(q[k])==str(r[k])==str(x[k]),(n,k)
 for k in ['F_start','F_end','R_start','R_end']:assert len({coords[x['region']+suffix][k] for suffix in ['', 'A','B','D']})==1
 for mode,flag in [('coverage','le2last3'),('exact','exact')]:
  obs=[]
  for o in orders:
   labels={z['label'] for z in panel if z['order']==o};hit={z['label'] for z in panel if z['order']==o and z['accession'] in h[n,'target','WC',flag]};obs.append(len(hit)/len(labels))
  score=100*sum(obs)/len(obs);assert math.isclose(score,float(r['order_'+mode+'_pct']),abs_tol=1e-8);assert math.isclose(score,float(macro[n]['order_'+mode+'_pct']),abs_tol=1e-8)
 assert float(r['order_exact_pct'])>=float(b['order_exact_pct'])-1e-8
 assert float(r['taxon_exact_pct'])>=float(b['taxon_exact_pct'])-1e-8
 assert float(r['taxon_coverage_pct'])>=float(b['taxon_coverage_pct'])-4.000001
 for col,model,flag in [('WC3','WC','le3'),('GT2','GT','le2'),('strict_WC','WC','le2last3'),('strict_GT','GT','le2last3')]:assert len(h[n,'background',model,flag])==int(r[col])
 assert max(int(r[k]) for k in ['WC3','GT2'])<=100 and max(int(r[k]) for k in ['strict_WC','strict_GT'])<=20
 for t in x['thermal']:assert t['structure_max']<55 and abs((t['F_tm_min']+t['F_tm_max']-t['R_tm_min']-t['R_tm_max'])/2)<=5
 for fn in ['README.md','README.zh-CN.md']:
  s=(p/fn).read_text();assert f"| {n} | `{q['F']}` | `{q['R']}` |" in s
  line=next(a for a in s.splitlines() if a.startswith('| '+n+' |'));assert f"{float(r['order_coverage_pct']):.2f}" in line and f"{float(r['order_exact_pct']):.2f}" in line
v=json.loads((d/'verification.json').read_text());assert v['target_checks']==486 and v['background_set_checks']==36 and v['disagreements']==0 and v['background_disagreements']==0
print('PASS: four D assays, shared coordinates, order metrics, label safeguards, background counts, thermal gates and bilingual sequences; 486 independent target checks / 36 background sets')
