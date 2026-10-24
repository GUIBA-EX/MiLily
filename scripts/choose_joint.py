from common import *
from collections import defaultdict
feasible=json.loads((p/'feasible.json').read_text());ol={r['id']:r for r in json.loads((p/'oligos.json').read_text())}
def locus(r):return tuple(ol[r[s+'_id']][k] for s in ['F','R'] for k in ['start','end'])
def metrics(pp):
 wc=set().union(*(set(x['WC3']) for x in pp));gt=set().union(*(set(x['GT2']) for x in pp))
 if len(wc)>5 or len(gt)>5:return None
 c=float(w@np.logical_or.reduce([x['cv'] for x in pp]));e=float(w@np.logical_or.reduce([x['ex'] for x in pp]))
 return (round(c+e,12),round(c,12),round(e,12),-sum(x['degeneracy_F']+x['degeneracy_R'] for x in pp),-len(wc)-len(gt))
selected=[];audit=[];joint=[]
for reg in ['S','M','L','XL']:
 groups=defaultdict(dict)
 for r in feasible:
  if r['region']==reg:groups[locus(r)].setdefault((r['F'],r['R']),r)
 groups={k:list(v.values()) for k,v in groups.items()};rejected=set();thermal_rejections=0
 while True:
  options=[]
  for loc,g in groups.items():
   g=[r for r in g if (r['F'],r['R']) not in rejected];ordinary=[r for r in g if r['degeneracy_F']*r['degeneracy_R']==1];degen=[r for r in g if r['degeneracy_F']*r['degeneracy_R']>1]
   if len(ordinary)<2 or not degen:continue
   one=max(ordinary,key=lambda r:metrics([r]));d=max(degen,key=lambda r:metrics([r]));ab=None;best=None
   for pp in itertools.combinations(ordinary,2):
    score=metrics(pp)
    if score is not None and (best is None or score>best):ab=pp;best=score
   if ab is None:continue
   m=[metrics([d]),metrics([one]),best]
   # Equal weight for degenerate single, ordinary single and ordinary A/B performance.
   score=(round(sum(x[0] for x in m)/3,12),round(sum(x[1] for x in m)/3,12),round(sum(x[2] for x in m)/3,12),sum(x[3] for x in m),sum(x[4] for x in m))
   options.append((score,loc,d,one,ab,m))
  if not options:raise RuntimeError((reg,'no common locus supports D, ordinary and two distinct ordinary variants'))
  options.sort(key=lambda x:x[0],reverse=True);score,loc,d,one,ab,m=options[0];bad=[r for r in [d,one,*ab] if not thermal(r['F'],r['R'])[0]]
  if not bad:break
  rejected.update((r['F'],r['R']) for r in bad);thermal_rejections+=len(bad)
 for chem,pp,ms in [('degenerate',[d],m[0]),('ordinary',[one],m[1]),('ordinary',ab,m[2])]:
  count=len(pp);scheme=reg+'D' if chem=='degenerate' else reg if count==1 else reg+'A+'+reg+'B'
  for i,r in enumerate(pp):selected.append(dict(r,scheme=scheme,name=reg+'D' if chem=='degenerate' else reg if count==1 else reg+chr(65+i),chemistry=chem,option=count,union_coverage=ms[1],union_exact=ms[2],thermal=thermal(r['F'],r['R'])[1]))
  audit.append(dict(scheme=scheme,eligible=len(groups[loc]),thermal_rejections=thermal_rejections,coverage=ms[1],exact=ms[2],common_locus=loc));print(audit[-1],flush=True)
 joint.append(dict(region=reg,F_start=loc[0],F_end=loc[1],R_start=loc[2],R_end=loc[3],reference_span_bp=loc[3]-loc[0]+1,eligible_loci=len(options),joint_score=score[0]))
(p/'selected.json').write_text(json.dumps(selected,indent=2));(p/'audit.json').write_text(json.dumps(audit,indent=2));write(p/'joint_locus.csv',joint);print('DONE',flush=True)
