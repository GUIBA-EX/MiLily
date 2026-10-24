from common import *
import collections
rev={frozenset(v):k for k,v in I.items() if k!='X'}
seq={r.id.removeprefix('_R_'):str(r.seq).upper() for r in SeqIO.parse(p/'full_aligned.fasta','fasta')};ref=seq[json.loads((p/'config.json').read_text())['reference']];cols=[i for i,b in enumerate(ref) if b!='-'];rows=[];seen=set()
for side in ['F','R']:
 for a in range(101,len(cols)-35,5):
  for L in [18,22,26,30]:
   b=a+L-1;ts=[seq[x['accession']][cols[a-1]:cols[b-1]+1].replace('-','') for x in panel]
   if side=='R':ts=[str(Seq(t).reverse_complement()) for t in ts]
   valid=[i for i,t in enumerate(ts) if len(t)==L and set(t)<=set('ACGT')]
   if sum(w[i] for i in valid)<.65:continue
   freq=collections.Counter();counts=[collections.Counter() for _ in range(L)]
   for i in valid:
    freq[ts[i]]+=w[i]
    for j,c in enumerate(ts[i]):counts[j][c]+=w[i]
   majority=''.join(c.most_common(1)[0][0] for c in counts);qs=[q for q,_ in freq.most_common(3)]+[majority]
   alts=sorted([(v/sum(ct.values()),j,c) for j,ct in enumerate(counts) for c,v in ct.items() if c!=majority[j]],reverse=True)
   for cap in [4,16,32]:
    sets=[set(c) for c in majority]
    for fraction,j,c in alts:
     if fraction<.04:continue
     cand=[v|{c} if k==j else v for k,v in enumerate(sets)]
     if math.prod(map(len,cand))>cap:continue
     q=''.join(rev[frozenset(v)] for v in cand)
     if terminal(q):sets=cand
    qs.append(''.join(rev[frozenset(v)] for v in sets))
   for q in dict.fromkeys(qs):
    if not terminal(q) or (side,a,q) in seen:continue
    seen.add((side,a,q));cv=[];ex=[]
    for t in ts:
     mm=[c not in I[n] for n,c in zip(q,t)] if len(t)==L and set(t)<=set('ACGT') else [True]*L
     cv.append(sum(mm)<=2 and not any(mm[-3:]));ex.append(not any(mm))
    cov=float(w@cv);exact=float(w@ex)
    if cov<.20:continue
    th=oligo_thermal(q)
    if any(t[2]>=55 or t[0]<45 or t[1]>75 for t in th):continue
    rows.append(dict(id=f'O{len(rows):05}',side=side,sequence=q,start=a,end=b,degeneracy=deg(q),cv=cv,ex=ex,coverage=cov,exact=exact))
 print(side,len(rows),flush=True)
(p/'all_oligos.json').write_text(json.dumps(rows))
# Bounded spatial shortlist: retain up to 3 per 25-bp bin, direction and chemistry.
groups=collections.defaultdict(list)
for r in rows:groups[r['side'],r['start']//25,r['degeneracy']>1].append(r)
keep=[]
for g in groups.values():keep+=sorted(g,key=lambda r:(-r['coverage']-r['exact'],-r['coverage'],r['degeneracy']))[:3]
(p/'oligos.json').write_text(json.dumps(keep));d=p/'sites';d.mkdir(exist_ok=True);(d/'oligos.tsv').write_text(''.join(f"{r['id']} {r['side']} {r['sequence']}\n" for r in keep));print('Shortlist',len(keep),flush=True)
