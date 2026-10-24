# MiLily

[中文](README.zh-CN.md)

![Binding positions](figures/binding_positions.svg)

Each length uses one shared locus: ordinary, A, B and D have identical forward and reverse start/end coordinates. At each locus, ordinary single, ordinary A/B union and degenerate single are selected by coverage plus exact matching; their scores are averaged equally to select the locus. Background limits are WC≤3 ≤5 and GT≤2 ≤5 accessions. All concrete variants pass terminal rules and both thermodynamic scenarios. A/B results are separate-PCR unions, not experimentally validated multiplex results. References are reused for design and evaluation; coverage is computational, not measured PCR efficiency.

D denotes a degenerate single pair; no suffix denotes an ordinary single pair; A/B are ordinary same-locus alternatives. Each project has 12 portfolios, 16 pair records and 32 sequences.

| Scheme | Coverage % | Exact % | WC≤3 | GT≤2 | WC≤4 |
|---|---:|---:|---:|---:|---:|
| SD | 72.00 | 46.00 | 0 | 0 | 0 |
| S | 66.00 | 28.00 | 0 | 0 | 0 |
| SA+SB | 66.00 | 46.00 | 0 | 0 | 0 |
| MD | 68.00 | 16.00 | 2 | 0 | 11 |
| M | 88.00 | 0.00 | 4 | 1 | 11 |
| MA+MB | 88.00 | 16.00 | 4 | 1 | 14 |
| LD | 88.00 | 30.00 | 0 | 0 | 0 |
| L | 88.00 | 30.00 | 0 | 0 | 0 |
| LA+LB | 88.00 | 46.00 | 0 | 0 | 0 |
| XLD | 88.00 | 62.00 | 3 | 0 | 104 |
| XL | 68.00 | 8.00 | 0 | 0 | 6 |
| XLA+XLB | 76.00 | 18.00 | 0 | 0 | 6 |

Background hits can remain substantial under relaxed mismatch models; see the complete results and missed-reference records.

[Sequences](sequences/primer_pairs.csv) · [FASTA](sequences/primers.fasta) · [Results](results/comparison.csv) · [Verification](results/verification.json) · [Full base matching](results/base_matching.html)

## S

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| SD | `GATCTAATGAAACCCCAA` | `TRTCCCTTTTGGTYTAGC` |
| S | `GATCTAATGAAACCCCAA` | `TATCCCTTTTGGTTTAGC` |
| SA | `GATCTAATGAAACCCCAA` | `TATCCCTTTTGGTTTAGC` |
| SB | `GATCTAATGAAACCCCAA` | `TGTCCCTTTTGGTTTAGC` |

![SD base matching](figures/base_matching_SD.svg)

![S base matching](figures/base_matching_S.svg)
## M

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| MD | `TTACTGTTACAAAAGTAAACTAAGAG` | `GGCTGYTTCTAGGCCTAC` |
| M | `TTACTGTTGCAAAAGTAAACTAAGAG` | `GGCTGTTTCTAGGCCTAC` |
| MA | `TTACTGTTGCAAAAGTAAACTAAGAG` | `GGCTGTTTCTAGGCCTAC` |
| MB | `TTACTGTTACAAAAGTAAACTAAGAG` | `GGCTGCTTCTAGGCCTAC` |

![MD base matching](figures/base_matching_MD.svg)

![M base matching](figures/base_matching_M.svg)
## L

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| LD | `CAAGAGATCTAATGAAACCCCA` | `GGCTGYTTCTAGGCCTAC` |
| L | `CAAGAGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` |
| LA | `CAAGAGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` |
| LB | `CAAGGGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` |

![LD base matching](figures/base_matching_LD.svg)

![L base matching](figures/base_matching_L.svg)
## XL

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XLD | `AGGCAAVACGAARRCTYAACTG` | `GACTTDCGTCGGTCTGAA` |
| XL | `AGGCAAGACGAAAGCTTAACTG` | `GACTTGCGTCGGTCTGAA` |
| XLA | `AGGCAAGACGAAAGCTTAACTG` | `GACTTGCGTCGGTCTGAA` |
| XLB | `AGGCAACACGAAAACTTAACTG` | `GACTTGCGTCGGTCTGAA` |

![XLD base matching](figures/base_matching_XLD.svg)

![XL base matching](figures/base_matching_XL.svg)

Independent target checks: 864; disagreements: 0. Background set checks: 32; disagreements: 0.

[Copyright / 著作权声明](COPYRIGHT.md)
