from pathlib import Path
import json,csv,subprocess
p=Path(__file__).resolve().parent;root=p.parents[1];pool=json.loads((p/'oligos.json').read_text());wanted={(r['side'],r['sequence']):r['id'] for r in pool};sites=p/'sites';sites.mkdir(exist_ok=True)
bg=p/'background.fasta'
if not bg.exists():bg.symlink_to(root/'work/milily/background.fasta')
oldp=root/'work/lily_urchin_occam/MiLily';old=json.loads((oldp/'oligos.json').read_text());mapping={r['id']:wanted[r['side'],r['sequence']] for r in old if (r['side'],r['sequence']) in wanted};seen=set(mapping.values())
with (p/'reused_background_sites.tsv').open('w') as f:
 for row in csv.reader((oldp/'sites/background_sites.tsv').open(),delimiter='\t'):
  if row[0] in mapping:row[0]=mapping[row[0]];f.write('\t'.join(row)+'\n')
new=[r for r in pool if r['id'] not in seen];(sites/'oligos.tsv').write_text(''.join(f"{r['id']} {r['side']} {r['sequence']}\n" for r in new));print('reuse',len(seen),'new',len(new),flush=True)
subprocess.run([str(root/'work/micucumber_taxon_optimization/scan_sites'),str(sites)],check=True)
