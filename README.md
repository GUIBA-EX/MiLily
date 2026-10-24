![MiLily](figures/MiLily_overview_current.png)

# MiLily

[中文](README.zh-CN.md)

Crinoid 16S rRNA primers across five windows: XS, S, M, L and XL. XS is a fixed degenerate single pair; S–XL provide an ordinary single pair, complementary ordinary A/B pairs and a degenerate D single pair at identical coordinates within each length. The release contains 13 portfolios, 17 pair records and 34 oligos.

![Binding positions](figures/binding_positions.svg)

## Portfolio comparison

Coverage and exact matching use a frozen panel of 27 references and 25 taxonomic labels, weighted equally by label and within label. Coverage requires ≤2 mismatches per primer and compatible terminal 3 nt; exact matching requires zero mismatches at both ends. WC3, GT2 and WC4 count paired hits in 7,177 non-target references: ≤3 mismatches per primer, ≤2 under a G–T pairing model, and ≤4, respectively. These counts are not measured amplification proportions.

| Scheme | Coverage % | Exact % | WC≤3 | GT≤2 | WC≤4 |
|---|---:|---:|---:|---:|---:|
| XS | 100.00 | 96.00 | 4196 | 3889 | 4405 |
| SD | 88.00 | 66.00 | 0 | 12 | 15 |
| S | 66.00 | 28.00 | 0 | 0 | 0 |
| SA+SB | 66.00 | 46.00 | 0 | 0 | 0 |
| MD | 100.00 | 84.00 | 16 | 14 | 29 |
| M | 88.00 | 0.00 | 4 | 1 | 11 |
| MA+MB | 88.00 | 20.00 | 4 | 0 | 14 |
| LD | 88.00 | 38.00 | 0 | 0 | 0 |
| L | 88.00 | 30.00 | 0 | 0 | 0 |
| LA+LB | 88.00 | 46.00 | 0 | 0 | 0 |
| XLD | 96.00 | 66.00 | 3 | 3 | 121 |
| XL | 68.00 | 8.00 | 0 | 0 | 6 |
| XLA+XLB | 76.00 | 18.00 | 0 | 0 | 6 |

## XS

XS is retained as a short-amplicon candidate for experimental validation: one pair, F/R degeneracy 3/1, and predicted products of 159–194 bp. Its primer-inclusive span on AF049132.1 is 179 bp. D in the F sequence denotes A/G/T; the assay name is XS.

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XS | `TTGGGGCAACCDCGAAG` | `CAACATCGAGGTCGCAAAC` |

XS passes terminal rules and has compatible duplex Tm ranges. Its three F variants predict internal short hairpins with Tm 62.6–69.4°C, above the 55°C structure gate used for S–XL; the primer 3′ end lies outside the stem. Under the strict target-matching criterion, XS still matches 18 non-target records, including 10 sea-urchin records matching both primers exactly. XS is reported as a fixed candidate rather than a structure/background-gate-passing S–XL design.

[XS assessment and evidence](docs/XS.md) · [Base table](results/xs/base_matching.csv) · [Independent verification](results/xs/background_verification.json)

![XS base matching](figures/base_matching_XS.svg)

## Selecting S–XL

Ordinary, A, B and D variants within each length have identical forward/reverse boundaries. Prefer one pair when sufficient. A/B denote separate-PCR unions with unique coverage or exact-match contributions from both components. D is a single pair only. Retained D degeneracies for S, M, L and XL are 32/64, 16/8, 1/8 and 48/6, balancing matching gains against complexity. WC3 and GT2 limits are 20 records each for SD/MD and 5 each for the other S–XL portfolios. All expanded S–XL sequences pass terminal and both-concentration thermodynamic checks.

[Retention decisions / 保留决策](docs/DECISIONS.md) · [A/B complementarity / 互补性](docs/AB_COMPLEMENTARITY.md)

## S

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| SD | `GATCTAMTGAWRYYCCAA` | `TRTCCCTTTTRGYYTWGY` |
| S | `GATCTAATGAAACCCCAA` | `TATCCCTTTTGGTTTAGC` |
| SA | `GATCTAATGAAACCCCAA` | `TATCCCTTTTGGTTTAGC` |
| SB | `GATCTAATGAAACCCCAA` | `TGTCCCTTTTGGTTTAGC` |

![SD base matching](figures/base_matching_SD.svg)

![S base matching](figures/base_matching_S.svg)

![SA base matching](figures/base_matching_SA.svg)

![SB base matching](figures/base_matching_SB.svg)

## M

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| MD | `TTACTGTTRCAAAAGTAAAYWAAGAR` | `GRCTGCTTYTRGGCCTAC` |
| M | `TTACTGTTGCAAAAGTAAACTAAGAG` | `GGCTGTTTCTAGGCCTAC` |
| MA | `TTACTGTTACAAAAGTAAACTAAGAG` | `GGCTGCTTCTAGGCCTAC` |
| MB | `TTACTGTTGCAAAAGTAAACTAAGAG` | `GACTGCTTCTAGGCCTAC` |

![MD base matching](figures/base_matching_MD.svg)

![M base matching](figures/base_matching_M.svg)

![MA base matching](figures/base_matching_MA.svg)

![MB base matching](figures/base_matching_MB.svg)

## L

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| LD | `CAAGAGATCTAATGAAACCCCA` | `GRCTGCTTYTRGGCCTAC` |
| L | `CAAGAGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` |
| LA | `CAAGAGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` |
| LB | `CAAGGGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` |

![LD base matching](figures/base_matching_LD.svg)

![L base matching](figures/base_matching_L.svg)

![LA base matching](figures/base_matching_LA.svg)

![LB base matching](figures/base_matching_LB.svg)

## XL

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XLD | `AGGCAAVACGARRRCTYAACTG` | `GACTYDCGTCGGTCTGAA` |
| XL | `AGGCAAGACGAAAGCTTAACTG` | `GACTTGCGTCGGTCTGAA` |
| XLA | `AGGCAACACGAAAACTTAACTG` | `GACTTGCGTCGGTCTGAA` |
| XLB | `AGGCAAGACGAAAGCTTAACTG` | `GACTTGCGTCGGTCTGAA` |

![XLD base matching](figures/base_matching_XLD.svg)

![XL base matching](figures/base_matching_XL.svg)

![XLA base matching](figures/base_matching_XLA.svg)

![XLB base matching](figures/base_matching_XLB.svg)

## Data and reproduction

Independent verification covers 918 target decisions and 34 background-set checks with zero disagreements. A wider target-length scan confirms that XS metrics do not depend on the 150–500 bp filter. Design and evaluation share references; this release adds no wet-lab validation. On the same 25-label panel, XS has 22/25 labels without observed shared barcodes (88%), the same as MD; this is not an identification-success rate for unknown species.

[Sequences](sequences/primer_pairs.csv) · [FASTA](sequences/primers.fasta) · [Results](results/comparison.csv) · [Base matching](results/base_matching.html) · [Methods](docs/METHODS.md) · [Reproduction](docs/REPRODUCIBILITY.md) · [Files](docs/FILES.md)

[Copyright / 著作权声明](COPYRIGHT.md)
