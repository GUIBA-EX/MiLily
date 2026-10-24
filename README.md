![MiLily overview](figures/MiLily_overview.png)

# MiLily

Crinoid mitochondrial 16S primers · First computational trial

[简体中文](README.zh-CN.md)

Banner badges show the reference spans, including primers, of SD, MD, LD and XLD: 162, 253, 302 and 443 bp. The map below shows actual binding coordinates for every candidate; animal illustrations are schematic.

![MiLily binding positions](figures/binding_positions.svg)

Following the MiCucumber/MiUrchin workflow, four reference-length bands compare degenerate and ordinary designs. D marks one degenerate pair; an unsuffixed name marks one ordinary pair; A/B are ordinary components used in separate PCRs. There are 12 portfolios, 16 paired records and 32 oligos. Both forward and reverse starts of A/B components differ by at most 35 bp. Alternative portfolios can use different loci; length labels do not imply identical sites.

## First-trial priorities

Prioritize **SD** for a short amplicon with relatively high exact matching, **MD** for maximal degenerate single-pair coverage, and **LD** for intermediate length and balanced coverage/exact matching. For fewer oligo variants, ordinary **L** is a strong candidate: 88% coverage, 30% exact matching, and zero WC≤3, GT≤2 and WC≤4 background hits. LA/LB raises exact matching to 38% without improving coverage. XLD reaches 62% exact matching but has 104 WC≤4 background hits. These are computational candidates without wet-lab validation.

## Shared complete-sequence panel

27 full-sequence haplotypes deduplicated within 25 taxonomic labels, including unresolved identifications; these are not 25 confirmed species. Labels and within-label haplotypes receive equal weights. Coverage requires ≤2 mismatches per primer and IUPAC-compatible terminal 3 nt; exact matching requires zero mismatches on both primers.

| Scheme | Coverage | Exact | WC≤3 | GT≤2 | WC≤4 | Observed product bp |
|---|---:|---:|---:|---:|---:|---|
| SD | 84.0% | 66.0% | 0 | 0 | 11 | 160–170 |
| S | 66.0% | 28.0% | 0 | 0 | 0 | 194–203 |
| SA+SB | 84.0% | 18.0% | 0 | 4 | 25 | 198–214 |
| MD | 92.0% | 26.0% | 0 | 0 | 2 | 250–260 |
| M | 76.0% | 14.0% | 4 | 2 | 11 | 250–260 |
| MA+MB | 88.0% | 22.0% | 4 | 3 | 18 | 243–260 |
| LD | 88.0% | 54.0% | 0 | 1 | 9 | 302–311 |
| L | 88.0% | 30.0% | 0 | 0 | 0 | 288–297 |
| LA+LB | 88.0% | 38.0% | 0 | 0 | 22 | 288–317 |
| XLD | 88.0% | 62.0% | 3 | 0 | 104 | 443–471 |
| XL | 68.0% | 8.0% | 0 | 0 | 26 | 438–462 |
| XLA+XLB | 92.0% | 16.0% | 0 | 0 | 48 | 376–462 |

Background counts are accessions among 7,177 frozen records, not probabilities of amplification. GT permits possible G–T pairing; WC≤4 is a more permissive sensitivity analysis. Two-pair metrics are separate-PCR unions, not validated multiplex performance.

## Reference scope and limits

The existing frozen MiStar/MiCucumber corpus supplies 269 crinoid 16S records; no exhaustive refresh was performed. Coordinates use extracted 16S of *Florometra serratissima* AF049132.1, 1-based and ungapped. Reference spans are S150–224, M225–284, L285–359 and XL360–450 bp including primers; taxon-specific products may fall outside these bands.

Most partial records do not span selected sites. Except XLA/XLB, portfolios have 43 evaluable records representing 25 labels; these include full-sequence duplicates, and deduplicated weighted metrics match the complete panel. XLA/XLB has 95 evaluable records / 66 labels, with 84.09% coverage and 26.52% exact matching. Evaluable sets differ and are not directly ranked. Missing site coverage is marked unevaluable, not a demonstrated failure. Selection and evaluation share the design panel: this is not a held-out test. The bounded coordinate/length grid and spatial shortlist do not guarantee a global optimum.

## Terminal and thermodynamic rules

3′ degeneracy is allowed, including the final base. Every concrete variant has no terminal homotriplet, ≥1 G/C in the last 3 nt, 1–4 G/C in the last 5 nt and no homopolymer longer than 4. Two scenarios use 50 nM per variant and 200 nM per direction equally divided among variants, with 50 mM monovalent salt, 1.5 mM Mg and 0.6 mM dNTP. All hairpin/dimer Tm values are <55°C and F/R Tm-range midpoint difference is ≤5°C. Unequal-concentration heterodimers use the larger partner concentration as an approximation.

## Sequences, figures and reproduction

[Paired sequences](sequences/primer_pairs.csv) · [FASTA](sequences/primers.fasta) · [Full comparison](results/comparison.csv) · [Missed panel references](results/missed_references.csv) · [Target evaluation](results/target_evaluation.csv) · [Background accessions](results/background_hits.csv) · [Observed barcode resolution](results/barcode_resolution.csv)

[All base-matching figures](results/base_matching.html) · [Coordinates](results/binding_positions.csv) · [Terminal audit](results/terminal_audit.csv) · [Thermodynamics](results/thermal.csv) · [Independent verification](results/verification.json) · [Methods](docs/METHODS.md) · [Reproduction](docs/REPRODUCIBILITY.md)

Base plots show all 27 complete sequences oriented as the primer, 5′→3′. Blue marks IUPAC compatibility, orange a mismatch, and the box terminal 3 nt. Question marks indicate unequal-length windows. Barcode resolution describes observed sharing of identical internal sequences among detected labels, not true species identification accuracy.

### S

All sequences are written 5′→3′; R is the reverse oligo as ordered.

| Name | Forward F | Reverse R | Degeneracy F / R |
|---|---|---|---:|
| SD | `TTACTGTTDCAAAAGTAAAYWAAGAR` | `AGYTTRTCCCTTTTRGTYTAGY` | 24 / 32 |
| S | `GATCTAATGAAACCCCAA` | `TATCCCTTTTGGTTTAGC` | 1 / 1 |
| SA | `GTGAAACGAGCTTGGTGATAGC` | `TTGGTGGCTGCTTCTAGG` | 1 / 1 |
| SB | `AATGAGTTTAAGCTCAAG` | `TTTATTATGCTTTAACGC` | 1 / 1 |

![MiLily SD](figures/base_matching_SD.svg)

[Ordinary S](figures/base_matching_S.svg) · [SA](figures/base_matching_SA.svg) · [SB](figures/base_matching_SB.svg)

### M

All sequences are written 5′→3′; R is the reverse oligo as ordered.

| Name | Forward F | Reverse R | Degeneracy F / R |
|---|---|---|---:|
| MD | `AWRTATTACTGTTRCAAAAGTAAAYWAAGA` | `GGCTGCTTCTAGGCCTAC` | 32 / 1 |
| M | `TTACTGTTACAAAAGTAAACAAAGAG` | `TTGGTGGCTGCTTCTAGG` | 1 / 1 |
| MA | `TTACTGTTACAAAAGTAAACAAAGAG` | `TTGGTGGCTGCTTCTAGG` | 1 / 1 |
| MB | `GTTGCAAAAGTAAACTAAGAGG` | `GGCTGCTTCTAGGCCTAC` | 1 / 1 |

![MiLily MD](figures/base_matching_MD.svg)

[Ordinary M](figures/base_matching_M.svg) · [MA](figures/base_matching_MA.svg) · [MB](figures/base_matching_MB.svg)

### L

All sequences are written 5′→3′; R is the reverse oligo as ordered.

| Name | Forward F | Reverse R | Degeneracy F / R |
|---|---|---|---:|
| LD | `WACCCGAAACCARGRGATCTAATGMW` | `WGDTGGCTGYTTCTAGGCCTAC` | 32 / 12 |
| L | `CAAGAGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` | 1 / 1 |
| LA | `TTCAAAACCCGAAACCAAGAGA` | `TTGGTGGCTGCTTCTAGG` | 1 / 1 |
| LB | `CAAGAGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` | 1 / 1 |

![MiLily LD](figures/base_matching_LD.svg)

[Ordinary L](figures/base_matching_L.svg) · [LA](figures/base_matching_LA.svg) · [LB](figures/base_matching_LB.svg)

### XL

All sequences are written 5′→3′; R is the reverse oligo as ordered.

| Name | Forward F | Reverse R | Degeneracy F / R |
|---|---|---|---:|
| XLD | `AGGCAAVACGAARRCTYAACTG` | `GACTTDCGTCGGTCTGAA` | 24 / 3 |
| XL | `AGGCAAGACGAAAGCTTAACTG` | `GCGTCGGTCTGAACTCAG` | 1 / 1 |
| XLA | `AGGCAAGACGAAAGCTTAACTG` | `GCGTCGGTCTGAACTCAG` | 1 / 1 |
| XLB | `AAAAGAAATTAATATTTTAGTGAAGA` | `TTTAAAGGTCGAACAGAC` | 1 / 1 |

![MiLily XLD](figures/base_matching_XLD.svg)

[Ordinary XL](figures/base_matching_XL.svg) · [XLA](figures/base_matching_XLA.svg) · [XLB](figures/base_matching_XLB.svg)

Independent whole-sequence scans: all 864 target-state and 32 background-set comparisons agree. See the verification record.

[Copyright / 著作权声明](COPYRIGHT.md)

[GitHub: GUIBA-EX/MiLily](https://github.com/GUIBA-EX/MiLily) · [文件索引 / File index](docs/FILES.md)
