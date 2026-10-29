"""Independent position-by-position check of unchanged manual XS on the curated panel."""
from pathlib import Path
import csv
p=Path(__file__).resolve().parents[1];seq={}
for l in (p/'inputs/results/species_qc/representatives.fasta').open():
 if l.startswith('>'):key=l[1:].split()[0];seq[key]=''
 else:seq[key]+=l.strip().upper()
I=dict(A='A',C='C',G='G',T='T',D='AGT');f='TTGGGGCAACCDCGAAG';r='CAACATCGAGGTCGCAAAC';rsets=[set(I[x].translate(str.maketrans('ACGT','TGCA'))) for x in r[::-1]];fsets=[set(I[x]) for x in f]
def positions(s,ss,reverse):
 out=[]
 for i in range(len(s)-len(ss)+1):
  t=s[i:i+len(ss)]
  if any(c not in 'ACGT' for c in t):continue
  bad=[j for j,(c,allowed) in enumerate(zip(t,ss)) if c not in allowed]
  if len(bad)<=2:out.append((i,len(bad),any(j<3 if reverse else j>=len(ss)-3 for j in bad)))
 return out
expected={x['accession']:x for x in csv.DictReader((p/'results/new_curated_XS_hits.csv').open())}
for a,x in expected.items():
 covered=exact=False
 for s in [seq[a],seq[a].translate(str.maketrans('ACGT','TGCA'))[::-1]]:
  for fp,fm,fl in positions(s,fsets,False):
   for rp,rm,rl in positions(s,rsets,True):
    if rp-fp-len(f)<20 or not 70<=rp+len(r)-fp<=500:continue
    covered|=not fl and not rl;exact|=fm==rm==0
 assert int(x['le2last3'])==int(covered) and int(x['exact'])==int(exact),a
print('PASS: manual XS unchanged; naive independent paired scan agrees for',len(expected),'curated species')
