"""Reproduce the fixed XS assay from frozen local references; no network access."""
from pathlib import Path
import argparse,csv,json,subprocess,collections,shutil
PROJECT=Path(__file__).resolve().parents[1]
F='TTGGGGCAACCDCGAAG';R='CAACATCGAGGTCGCAAAC'
I={k:set(v) for k,v in dict(A='A',C='C',G='G',T='T',D='AGT').items()};C=dict(zip('ACGT','TGCA'))
def fasta(path):
 key=None;s=[]
 for l in path.open():
  if l.startswith('>'):
   if key is not None:yield key,''.join(s)
   key=l[1:].split()[0];s=[]
  else:s.append(l.strip().upper())
 if key is not None:yield key,''.join(s)
def rc(s):return s.translate(str.maketrans('ACGT','TGCA'))[::-1]
def masks(q,gt,reverse=False):
 sets=[set(I[c]) for c in q]
 if gt:
  for x in sets:
   old=set(x)
   if 'G' in old:x.add('A')
   if 'T' in old:x.add('C')
 if reverse:sets=[{C[c] for c in x} for x in sets[::-1]]
 return {c:sum(1<<j for j,x in enumerate(sets) if c in x) for c in 'ACGT'}
def scan(s,q,mask,k):
 state=[0]*(k+1);end=1<<(len(q)-1);hits=[]
 for j,c in enumerate(s):
  if c not in mask:state=[0]*(k+1);continue
  old=state;v=mask[c];state=[((old[0]<<1)|1)&v]+[(((old[e]<<1)|1)&v)|((old[e-1]<<1)|1) for e in range(1,k+1)]
  if j+1>=len(q) and state[k]&end:hits.append((j-len(q)+1,next(e for e in range(k+1) if state[e]&end)))
 return hits
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--references',type=Path,default=PROJECT/'references');ap.add_argument('--expected',type=Path,default=PROJECT/'results/xs/assessment.json');ap.add_argument('--scanner-source',type=Path,default=Path(__file__).with_name('xs_independent_scan.cpp'));args=ap.parse_args();out=args.output.resolve();out.mkdir(parents=True,exist_ok=True)
 for role in ['target','background']:shutil.copyfile(args.references/(role+'.fasta'),out/(role+'.fasta'))
 (out/'independent_primers.tsv').write_text(f'XS\t{F}\t{R}\n');exe=out/'independent_scan';subprocess.run(['c++','-O3','-std=c++17',str(args.scanner_source),'-o',str(exe)],check=True);subprocess.run([str(exe),str(out)],check=True)
 h=collections.defaultdict(set)
 for x in csv.DictReader((out/'independent_hits.tsv').open(),delimiter='\t'):
  for k in ['exact','le2last3','le2','le3','le4']:
   if x[k]=='1':h[x['role'],x['model'],k].add(x['accession'])
 panel=list(csv.DictReader((args.references/'panel.csv').open()));total=sum(float(x['weight']) for x in panel)
 metrics={k:100*sum(float(x['weight']) for x in panel if x['accession'] in h['target','WC',flag])/total for k,flag in [('coverage_pct','le2last3'),('exact_pct','exact')]}
 for key,model,flag in [('background_WC3','WC','le3'),('background_GT2','GT','le2'),('strict_background_WC2_last3','WC','le2last3'),('exact_background_WC0','WC','exact')]:metrics[key]=len(h['background',model,flag])
 expected=json.loads(args.expected.read_text())
 for k,v in metrics.items():assert abs(v-expected[k])<1e-8,(k,v,expected[k])
 # Independent local aligned-window predictions of the 27 target records.
 al={a.removeprefix('_R_'):s for a,s in fasta(args.references/'full_aligned.fasta')};cols=[j for j,c in enumerate(al['AF049132.1']) if c!='-'];checks=0
 for x in panel:
  cv=[];ex=[]
  for q,a,b,reverse in [(F,1122,1138,False),(R,1282,1300,True)]:
   s=al[x['accession']][cols[a-6]:cols[b+4]+1].replace('-','');s=rc(s) if reverse else s;states=[]
   for j in range(len(s)-len(q)+1):
    t=s[j:j+len(q)]
    if set(t)<=set('ACGT'):
     mm=[c not in I[n] for n,c in zip(q,t)];states.append((sum(mm),any(mm[-3:])))
   cv.append(any(n<=2 and not last for n,last in states));ex.append(any(n==0 for n,last in states))
  for v,flag in [(all(cv),'le2last3'),(all(ex),'exact')]:assert v==(x['accession'] in h['target','WC',flag]),(x['accession'],flag);checks+=1
 # An independent bit-parallel Hamming scanner reproduces paired background sets.
 actual={m:set() for m in ['WC','GT']};params={m:(masks(F,m=='GT'),masks(R,m=='GT',True),3 if m=='WC' else 2) for m in actual}
 for acc,s in fasta(args.references/'background.fasta'):
  for m,(fm,rm,k) in params.items():
   for t in [s,rc(s)]:
    ff=scan(t,F,fm,k);rr=scan(t,R,rm,k)
    if any(0<=rp-fp-len(F)<=1000 for fp,_ in ff for rp,_ in rr):actual[m].add(acc);break
 for m in actual:assert actual[m]==h['background',m,'le3' if m=='WC' else 'le2'],m
 result=dict(name='XS',metrics=metrics,target_checks=checks,target_disagreements=0,background_checks=2,background_disagreements=0);(out/'verification.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
if __name__=='__main__':main()
