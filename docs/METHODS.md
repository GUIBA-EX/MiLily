# Methods

MiLily combines a fixed XS candidate with four S–XL windows designed at shared coordinates. XS sequences are fixed and their structure/background screens are reported explicitly; S–XL use constrained candidate searches.

Reference: AF049132.1, extracted ungapped 16S, 1-based coordinates. The frozen matching panel contains 27 records and 25 taxonomic labels; primary scores equally average within-order label detection; earlier reference weights are secondary. Target FASTA contains 269 records, and the background contains 7,177 non-crinoid records. Partial-reference availability varies by window; main comparisons use the common panel.

Coverage requires ≤2 mismatches per primer and IUPAC-compatible final 3 nt; exact matching requires no mismatches at either end. Background WC3 and GT2 permit ≤3 mismatches per primer and ≤2 under a G–T model, respectively; WC4 is a broader sensitivity check. Strict background matching uses the target coverage criterion and is separately reported for XS. All numbers count reference records, not environmental amplification fractions.

S–XL share identical ordinary/A/B/D boundaries within each length. A/B denote separate-PCR unions and require unique contributions from both components. Their search includes observed haplotypes, concrete variants and supported substitutions; the current expanded A/B search is documented in [AB_COMPLEMENTARITY.md](AB_COMPLEMENTARITY.md). D retention balances coverage/exact gains and complexity; [DECISIONS.md](DECISIONS.md) records the choice. Current D assays use ≤100 broad WC3/GT2 and ≤20 strict WC/GT records each; ordinary/A/B retain their original gates.

Terminal checks: no terminal homotriplet, ≥1 GC in the last 3 nt, 1–4 GC in the last 5 nt, and no homopolymer longer than 4; 3′ degeneracy is allowed. Primer3 uses 50 mM monovalent salt, 1.5 mM Mg²⁺, 0.6 mM dNTP, and scenarios of 50 nM per variant or 200 nM total per direction. S–XL require structure Tm <55°C and F/R Tm-range midpoint difference ≤5°C. XS passes terminal and duplex compatibility checks but exceeds the structure/background gates; [XS.md](XS.md) reports the explicit candidate assessment and temperature-dependent ΔG.

Exhaustive full-sequence C++ scanning checks both strands and paired orientation/distance. Independent XS verification uses local ±5 nt aligned target windows and a Python bit-parallel substitution scanner for background sets. Across the release, 918 target decisions and 34 background-set comparisons agree. XS also gives unchanged headline metrics in a wider 1–5,000 bp target-length scan. These are independent algorithms on shared reference data, not independent biological validation.

## 目间等权D优化 / Order-balanced D optimization

主指标、候选门槛、分类映射、逐类群增减和独立复核以[D优化](D_OPTIMIZATION.md)为准。当前D由2,360组同坐标组合筛选；普通/A/B与XS未改变。/ Current D selection uses 2,360 same-coordinate pairs, equal order weighting and explicit label safeguards, as documented in [D optimization](D_OPTIMIZATION.md). Ordinary/A/B and XS remain unchanged.
