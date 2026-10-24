from common import *
import subprocess
rr=json.loads((p/'selected.json').read_text());v=p/'verify';v.mkdir(exist_ok=True)
for role in ['target','background']:
 f=v/(role+'.fasta')
 if not f.exists():f.symlink_to((p/(role+'.fasta')).resolve())
(v/'independent_primers.tsv').write_text(''.join(f"{x['name']}\t{x['F']}\t{x['R']}\n" for x in rr))
subprocess.run([str(root/'work/micucumber_nondegenerate/independent_scan'),str(v)],check=True)
