from common import *
import html
rr=json.loads((p/'selected.json').read_text());ol={r['id']:r for r in json.loads((p/'oligos.json').read_text())};out=p/'release';out.mkdir(exist_ok=True)
al={r.id.removeprefix('_R_'):str(r.seq).upper() for r in SeqIO.parse(p/'full_aligned.fasta','fasta')};refid=json.loads((p/'config.json').read_text())['reference'];ref=al[refid];cols=[i for i,c in enumerate(ref) if c!='-'];positions=[];colors=dict(S='#13aaba',M='#e59b19',L='#2779ef',XL='#922bde')
def txt(x,y,s,size=14,fill='#173647',extra=''):return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" {extra}>{html.escape(str(s))}</text>'
def svg(w,h):return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" rx="20" fill="#f7fbff"/><g font-family="Arial,sans-serif">']
links=[]
for r in rr:
 es=svg(1550,1520);es+=[txt(28,38,f"MiLily {r['name']} | Primer–template bases",26),txt(28,65,'Blue: IUPAC-compatible · Orange: mismatch · Grey: gap/unknown · Box: terminal 3 nt · Primer-oriented 5′ → 3′',16)]
 pos=dict(name=r['name'],region=r['region'],reference=refid)
 for side_idx,side in enumerate(['F','R']):
  o=ol[r[side+'_id']];q=r[side];a,b=o['start'],o['end'];pos.update({side+'_start':a,side+'_end':b,side+'_sequence':q});y0=110+side_idx*700
  es.append(txt(28,y0,f"{side}  |  {a}–{b}  |  degeneracy {deg(q)}",19))
  records=[('Primer',q)]
  for x in panel:
   t=al[x['accession']][cols[a-1]:cols[b-1]+1].replace('-','')
   if side=='R':t=str(Seq(t).reverse_complement())
   if len(t)!=len(q):t='?'*len(q)
   records.append((x['label']+' / '+x['accession'],t))
  for i,(label,t) in enumerate(records):
   yy=y0+18+i*23;es.append(txt(28,yy+16,label,13))
   for j,c in enumerate(t):
    col='#d6edf4' if c in I.get(q[j],'') or i==0 else '#e3e8ee' if c not in 'ACGT' else '#ffd5a1';xx=570+j*25
    es.append(f'<rect x="{xx}" y="{yy}" width="24" height="22" fill="{col}"/>');es.append(txt(xx+12,yy+16,c,15,extra='text-anchor="middle" font-family="monospace"'))
  es.append(f'<rect x="{570+(len(q)-3)*25-1}" y="{y0+17}" width="76" height="{len(records)*23}" fill="none" stroke="#173647" stroke-width="2"/>')
 pos['reference_span_bp']=pos['R_end']-pos['F_start']+1;positions.append(pos);es.append('</g></svg>');name=f"base_matching_{r['name']}.svg";(out/name).write_text(''.join(es));links.append(f'<h2>{r["name"]}</h2><img src="{name}" style="width:100%;max-width:1550px">')
write(out/'binding_positions.csv',positions)
H=180+len(rr)*65;es=svg(1500,H);es.extend([txt(30,38,'MiLily | Current binding positions',27),txt(30,68,f'{refid} · Extracted 16S rRNA · 1-based, ungapped · Shared linear axis',17)]);x=lambda v:150+v/len(cols)*1250
for tick in range(0,len(cols)+1,100):
 xx=x(tick);es.append(f'<path d="M{xx},105 V{H-55}" stroke="#dce8ef"/>');es.append(txt(xx,98,tick,12))
for i,r in enumerate(positions):
 y=132+i*65;c=colors[r['region']];a,b,u,v=[x(r[k]) for k in ['F_start','F_end','R_start','R_end']];es.append(txt(30,y+5,r['name'],20,c));es.append(f'<path d="M{a},{y} H{v}" stroke="{c}" stroke-opacity=".4" stroke-width="4"/><path d="M{a},{y} H{b} l-6,-5 m6,5 l-6,5 M{v},{y} H{u} l6,-5 m-6,5 l6,5" stroke="{c}" stroke-width="5" fill="none"/>');es.extend([txt((a+v)/2,y-12,str(r['reference_span_bp'])+' bp',14,c),txt(a,y+23,f"F {r['F_start']}–{r['F_end']}",12),txt(v,y+38,f"R {r['R_start']}–{r['R_end']}",12,extra='text-anchor="end"')])
es.extend([txt(30,H-15,'Spans include primers; product lengths vary among taxa. Arrowheads indicate 3′ ends.',14),'</g></svg>']);(out/'binding_positions.svg').write_text(''.join(es))
(out/'base_matching.html').write_text('<!doctype html><meta charset="utf-8"><title>MiLily base matching</title><body style="font-family:Arial;background:#f4f8fc;margin:30px"><h1>MiLily · 碱基匹配 / Base matching</h1><p>27 complete-sequence haplotypes; 25 labels. Question marks indicate unequal-length windows, not inferred mismatches. / 问号为长度不一致窗口，不计作已知错配。</p>'+''.join(links))
print('Figures generated')
