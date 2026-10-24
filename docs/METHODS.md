# MiLily design record

Objective: exploratory crinoid mitochondrial 16S primers, following MiCucumber/MiUrchin constraints. Allow terminal IUPAC degeneracy. Compare one degenerate pair, one ordinary pair and two ordinary pairs for S/M/L/XL. Release destination: GUIBA-EX/MiLily.

Data: reuse the frozen MiStar/MiCucumber annotated 16S accession corpus, reclassifying Crinoidea as target. 269 target records, 7,177 background records. No fresh exhaustive database retrieval. Complete 1,100–2,000 nt ACGT sequences, deduplicated within organism label, define 27 haplotypes / 25 labels. Includes unresolved labels; these are not 25 confirmed species. Florometra serratissima AF049132.1 is the coordinate reference.

Design: scan 5-bp starts with lengths 18/22/26/30; observed top-3 ordinary oligos plus majority consensus and IUPAC candidates capped at 4/16/32 variants. Retain terminal-safe candidates supported by >=65% alignable panel weight and >=20% per-side coverage; screen Tm 45–75 °C in both concentration scenarios. Retain up to 3 candidates per 25-bp bin, side and chemistry for a bounded first trial. This is not exhaustive optimization.

Bands on reference: S150–224; M225–284; L285–359; XL360–450 bp, including primers. Choose coverage+exact weighted score, then coverage/exact, lower degeneracy/background. Background gates <=5 accessions for each WC3 and GT2 model. Report WC4 sensitivity.

Every concrete variant: no terminal homotriplet, >=1 GC in last3, 1–4 GC in last5, no homopolymer >4. Both 50 nM per variant and 200 nM per direction, split equally, evaluated with 50 mM monovalent, 1.5 mM Mg, 0.6 mM dNTP. Hairpin/all dimer maxTm <55°C; F/R Tm-range midpoints differ <=5°C. Heterodimer concentration approximated with larger partner concentration. Not experimental validation.

Validation: separate exhaustive C++ whole-sequence paired-product scan, both orientations, no seed shortcut; independent background-set comparison; full-panel coverage with <=2 mismatches per primer and IUPAC-compatible last3; zero mismatches for exact. Short-fragment sequence-end completeness evaluated separately. Two-pair results are separate-PCR unions, not a tested multiplex.

Ordinary A/B components are restricted to nearby binding windows: both forward and reverse start coordinates differ by at most 35 bp. Length-band labels do not imply identical loci across all alternative portfolios.
