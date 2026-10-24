from pathlib import Path
import csv,json,re,hashlib,itertools,math,zipfile,collections
p=Path(__file__).resolve().parents[1]
def rows(f):return list(csv.DictReader((p/f).open()))
I=dict(A='A',C='C',G='G',T='T',R='AG',Y='CT',S='CG',W='AT',K='GT',M='AC',B='CGT',D='AGT',H='ACT',V='ACG',N='ACGT')
a=rows('sequences/primer_pairs.csv');assert len(a)==16 and len({x['scheme'] for x in a})==12
fa={};key=None
for line in (p/'sequences/primers.fasta').read_text().splitlines():
 if line.startswith('>'):key=line[1:];fa[key]=''
 else:fa[key]+=line
assert len(fa)==32
for r in a:
 for side in ['F','R']:
  q=r[side];assert fa[f"MiLily-{r['name']}_{side}"]==q;assert math.prod(len(I[c]) for c in q)==int(r['degeneracy_'+side])
  for s in map(''.join,itertools.product(*(I[c] for c in q))):assert len(set(s[-3:]))>1 and any(c in 'GC' for c in s[-3:]) and 1<=sum(c in 'GC' for c in s[-5:])<=4 and not any(c*5 in s for c in 'ACGT')
for r in rows('results/thermal.csv'):
 assert float(r['structure_max'])<55
 assert abs((float(r['F_tm_min'])+float(r['F_tm_max'])-float(r['R_tm_min'])-float(r['R_tm_max']))/2)<=5
v=json.loads((p/'results/verification.json').read_text());assert v['checks']==864 and v['disagreements']==0 and v['background_checks']==32 and v['background_disagreements']==0
hits=collections.defaultdict(set)
for r in csv.DictReader((p/'results/independent_hits.tsv').open(),delimiter='\t'):
 for k in ['exact','le2last3','le2','le3','le4']:
  if r[k]=='1':hits[r['name'],r['role'],r['model'],k].add(r['accession'])
panel=rows('references/panel.csv')
for r in rows('results/comparison.csv'):
 names=[x['name'] for x in a if x['scheme']==r['scheme']]
 def union(role,model,k):return set().union(*(hits[n,role,model,k] for n in names))
 for col,k in [('coverage_pct','le2last3'),('exact_pct','exact')]:assert abs(float(r[col])-100*sum(float(x['weight']) for x in panel if x['accession'] in union('target','WC',k)))<1e-8
 for col,m,k in [('WC3','WC','le3'),('GT2','GT','le2'),('WC4','WC','le4')]:assert int(r[col])==len(union('background',m,k))
for r in rows('results/binding_positions.csv'):
 for side in ['F','R']:assert int(r[side+'_end'])-int(r[side+'_start'])+1==len(r[side+'_sequence'])
 assert int(r['reference_span_bp'])==int(r['R_end'])-int(r['F_start'])+1
coords={r['name']:r for r in rows('results/binding_positions.csv')}
for reg in ['S','M','L','XL']:
 arow,brow=coords[reg+'A'],coords[reg+'B']
 assert all(arow[side+'_'+k]==brow[side+'_'+k] for side in ['F','R'] for k in ['start','end']),reg
 assert (arow['F_sequence'],arow['R_sequence'])!=(brow['F_sequence'],brow['R_sequence']),reg
for f in list(p.rglob('*.md'))+list(p.rglob('*.html')):
 links=re.findall(r'\]\(([^)]+)\)',f.read_text()) if f.suffix=='.md' else re.findall(r'(?:href|src)="([^"]+)"',f.read_text())
 for link in links:
  if '://' in link or link.startswith('#'):continue
  assert (f.parent/link.split('#')[0]).exists(),(f,link)
with zipfile.ZipFile(p/'reproduction_sources.zip') as z:assert z.testzip() is None
for n,h in json.loads((p/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((p/n).read_bytes()).hexdigest()==h,n
print('PASS: 12 portfolios, 16 pairs, 32 oligos; all terminal variants, thermal scenarios, raw-hit metrics, coordinates, links, bundle and hashes')
