"""Repeat XS terminal, duplex and internal-structure predictions with Primer3."""
from pathlib import Path
import argparse,json,itertools
import primer3
F='TTGGGGCAACCDCGAAG';R='CAACATCGAGGTCGCAAAC';FS=[F.replace('D',c) for c in 'AGT'];RS=[R];kw=dict(mv_conc=50,dv_conc=1.5,dntp_conc=.6)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();reports=[];structures=[]
 for scenario in ['50_per_variant','200_per_direction']:
  fc=50 if scenario=='50_per_variant' else 200/len(FS);rc=50 if scenario=='50_per_variant' else 200/len(RS)
  ft=[primer3.calc_tm(s,dna_conc=fc,**kw) for s in FS];rt=[primer3.calc_tm(s,dna_conc=rc,**kw) for s in RS];st=[]
  for q,c in [(s,fc) for s in FS]+[(s,rc) for s in RS]:
   st += [primer3.calc_hairpin(q,dna_conc=c,**kw).tm,primer3.calc_homodimer(q,dna_conc=c,**kw).tm]
   if scenario=='50_per_variant':
    for t in [37,57,60]:structures.append(dict(sequence=q,temp_C=t,**primer3.calc_hairpin(q,dna_conc=c,temp_c=t,output_structure=True,**kw).todict()))
  for seqs,c in [(FS,fc),(RS,rc)]:
   for x,y in itertools.combinations(seqs,2):st.append(primer3.calc_heterodimer(x,y,dna_conc=c,**kw).tm)
  for x,y in itertools.product(FS,RS):st.append(primer3.calc_heterodimer(x,y,dna_conc=max(fc,rc),**kw).tm)
  reports.append(dict(scenario=scenario,F_tm_min=min(ft),F_tm_max=max(ft),R_tm_min=min(rt),R_tm_max=max(rt),structure_max=max(st)))
 result=dict(F=F,R=R,scenarios=reports,hairpins=structures,thermal_gate_pass=all(x['structure_max']<55 and abs((x['F_tm_min']+x['F_tm_max']-x['R_tm_min']-x['R_tm_max'])/2)<=5 for x in reports));a.output.write_text(json.dumps(result,indent=2));print(json.dumps(reports,indent=2))
if __name__=='__main__':main()
