from common import *
import collections
rows=json.loads((p/'oligos.json').read_text());ol={r['id']:r for r in rows};sites=collections.defaultdict(lambda:collections.defaultdict(list))
canonical={};alias={}
for r in rows:alias[r['id']]=canonical.setdefault((r['side'],r['sequence']),r['id'])
for name,acc,ori,gt,pos,mm,last in csv.reader((p/'sites/background_sites.tsv').open(),delimiter='\t'):
 if name!=alias[name] or (gt=='0' and int(mm)>3):continue
 sites[name,int(gt)][acc,ori].append((int(pos),int(mm)))
print('sites loaded',flush=True)
def bg(f,r,gt,limit):
 a=sites[alias[f['id']],gt];b=sites[alias[r['id']],gt];found=set()
 for key in a.keys()&b.keys():
  if any(fm<=limit and rm<=limit and 0<=rp-fp-len(f['sequence'])<=1000 for fp,fm in a[key] for rp,rm in b[key]):found.add(key[0])
  if len(found)>5:break
 return sorted(found)
feasible=[]
for reg,lo,hi in [('S',150,224),('M',225,284),('L',285,359),('XL',360,450)]:
 fs=[r for r in rows if r['side']=='F'];rs=[r for r in rows if r['side']=='R'];tested=0
 for f,r in itertools.product(fs,rs):
  span=r['end']-f['start']+1
  if not lo<=span<=hi or r['start']<=f['end']:continue
  ft,rt=oligo_thermal(f['sequence']),oligo_thermal(r['sequence'])
  if any(abs((a[0]+a[1]-b[0]-b[1])/2)>5 for a,b in zip(ft,rt)):continue
  cv=(np.array(f['cv'])&r['cv']).tolist();ex=(np.array(f['ex'])&r['ex']).tolist();cov=float(w@cv);exact=float(w@ex)
  if cov<.1:continue
  tested+=1;a=bg(f,r,0,3)
  if len(a)>5:continue
  b=bg(f,r,1,2)
  if len(b)>5:continue
  feasible.append(dict(region=reg,F=f['sequence'],R=r['sequence'],F_id=f['id'],R_id=r['id'],degeneracy_F=f['degeneracy'],degeneracy_R=r['degeneracy'],cv=cv,ex=ex,coverage=cov,exact=exact,WC3=a,GT2=b,reference_span=span))
 print(reg,'tested',tested,'eligible',sum(x['region']==reg for x in feasible),flush=True)
(p/'feasible.json').write_text(json.dumps(feasible))
selected=[];audit=[]
for reg in ['S','M','L','XL']:
 for chem,count in [('degenerate',1),('ordinary',1),('ordinary',2)]:
  pool=[r for r in feasible if r['region']==reg and (r['degeneracy_F']*r['degeneracy_R']>1)==(chem=='degenerate')]
  # Include a terminal/thermal signature in state reduction, so a failing representative does not hide alternatives.
  dedup={}
  for r in pool:
   key=(tuple(r['cv']),tuple(r['ex']),tuple(r['WC3']),tuple(r['GT2']),r['F'],r['R'])
   dedup.setdefault(key,r)
  pool=list(dedup.values());rejections=0
  if len(pool)<count:
   audit.append(dict(scheme=reg,chemistry=chem,pairs=count,status='no eligible candidates'));continue
  while True:
   if not pool:raise RuntimeError((reg,chem,count,'no thermally eligible candidates'))
   best=None;chosen=None
   def combos():
    if count==1:
     yield from itertools.combinations(pool,1);return
    cm=np.array([r['cv'] for r in pool]);em=np.array([r['ex'] for r in pool])
    for i in range(len(pool)-1):
     score=(cm[i+1:]|cm[i])@w+(em[i+1:]|em[i])@w
     for j in np.flatnonzero(score>=(-1 if best is None else best[0]-1e-10)):yield pool[i],pool[i+1+int(j)]
   for pp in combos():
    if len(pp)==2 and (abs(ol[pp[0]['F_id']]['start']-ol[pp[1]['F_id']]['start'])>35 or abs(ol[pp[0]['R_id']]['start']-ol[pp[1]['R_id']]['start'])>35):continue
    a=set().union(*(set(x['WC3']) for x in pp));b=set().union(*(set(x['GT2']) for x in pp))
    if len(a)>5 or len(b)>5:continue
    c=float(w@np.logical_or.reduce([x['cv'] for x in pp]));e=float(w@np.logical_or.reduce([x['ex'] for x in pp]));score=(round(c+e,12),round(c,12),round(e,12),-sum(x['degeneracy_F']+x['degeneracy_R'] for x in pp),-len(a)-len(b))
    if best is None or score>best:best=score;chosen=pp
   if chosen is None:raise RuntimeError((reg,chem,count,'no portfolio'))
   bad=[r for r in chosen if not thermal(r['F'],r['R'])[0]]
   if not bad:break
   rejections+=len(bad);pool=[r for r in pool if all((r['F'],r['R'])!=(b['F'],b['R']) for b in bad)]
  scheme=reg+'D' if chem=='degenerate' else reg if count==1 else reg+'A+'+reg+'B'
  for i,r in enumerate(chosen):selected.append(dict(r,scheme=scheme,name=reg+'D' if chem=='degenerate' else reg if count==1 else reg+chr(65+i),chemistry=chem,option=count,union_coverage=best[1],union_exact=best[2],thermal=thermal(r['F'],r['R'])[1]))
  audit.append(dict(scheme=scheme,eligible=len(pool),thermal_rejections=rejections,coverage=best[1],exact=best[2]));print(audit[-1],flush=True)
(p/'selected.json').write_text(json.dumps(selected,indent=2));(p/'audit.json').write_text(json.dumps(audit,indent=2));print('DONE',flush=True)
