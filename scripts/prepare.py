from pathlib import Path
import csv,json,collections,hashlib
from Bio import SeqIO
p=Path(__file__).resolve().parent;src=p.parent/'micucumber'
meta={r['accession']:r for r in csv.DictReader((src/'metadata.tsv').open(),delimiter='\t')};records={r.id:r for n in ['target.fasta','background.fasta'] for r in SeqIO.parse(src/n,'fasta')};rows=[];target=[];background=[]
for k,r in records.items():
 m=dict(meta[k]);m['role']='target' if m['clade']=='Crinoidea' else 'background';rows.append(m);(target if m['role']=='target' else background).append(r)
for name,data in [('target.fasta',target),('background.fasta',background)]:SeqIO.write(data,p/name,'fasta')
with (p/'metadata.tsv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
full=[];seen=set()
for r in sorted(target,key=lambda r:r.id):
 seq=str(r.seq).upper();key=(meta[r.id]['organism'],seq)
 if 1100<=len(seq)<=2000 and set(seq)<=set('ACGT') and key not in seen:full.append(r);seen.add(key)
SeqIO.write(full,p/'full_length.fasta','fasta');SeqIO.write([r for r in target if r.id not in {x.id for x in full}],p/'target_fragments.fasta','fasta')
preferred=[r for r in full if meta[r.id]['organism']=='Florometra serratissima'];ref=next((r for r in preferred if r.id.startswith('NC_')),preferred[0] if preferred else full[0]);(p/'config.json').write_text(json.dumps(dict(reference=ref.id,reference_label=meta[ref.id]['organism'],target_clade='Crinoidea',initial_scan_start=100,initial_scan_end=min(1350,len(ref)-35)),indent=2));(p/'baselines.json').write_text('[]')
manifest=dict(target_records=len(target),background_records=len(background),full_length_label_haplotypes=len(full),clades=dict(collections.Counter(m['clade'] for m in rows)),target_annotation=dict(collections.Counter(meta[r.id]['status'] for r in target)),reference=ref.id,source='MiCucumber/MiStar frozen accession data; reclassified Crinoidea as target',inputs={n:hashlib.sha256((src/n).read_bytes()).hexdigest() for n in ['target.fasta','background.fasta','metadata.tsv']},fresh_database_download=False)
(p/'input_manifest.json').write_text(json.dumps(manifest,indent=2));print(json.dumps(manifest,indent=2));print('reference',ref.id,meta[ref.id]['organism'],len(ref))
