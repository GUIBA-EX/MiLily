![MiLily](figures/MiLily_overview_current.png)

# MiLily

[中文](README.zh-CN.md)

## Abstract

Candidate mitochondrial 16S rRNA primers for environmental DNA across XS, S, M, L and XL. Each S–XL window retains an ordinary pair and a degenerate D pair at shared reference coordinates; XS is a single retained pair.
One reference per species is retained. Primary metrics weight evaluable species equally, with order-level results reported separately.
The crinoid panel contains 128 species, but only 19 are evaluable for S–XL. XS was designed manually and is assessed separately.

S–XL were evaluated on 19 species, while the manually designed XS was assessed separately. SD covers 17/19 and MD covers 19/19 on the current S–XL panel. Laboratory testing and broader reference sampling remain necessary.

## Introduction

Environmental DNA metabarcoding of crinoids depends on reference sequences that represent both the target taxa and the primer-binding sites. MiLily compares mitochondrial 16S primer windows and includes a manually designed XS pair assessed on its own reference panel. Marine eDNA metabarcoding studies demonstrate the importance of marker and reference-library choice (Gold et al., 2022); MiFish provides an example of sequence-alignment-based primer design for fishes (Miya et al., 2015). Mitochondrial 16S has been used alongside other markers in crinoid phylogenetic studies (Taylor et al., 2023).

[参考面板 / Reference panel](results/species_qc/panel.csv) · [参考序列审核 / Reference curation](results/species_qc/README.md)

![Reference binding positions](figures/amplicon_regions.en.svg)

## Methods

### Reference datasets and alignment

The target library comprised 269 mitochondrial sequence records from crinoids; the non-target library comprised 7,177 reference records. Target records were reviewed for sequence quality and taxonomy, and one representative was retained per identifiable species (128 species). Representatives were selected using binding-window completeness, ambiguous bases and reference-site coverage, without using primer-match outcomes. The retained sequences were realigned with MAFFT 7.526 (Katoh & Standley, 2013) using the ungapped mitochondrial 16S rRNA reference AF049132.1; positions are reported as 1-based coordinates. For the curated species panels, each binding window had to span the reference region, contain at least 90% of its reference-site count as A/C/G/T, and contain no ambiguous nucleotide; alignment gaps were permitted. The numbers of evaluable species were 19 for each S–XL window; missing windows were excluded from the corresponding denominator. The [reference audit](results/species_qc/README.md) provides the selection criteria and accession-level records.

### Primer design and screening

Ordinary and degenerate candidates were compared within fixed forward and reverse reference windows. For S–XL, the ordinary and D pairs at each length share the same reference endpoints. D oligonucleotides were limited to eight concrete variants per primer, with IUPAC ambiguity confined to the 3′ half. Terminal screening excluded homotriplet ends and homopolymers longer than four bases and required a G or C in the final three positions. Primer3 (Untergasser et al., 2012) evaluations used 50 mM monovalent salt, 1.5 mM Mg²⁺ and 0.6 mM dNTP, under 50 nM per variant and 200 nM total per direction. The S–XL structural gate required a maximum predicted structure Tm below 55 °C and a forward–reverse duplex-Tm midpoint difference of at most 5 °C. XS was designed manually and assessed separately on its original 27-reference, 25-label panel. Its non-target and secondary-structure results were recorded separately rather than applying the S–XL selection gates retrospectively.

### In-silico evaluation

Target coverage required at most two mismatches per primer and IUPAC-compatible final 3 nt; exact matching required zero mismatches at both sites. For S–XL, paired target scans required an amplicon of 150–500 bp and an internal distance of at least 50 bp. Background searches allowed an internal distance of 0–1,000 bp. Strict Watson–Crick (WC) and G–T models retained the terminal constraint; WC≤3 and GT≤2 were additional permissive screens without that constraint. For the current S–XL species panel, coverage and exact-match percentages weighted evaluable species equally, with results also summarized by order; non-target counts represent reference records. C++ and Python scans were compared on the same sequence data to verify target and strict background hit sets. These are computational predictions and require experimental validation.

[Detailed methods](docs/METHODS.md) · [Validation](docs/VALIDATION.md)

## Results

### Predicted performance

| Name | Coverage | Exact | Strict WC / GT | WC≤3 / GT≤2 |
|---|---:|---:|---:|---:|
| S | 14/19 (73.68%) | 6/19 (31.58%) | 0 / 0 | 0 / 0 |
| SD | 17/19 (89.47%) | 10/19 (52.63%) | 0 / 5 | 0 / 10 |
| M | 17/19 (89.47%) | 0/19 (0.00%) | 0 / 1 | 4 / 1 |
| MD | 19/19 (100.00%) | 7/19 (36.84%) | 2 / 9 | 13 / 10 |
| L | 17/19 (89.47%) | 6/19 (31.58%) | 0 / 0 | 0 / 0 |
| LD | 17/19 (89.47%) | 8/19 (42.11%) | 0 / 0 | 0 / 0 |
| XL | 12/19 (63.16%) | 0/19 (0.00%) | 0 / 0 | 0 / 0 |
| XLD | 18/19 (94.74%) | 2/19 (10.53%) | 0 / 3 | 4 / 3 |

Coverage allows at most two mismatches per primer with compatible terminal 3 nt; exact matching requires zero mismatches in both primers. Strict WC/GT retain the terminal constraint; WC≤3 / GT≤2 are permissive background screens.

Each D primer has at most eight variants, with ambiguity confined to its 3′ half. XS is a single pair with a fixed name. Computational predictions require experimental validation.

SD covers all 17 evaluable Comatulida but neither the Cyrtocrinida nor Isocrinida representative. The XS structure and background assessment is reported in [XS assessment](results/xs/assessment.json).

### XS

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XS | `TTGGGGCAACCDCGAAG` | `CAACATCGAGGTCGCAAAC` |

![XS base matching](figures/base_matching_XS.svg)

The XS diagram uses its original reference panel.

### S

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| S | `GATCTAATGAAACCCCAA` | `TATCCCTTTTGGTTTAGC` |
| SD | `GATCTAATGAARYYCCAA` | `TATCCCTTTTRGTTTWGY` |

![S base matching](results/current_primers/S/base_matching_S.svg)

![SD base matching](results/current_primers/S/base_matching_SD.svg)

[S · Orders](results/current_primers/S/S_by_order.csv) · [Species](results/current_primers/S/S_by_taxon.csv)

[SD · Orders](results/current_primers/S/SD_by_order.csv) · [Species](results/current_primers/S/SD_by_taxon.csv)

### M

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| M | `TTACTGTTGCAAAAGTAAACTAAGAG` | `GGCTGTTTCTAGGCCTAC` |
| MD | `TTACTGTTGCAAAAGTAAAYWAAGAR` | `GGCTGCTTCTAGGCCTAC` |

![M base matching](results/current_primers/M/base_matching_M.svg)

![MD base matching](results/current_primers/M/base_matching_MD.svg)

[M · Orders](results/current_primers/M/M_by_order.csv) · [Species](results/current_primers/M/M_by_taxon.csv)

[MD · Orders](results/current_primers/M/MD_by_order.csv) · [Species](results/current_primers/M/MD_by_taxon.csv)

### L

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| L | `CAAGAGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` |
| LD | `CAAGAGATCTAATGAARMCCCA` | `GGCTGCTTCTAGGCCTAC` |

![L base matching](results/current_primers/L/base_matching_L.svg)

![LD base matching](results/current_primers/L/base_matching_LD.svg)

[L · Orders](results/current_primers/L/L_by_order.csv) · [Species](results/current_primers/L/L_by_taxon.csv)

[LD · Orders](results/current_primers/L/LD_by_order.csv) · [Species](results/current_primers/L/LD_by_taxon.csv)

### XL

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XL | `AGGCAAGACGAAAGCTTAACTG` | `GACTTGCGTCGGTCTGAA` |
| XLD | `AGGCAAGACGAARRYTTAACTG` | `GACTTACGTCGGTCTGAA` |

![XL base matching](results/current_primers/XL/base_matching_XL.svg)

![XLD base matching](results/current_primers/XL/base_matching_XLD.svg)

[XL · Orders](results/current_primers/XL/XL_by_order.csv) · [Species](results/current_primers/XL/XL_by_taxon.csv)

[XLD · Orders](results/current_primers/XL/XLD_by_order.csv) · [Species](results/current_primers/XL/XLD_by_taxon.csv)

## Discussion

The S–XL evaluation includes 19 species from the curated 128-species panel. SD covers all 17 evaluable Comatulida but not the sampled Cyrtocrinida or Isocrinida representatives. The manually designed XS was evaluated on a different 27-reference, 25-label panel and has predicted secondary-structure and non-target matches; its metrics should therefore be interpreted using that panel and assessment. Broader reference sampling and laboratory validation are needed to assess performance across crinoids.

[Copyright / 著作权](COPYRIGHT.md)

## References

1. Gold, Z., Wall, A. R., Schweizer, T. M., et al. (2022). A manager’s guide to using eDNA metabarcoding in marine ecosystems. *PeerJ*, 10, e14071. https://doi.org/10.7717/peerj.14071

2. Miya, M., Sato, Y., Fukunaga, T., et al. (2015). MiFish, a set of universal PCR primers for metabarcoding environmental DNA from fishes: detection of more than 230 subtropical marine species. *Royal Society Open Science*, 2, 150088. https://doi.org/10.1098/rsos.150088

3. Taylor, K. H., Rouse, G. W., & Messing, C. G. (2023). Phylogeny and taxonomy of Himerometroidea (Echinodermata: Crinoidea). *Zootaxa*, 5277, 149–164. https://doi.org/10.11646/zootaxa.5277.1.7

4. Katoh, K., & Standley, D. M. (2013). MAFFT multiple sequence alignment software version 7: improvements in performance and usability. *Molecular Biology and Evolution*, 30, 772–780. https://doi.org/10.1093/molbev/mst010

5. Untergasser, A., Cutcutache, I., Koressaar, T., et al. (2012). Primer3—new capabilities and interfaces. *Nucleic Acids Research*, 40, e115. https://doi.org/10.1093/nar/gks596
