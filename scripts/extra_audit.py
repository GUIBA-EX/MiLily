from common import *
import collections
out=p/'release';rr=json.loads((p/'selected.json').read_text());meta={r['accession']:r for r in csv.DictReader((p/'metadata.tsv').open(),delimiter='\t')};audit=[]
for r in rr:
 for side in ['F','R']:
  q=r[side];vs=expand(q)
  assert all(len(set(s[-3:]))>1 and any(c in 'GC' for c in s[-3:]) and 1<=sum(c in 'GC' for c in s[-5:])<=4 and not any(c*5 in s for c in 'ACGT') for s in vs)
  audit.append(dict(name=r['name'],side=side,sequence=q,variants=len(vs),terminal3=q[-3:],last_base_degenerate=len(I[q[-1]])>1,all_variants_pass=True))
write(out/'terminal_audit.csv',audit)
bars=collections.defaultdict(lambda:collections.defaultdict(set))
for r in csv.DictReader((p/'verify/target_barcodes.tsv').open(),delimiter='\t'):bars[r['name']][r['sequence']].add(meta[r['accession']]['organism'])
rows=[];collisions=[]
for r in rr:
 data=bars[r['name']];labels=set().union(*data.values()) if data else set();amb=set().union(*(v for v in data.values() if len(v)>1)) if any(len(v)>1 for v in data.values()) else set()
 rows.append(dict(name=r['name'],amplified_labels=len(labels),unique_barcode_sequences=len(data),labels_without_observed_shared_barcodes=len(labels-amb),observed_label_resolution_pct=100*len(labels-amb)/len(labels) if labels else 0))
 for seq,ls in data.items():
  if len(ls)>1:collisions.append(dict(name=r['name'],labels='; '.join(sorted(ls)),sequence=seq))
write(out/'barcode_resolution.csv',rows)
if collisions:write(out/'barcode_collisions.csv',collisions)
print('Terminal variants and observed barcode collisions audited')
