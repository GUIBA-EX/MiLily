![MiLily介绍图：XS、S、M、L、XL](figures/MiLily_overview_current.png)

圆标为AF049132.1上的含引物参考跨度：XS 179、S 193、M 248、L 288、XL 443 bp。XS在参考面板中的预测产物长度为159–194 bp。

# MiLily

[English](README.md)

海百合16S rRNA引物，包含XS、S、M、L、XL五个长度窗口。XS为固定简并单对；S–XL各提供普通单对、同坐标普通A/B双对和简并D单对。现有13套方案、17对记录、34条引物序列。

![Binding positions](figures/binding_positions.svg)

## 方案比较

覆盖与完全匹配率使用27条参考、25个分类标签的冻结面板，标签等权、标签内等权。覆盖要求每条≤2个错配且末端3 nt兼容；完全匹配要求两端无错配。WC3、GT2、WC4为7,177条非目标参考中的成对命中数，分别使用每条≤3错配、允许G–T配对每条≤2错配、每条≤4错配；不代表实测扩增比例。

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

XS保留为短片段实验候选：一对引物，F/R简并度3/1，预测产物159–194 bp；在参考AF049132.1上的含引物跨度179 bp。F中的D=A/G/T，名称使用XS。

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XS | `TTGGGGCAACCDCGAAG` | `CAACATCGAGGTCGCAAAC` |

XS末端规则通过，双链Tm配对合适；F三个变体预测内部短发卡Tm为62.6–69.4°C，超过S–XL设计采用的55°C结构门槛，3′端不在该茎内。XS在相同严格目标匹配条件下仍有18条非目标命中，其中10条海胆参考与整对引物完全匹配。XS因此按固定候选报告，不计作通过S–XL的结构及非目标筛选。

[XS完整评价与证据](docs/XS.md) · [碱基表](results/xs/base_matching.csv) · [独立复核](results/xs/background_verification.json)

![XS base matching](figures/base_matching_XS.svg)

## S–XL的选择

每个长度的普通、A、B、D共享完全相同的正反向起止坐标。优先单对；A/B为分别PCR后的并集，双方均有独有覆盖或完全匹配贡献。D只保留单对。S、M、L、XL的D简并度分别为32/64、16/8、1/8、48/6，在匹配收益与组合复杂度间取舍。SD/MD的WC3及GT2门槛各20条，其余S–XL方案各5条；S–XL的所有展开序列通过末端及两种浓度热力学检查。

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

## 数据与复现

独立复核共918项目标判定、34项非目标集合检查，差异为0。XS另以不限150–500 bp的目标长度扫描确认主指标不变。设计与评价使用相同参考，尚无本项目新增湿实验验证；XS在同一25标签面板上的未观察共享条码标签比例为22/25（88%），与MD相同，不代表未知物种的鉴定成功率。

[Sequences](sequences/primer_pairs.csv) · [FASTA](sequences/primers.fasta) · [Results](results/comparison.csv) · [Base matching](results/base_matching.html) · [Methods](docs/METHODS.zh-CN.md) · [Reproduction](docs/REPRODUCIBILITY.zh-CN.md) · [Files](docs/FILES.md)

[Copyright / 著作权声明](COPYRIGHT.md)
