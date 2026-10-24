# MiLily

[English](README.md)

![Binding positions](figures/binding_positions.svg)

每个长度联合选择一个共同位点：普通、A、B、D的正反向起止坐标完全相同。位点内按覆盖率与完全匹配率之和选择普通单对、普通A/B并集和简并单对，三类评分等权平均选择位点。背景门槛为WC≤3及GT≤2各不超过5条记录。所有实际序列变体通过末端规则和两种浓度热力学检查。A/B指标为独立PCR并集，未验证混池；设计与评估共用参考数据，计算覆盖率不代表实测扩增效率。

D表示简并单对；无后缀为普通单对，A/B为同位点普通双对。每个项目12套方案、16对记录、32条序列。

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

宽松错配模型下的背景命中仍可能较高；完整结果和漏检记录见数据文件。

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
