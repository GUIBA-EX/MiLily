# D引物优化 / D-primer optimization

每个长度保留一对D，与普通/A/B起止坐标完全相同。主覆盖率与完全匹配率均先按每目内有命中的分类标签比例计算，再对四目等权平均。标签有多条参考时，任一参考命中即算检出，种内完整/部分覆盖另列。/ Each length retains one D pair at the ordinary/A/B coordinates. Coverage and exact matching average the fraction of detected labels within each order equally across four orders; any matching reference detects a label, while within-label completeness is reported separately.

共同面板27条参考、25个分类标签：Comatulida 22，Cyrtocrinida 1，Hyocrinida 1，Isocrinida 1。Hyocrinidae sp.及属级标签并非已鉴定物种；三个有柄目各仅一条参考，不能把本面板满覆盖解释为全目通用。旧面板order列均为Crinoidea，本轮仅在分类映射表中修正，旧权重留作次要比较。

The common panel has 27 references and 25 labels: 22 Comatulida and one each in Cyrtocrinida, Hyocrinida and Isocrinida. Family/genus-level labels are not identified species. One reference per stalked order provides limited within-order evidence. The former order column contained Crinoidea throughout; the corrected mapping is frozen separately.

分类依据 / Taxonomic sources: [Neogymnocrinus richeri, NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=710152), [Metacrinus rotundus, JAMSTEC](https://www.godac.jamstec.go.jp/bismal/e/view/9000385), [crinoid phylogenomics](https://doi.org/10.1098/rsos.251924).

## 当前选择 / Current selection

| D | Order coverage: before → after % | Order exact: before → after % | F/R degeneracy | Strict WC / GT | Broad WC3 / GT2 |
|---|---:|---:|---:|---:|---:|
| SD | 25.00 → 71.59 | 19.32 → 43.18 | 128/128 | 0 / 4 | 4 / 7 |
| MD | 100.00 → 100.00 | 23.86 → 50.00 | 96/8 | 10 / 18 | 26 / 23 |
| LD | 25.00 → 50.00 | 11.36 → 14.77 | 32/8 | 0 / 0 | 0 / 0 |
| XLD | 75.00 → 75.00 | 67.05 → 68.18 | 72/6 | 3 / 3 | 8 / 3 |

在2,360组同坐标组合中，以目间覆盖优先、目间完全匹配其次；每方向简并度≤128、严格WC/GT各≤20、宽松WC3/GT2各≤100。完全匹配在目间和标签两级均不得低于基线，标签覆盖最多下降4个百分点。末端规则及两种浓度场景热力学均须通过。比较20/50/100三档宽松背景门槛，选择符合当前允许少量非目标的收益较高方案。这是有界搜索内的选择，不是全局最优证明。

The 2,360 coordinate-fixed combinations are ranked by order coverage, then order exact matching. Degeneracy is capped at 128 per direction, strict WC/GT at 20 records each, and broad WC3/GT2 at 100 each. Exact matching cannot fall below baseline at either hierarchy; label coverage can fall by at most four percentage points. Terminal and two-concentration thermodynamic checks must pass. Background caps of 20/50/100 were compared. These are bounded-search choices.

S的收益伴随128/128简并度和部分标签替换；200 nM/方向时每变体仅1.5625 nM。M的50条门槛方案完全匹配更好，严格背景仍≤20。L的部分目间高分方案曾只覆盖少量标签，因此用标签保护条件剔除。XL收益较小，应与较低简并度旧方案共同进入实验比较。

S increases breadth at 128/128 degeneracy and exchanges some detected labels; at 200 nM per direction each variant receives 1.5625 nM. M improves exact matching under the 50-record broad cap while retaining strict hits ≤20. Label safeguards exclude L solutions with high macro scores but sparse total detection. XL improves modestly and merits an experimental comparison with the less degenerate baseline.

## 每目覆盖 / Coverage by order

| Assay | Comatulida | Cyrtocrinida | Hyocrinida | Isocrinida |
|---|---:|---:|---:|---:|
| SD-before | 22/22 | 0/1 | 0/1 | 0/1 |
| SD | 19/22 | 1/1 | 0/1 | 1/1 |
| MD-before | 22/22 | 1/1 | 1/1 | 1/1 |
| MD | 22/22 | 1/1 | 1/1 | 1/1 |
| LD-before | 22/22 | 0/1 | 0/1 | 0/1 |
| LD | 22/22 | 0/1 | 0/1 | 1/1 |
| XLD-before | 22/22 | 0/1 | 1/1 | 1/1 |
| XLD | 22/22 | 0/1 | 1/1 | 1/1 |

逐标签增减 / Label changes:

- SD coverage_hits: gained: Metacrinus rotundus, Neogymnocrinus richeri; lost: Antedon mediterranea, Capillaster sp. DH-Y2, Thaumatocrinus sp. JL223
- SD exact_hits: gained: Neogymnocrinus richeri, Poliometra prolixa; lost: Cyllometra manca, Thaumatocrinus sp. JL223
- MD coverage_hits: gained: none; lost: none
- MD exact_hits: gained: Anneissia pinguis, Metacrinus rotundus; lost: none
- LD coverage_hits: gained: Metacrinus rotundus; lost: none
- LD exact_hits: gained: Comatella stelligera, Stephanometra indica, Zygometra comata; lost: none
- XLD coverage_hits: gained: none; lost: none
- XLD exact_hits: gained: Tropiometra macrodiscus; lost: none

## 复核 / Verification

C++全窗口扫描与独立Python位并行扫描：486项目标判定、36个严格/完全匹配背景集合、45项宽松/严格背景计数，差异0。/ Independent C++ and Python scans agree on 486 target decisions, 36 background sets and 45 background counts.

[全部候选 / Candidates](../results/D_optimization/verified_comparison.csv) · [逐标签 / By label](../results/D_optimization/by_taxon.csv) · [选择规则 / Policy](../results/D_optimization/policy.json) · [独立复现包 / Reproduction](../results/D_optimization/reproduction_sources.zip)
