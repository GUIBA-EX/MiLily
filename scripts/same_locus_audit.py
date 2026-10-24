from common import *
import collections
rr=json.loads((p/'selected.json').read_text());ol={r['id']:r for r in json.loads((p/'oligos.json').read_text())};out=p/'release';out.mkdir(exist_ok=True);rows=[]
for reg in ['S','M','L','XL']:
 pp=[r for r in rr if r['scheme']==reg+'A+'+reg+'B'];assert len(pp)==2
 a,b=pp
 row=dict(region=reg,A=a['name'],B=b['name'])
 for side in ['F','R']:
  x,y=ol[a[side+'_id']],ol[b[side+'_id']]
  assert (x['start'],x['end'])==(y['start'],y['end'])
  row.update({side+'_start':x['start'],side+'_end':x['end'],side+'_A':a[side],side+'_B':b[side],side+'_substitutions':sum(c!=d for c,d in zip(a[side],b[side]))})
 assert row['F_substitutions']+row['R_substitutions']>0
 row['reference_span_bp']=row['R_end']-row['F_start']+1;row['same_locus']=True;rows.append(row)
fixed=json.loads((p/'fixed_single_pairs.json').read_text())
for old in fixed:
 new=next(r for r in rr if r['name']==old['name']);assert (new['F'],new['R'])==(old['F'],old['R'])
write(out/'same_locus_audit.csv',rows);print('PASS: four A/B portfolios have identical F/R coordinate intervals; 8 single-pair schemes unchanged')
