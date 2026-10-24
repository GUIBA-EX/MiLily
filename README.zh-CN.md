![MiLily](figures/MiLily_overview_current.png)

# MiLily

[English](README.md)

![Binding positions](figures/binding_positions.svg)

每个长度联合选择一个共同位点：普通、A、B、D的正反向起止坐标完全相同。位点内按覆盖率与完全匹配率之和选择普通单对、普通A/B并集和简并单对，三类评分等权平均选择位点。背景门槛：MiLily的SD/MD各20条，MiUrchin的XLD各50条，其余方案各5条，均分别应用于WC≤3和GT≤2。所有实际序列变体通过末端规则和两种浓度热力学检查。A/B指标为独立PCR并集，未验证混池；设计与评估共用参考数据，计算覆盖率不代表实测扩增效率。

D表示简并单对；无后缀为普通单对，A/B为同位点普通双对。每个项目12套方案、16对记录、32条序列。

## 保留理由

每个长度只保留一套D方案，固定普通/A/B/D共同坐标，本次A/B重选保留普通单对与D不变。扩大简并候选后，在覆盖与完全匹配不低于原D的方案中，优先选取接近最佳评分但简并度更低的候选；收益不足以抵偿复杂度时不追求最高评分。

S采用32/64，M采用16/8，L采用1/8，XL采用48/6。M舍弃仅多4个百分点完全匹配率的24/8档，XL舍弃仅多4个百分点完全匹配率的72/6档。

[完整比较 / Full comparison](docs/DECISIONS.md)

| Scheme | Coverage % | Exact % | WC≤3 | GT≤2 | WC≤4 |
|---|---:|---:|---:|---:|---:|
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

宽松错配模型下的背景命中仍可能较高；完整结果和漏检记录见数据文件。

[Sequences](sequences/primer_pairs.csv) · [FASTA](sequences/primers.fasta) · [Results](results/comparison.csv) · [Verification](results/verification.json) · [Full base matching](results/base_matching.html)

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

Independent target checks: 864; disagreements: 0. Background set checks: 32; disagreements: 0.

[Copyright / 著作权声明](COPYRIGHT.md)


扩大同坐标搜索后，各长度A/B均有双方独有贡献；两项并集指标均不低于此前方案。普通单对和D保持不变。依据样本目标选择单对或互补双对。[互补性与独有命中](docs/AB_COMPLEMENTARITY.md)
