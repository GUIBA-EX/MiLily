# MiLily, a set of universal PCR primers for metabarcoding environmental DNA from **sea lily**

[English](README.md)
[下载优化前英文 Method PDF（历史快照）](publications/MiLily_Method_ResearchGate.pdf)


![MiLily介绍图：XS、S、M、L、XL](figures/MiLily_overview_current.png)

圆标为AF049132.1上的含引物参考跨度：XS 179、S 193、M 248、L 288、XL 443 bp。XS在全目标参考扫描中的预测产物长度为159–194 bp，共同27条参考面板中的范围为178–194 bp。

## 摘要 / Abstract

MiLily是一套海百合类16S rRNA环境DNA候选引物，包含XS、S、M、L、XL五个窗口。主评价对四目等权，使用27条参考、25个分类标签及7,177条非目标记录。新SD、MD、LD、XLD的目间覆盖率分别为71.59%、100%、50%、75%，完全匹配率分别为43.18%、50%、14.77%、68.18%。四个D方案均为单对，并与各长度普通/A/B共享起止坐标。XS保留固定短片段方案；其非目标命中和结构预测单独报告。

## 引言 / Introduction

MiLily面向海百合类（Crinoidea，包括有柄海百合和海羽星）的线粒体16S rRNA宏条形码检测。现生海百合类包含以海羽星为主的Comatulida，以及Isocrinida、Hyocrinida和Cyrtocrinida等主要有柄类群。多基因与系统基因组研究显示，有柄和无柄体型的演化关系并非简单对应，形态相似性也不总能反映亲缘关系。[Rouse et al., 2013](https://doi.org/10.1016/j.ympev.2012.09.018)；[Rouse et al., 2026](https://doi.org/10.1098/rsos.251924)

Comatulidae的分子系统学与分类修订进一步表明，可靠鉴定需要结合形态、序列及更新后的分类名称。[Summers et al., 2014](https://doi.org/10.1016/j.ympev.2014.06.030)；[Summers et al., 2017](https://doi.org/10.11646/zootaxa.4268.2.1) 对MiLily而言，这些研究为按谱系组织参考序列、解释类群间匹配差异及维护物种标签提供了分类背景。

MiFish通过在保守区设置引物、扩增其间的短变异区，并以MiFish-E补充特定类群的结合位点变异，为广覆盖eDNA引物设计提供了参考。[Miya et al., 2015](https://doi.org/10.1098/rsos.150088)

短条形码研究表明，缩短扩增片段可提高降解DNA材料的可用性；不同短窗口保留的分类信息则需要分别评价。[Meusnier et al., 2008](https://doi.org/10.1186/1471-2164-9-214)；[Boyer et al., 2012](https://doi.org/10.1371/journal.pone.0038215) MiLily因此保留XS、S、M、L和XL五个窗口，将片段长度、目标覆盖、完全匹配和非目标命中纳入共同比较。

标记选择同时涉及分类覆盖与区分能力，ecoPrimers将这两个维度与片段长度、目标和非目标参考联合评价。[Riaz et al., 2011](https://doi.org/10.1093/nar/gkr732) MiLily沿用这一比较思路，在每个S–XL窗口内固定结合坐标，评价普通单对、互补A/B双对和简并D单对，以较少的引物组合覆盖主要序列变异。

## 方法 / Methods

### 参考数据与评价指标

参考坐标采用AF049132.1提取的无gap 16S序列，按1起算。该参考来自*Florometra serratissima*；其完整线粒体基因组及基因排列由Scouras与Smith报道。[Scouras & Smith, 2001](https://doi.org/10.1093/oxfordjournals.molbev.a003720) 目标FASTA含269条记录；主比较采用冻结共同面板，按目间等权评价；旧标签内参考加权值保留为次要指标。

覆盖要求两条引物各≤2个错配且各自末端3 nt满足IUPAC兼容；完全匹配要求两端均无错配。非目标库含7,177条记录。WC3、GT2、WC4分别统计每条≤3错配、允许G–T配对每条≤2错配、每条≤4错配的成对命中；这些宽松模型不强制末端3 nt兼容。严格非目标匹配另采用目标覆盖标准。非目标命中以参考记录数报告。

### 候选设计与复核

S–XL每个长度的普通、A、B、D共享正反向起止坐标。优先单对；A/B表示分别PCR后取并集，保留时要求双方均有独有覆盖或完全匹配贡献。D只保留单对。XS按给定序列独立评价。

末端检查要求无末端三连、末端3 nt至少一个GC、末端5 nt含1–4个GC、连续同聚物不超过4；允许3′简并。双链、发卡和二聚体热力学使用Primer3计算。[Untergasser et al., 2012](https://doi.org/10.1093/nar/gks596) 参数采用50 mM单价盐、1.5 mM Mg²⁺、0.6 mM dNTP，分别检查每变体50 nM及每方向总量200 nM。S–XL要求结构Tm<55°C，F/R双链Tm范围中点差≤5°C。本轮D的WC3/GT2各≤100条、严格WC/GT各≤20条，每方向简并度≤128；普通/A/B保留原有门槛。XS作为固定序列方案单独评价。

全序列双链扫描检查成对方向及距离，并以独立算法复核。完整参数和复现入口见[方法](docs/METHODS.zh-CN.md)与[复现说明](docs/REPRODUCIBILITY.zh-CN.md)。

## 结果 / Results

### 窗口与匹配表现

![Binding positions](figures/binding_positions.svg)

主指标按四目等权：每目先计算有至少一条参考命中的分类标签比例，再取均值。共同面板27条参考、25个标签，Comatulida 22个，其余三目各1个；不是完整物种名录。完全匹配采用同一层级。

| Scheme | Order coverage % | Order exact % | WC≤3 | GT≤2 |
|---|---:|---:|---:|---:|
| XS | 100.00 | 98.86 | 4196 | 3889 |
| SD | 71.59 | 43.18 | 4 | 7 |
| S | 19.32 | 7.95 | 0 | 0 |
| SA+SB | 19.32 | 13.64 | 0 | 0 |
| MD | 100.00 | 50.00 | 26 | 23 |
| M | 48.86 | 0.00 | 4 | 1 |
| MA+MB | 48.86 | 5.68 | 4 | 0 |
| LD | 50.00 | 14.77 | 0 | 0 |
| L | 25.00 | 9.09 | 0 | 0 |
| LA+LB | 25.00 | 13.64 | 0 | 0 |
| XLD | 75.00 | 68.18 | 8 | 3 |
| XL | 67.05 | 2.27 | 0 | 0 |
| XLA+XLB | 69.32 | 5.68 | 0 | 0 |

[D优化与类群增减 / D optimization and label changes](docs/D_OPTIMIZATION.md)

以下为旧口径的标签内参考加权指标，仅作次要比较。

| Scheme | Coverage % | Exact % | WC≤3 | GT≤2 | WC≤4 |
|---|---:|---:|---:|---:|---:|
| XS | 100.00 | 96.00 | 4196 | 3889 | 4405 |
| SD | 84.00 | 66.00 | 4 | 7 | 151 |
| S | 66.00 | 28.00 | 0 | 0 | 0 |
| SA+SB | 66.00 | 46.00 | 0 | 0 | 0 |
| MD | 100.00 | 92.00 | 26 | 23 | 47 |
| M | 88.00 | 0.00 | 4 | 1 | 11 |
| MA+MB | 88.00 | 20.00 | 4 | 0 | 14 |
| LD | 92.00 | 50.00 | 0 | 0 | 0 |
| L | 88.00 | 30.00 | 0 | 0 | 0 |
| LA+LB | 88.00 | 46.00 | 0 | 0 | 0 |
| XLD | 96.00 | 70.00 | 8 | 3 | 163 |
| XL | 68.00 | 8.00 | 0 | 0 | 6 |
| XLA+XLB | 76.00 | 18.00 | 0 | 0 | 6 |

独立复核覆盖918项目标判定和34项非目标集合检查，差异为0。XS扩大目标产物长度扫描范围后主指标不变。现有版本包含13套方案、17对记录和34条引物序列。

[Retention decisions / 保留决策](docs/DECISIONS.md) · [A/B complementarity / 互补性](docs/AB_COMPLEMENTARITY.md)

### 引物性能比较

![图1：目标覆盖率与完全匹配率](figures/performance_matching.svg)

**图1｜目标匹配。** 浅色条为覆盖率，深色条为完全匹配率；右侧标注依次为两项百分比。全部方案使用同一27条参考、25个标签面板，按四目等权计算。A/B表示分别PCR后取并集。

![图2：非目标匹配](figures/performance_background.svg)

**图2｜非目标匹配。** A：XS及S–XL简并单对的严格与完全匹配非目标记录数，标注为“严格 / 完全”。严格条件为两端各≤2错配且末端3 nt兼容。B：全部方案的WC3、GT2、WC4宽松成对命中，使用可显示零值的symlog横轴；右侧依次列出三种计数。背景库共7,177条记录。

![图3：产物长度与简并度](figures/performance_design.svg)

**图3｜长度与合成复杂度。** A：XS及S–XL简并单对在全目标参考扫描中的预测产物范围，均含引物；菱形为AF049132.1参考跨度。B：每条引物展开后的具体序列数，深色为F，浅色为R。

### XS

XS保留为短片段实验候选（本节原始评价使用参考加权口径）：一对引物，F/R简并度3/1，全目标参考扫描的预测产物159–194 bp（共同面板为178–194 bp）；在参考AF049132.1上的含引物跨度179 bp。F中的D=A/G/T，名称使用XS。

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XS | `TTGGGGCAACCDCGAAG` | `CAACATCGAGGTCGCAAAC` |

XS末端规则通过，双链Tm配对合适；F三个变体预测内部短发卡Tm为62.6–69.4°C，超过S–XL设计采用的55°C结构门槛，3′端不在该茎内。XS在相同严格目标匹配条件下仍有18条非目标命中，其中10条海胆参考与整对引物完全匹配。在57°C时，其内部短发卡预测ΔG约为−0.35至−0.65 kcal/mol。

[XS完整评价与证据](docs/XS.md) · [碱基表](results/xs/base_matching.csv) · [独立复核](results/xs/background_verification.json)

![XS base matching](figures/base_matching_XS.svg)

### S

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| SD | `GATCTAMTRMWAYYCCRA` | `TRTCCCTKTTRRTYTWRC` |
| S | `GATCTAATGAAACCCCAA` | `TATCCCTTTTGGTTTAGC` |
| SA | `GATCTAATGAAACCCCAA` | `TATCCCTTTTGGTTTAGC` |
| SB | `GATCTAATGAAACCCCAA` | `TGTCCCTTTTGGTTTAGC` |

![SD base matching](figures/base_matching_SD.svg)

![S base matching](figures/base_matching_S.svg)

![SA base matching](figures/base_matching_SA.svg)

![SB base matching](figures/base_matching_SB.svg)

### M

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| MD | `TYACTGTTDCAAAAGTRAAYWAAGAR` | `GRCTGCTTYTRGGCCTAC` |
| M | `TTACTGTTGCAAAAGTAAACTAAGAG` | `GGCTGTTTCTAGGCCTAC` |
| MA | `TTACTGTTACAAAAGTAAACTAAGAG` | `GGCTGCTTCTAGGCCTAC` |
| MB | `TTACTGTTGCAAAAGTAAACTAAGAG` | `GACTGCTTCTAGGCCTAC` |

![MD base matching](figures/base_matching_MD.svg)

![M base matching](figures/base_matching_M.svg)

![MA base matching](figures/base_matching_MA.svg)

![MB base matching](figures/base_matching_MB.svg)

### L

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| LD | `YARGAGATCTAATGAWAYYCCA` | `GRCTGCTTYTRGGCCTAC` |
| L | `CAAGAGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` |
| LA | `CAAGAGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` |
| LB | `CAAGGGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` |

![LD base matching](figures/base_matching_LD.svg)

![L base matching](figures/base_matching_L.svg)

![LA base matching](figures/base_matching_LA.svg)

![LB base matching](figures/base_matching_LB.svg)

### XL

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XLD | `AGGCAAVACGARRRCTHAACTG` | `GACTYDCGTCGGTCTGAA` |
| XL | `AGGCAAGACGAAAGCTTAACTG` | `GACTTGCGTCGGTCTGAA` |
| XLA | `AGGCAACACGAAAACTTAACTG` | `GACTTGCGTCGGTCTGAA` |
| XLB | `AGGCAAGACGAAAGCTTAACTG` | `GACTTGCGTCGGTCTGAA` |

![XLD base matching](figures/base_matching_XLD.svg)

![XL base matching](figures/base_matching_XL.svg)

![XLA base matching](figures/base_matching_XLA.svg)

![XLB base matching](figures/base_matching_XLB.svg)

## 讨论 / Discussion

XS以3/1的F/R简并度获得100%目间覆盖率和98.86%目间完全匹配率，适合优先开展短片段扩增试验。MD同样覆盖全部共同面板，宽松非目标命中较少。两者提供不同取舍：XS侧重短片段和低简并，MD侧重目标覆盖与背景区分。XS的18条严格非目标命中中，10条海胆记录与整对引物完全匹配，且预测产物长度与海百合重叠，适合在混合样中重点考察海胆DNA的竞争扩增。

MiFish通过补充结合位点变体提高特定类群的检测范围，这一思路也适用于MiLily的互补组合。[Miya et al., 2015](https://doi.org/10.1098/rsos.150088) 本项目的S、M、L双对主要增加完全匹配，XL双对同时增加覆盖；组合选择依据双方的独有贡献。普通、A、B、D保持相同坐标，使同窗口的比较集中于结合位点序列差异。

XS在共同面板上有22/25个分类标签未观察到共享条码（88%），与优化前MD相同。短标记的区分能力取决于窗口所含的变异，因此应联合考虑长度与条码信息，而非仅按片段长短排序。[Boyer et al., 2012](https://doi.org/10.1371/journal.pone.0038215) 当前结果来自共同参考面板的计算评价；后续将以组织DNA、已知组成混合样及环境样本比较扩增效率与检出组成。混合样实验尤其需要控制输入量：已有宏条形码实验发现，相近生物量的不同类群仍可产生显著不同的读数。[Elbrecht & Leese, 2015](https://doi.org/10.1371/journal.pone.0130324)

海百合参考库的扩展应同时考虑谱系代表性与名称核对。Comatulidae的整合分类研究观察到，外形差异与COI分化程度之间并非固定对应关系。[Summers et al., 2017](https://doi.org/10.11646/zootaxa.4268.2.1) 据此，MiLily后续应优先补充有凭证标本、形态鉴定及可追溯序列的参考，并结合系统基因组框架安排主要谱系的验证样本。[Rouse et al., 2026](https://doi.org/10.1098/rsos.251924)

## 合作邀请 / Collaboration

欢迎任何对海百合多样性、eDNA监测、引物设计和参考数据库建设感兴趣的研究者参与MiLily，**尤其欢迎有兴趣开展湿实验验证（wet-lab validation）的合作者**。

可合作的工作包括组织DNA扩增、已知组成混合样与环境样本测试、退火条件优化，以及不同引物方案的扩增效率、类群检出和非目标共扩增比较。也欢迎提供带有标本信息和鉴定记录的参考序列、实验反馈或分析建议。

有意合作请发送邮件至[1738314330@edu.k.u-tokyo.ac.jp](mailto:1738314330@edu.k.u-tokyo.ac.jp)，简要介绍研究方向、可用材料和希望开展的工作，共同讨论实验设计与分工。

## 数据与代码 / Data and code

[Sequences](sequences/primer_pairs.csv) · [FASTA](sequences/primers.fasta) · [Results](results/comparison.csv) · [Base matching](results/base_matching.html) · [Methods](docs/METHODS.zh-CN.md) · [Reproduction](docs/REPRODUCIBILITY.zh-CN.md) · [Files](docs/FILES.md)

性能图由[scripts/plot_performance.py](scripts/plot_performance.py)根据已发布CSV结果生成；安装Matplotlib后运行 `python scripts/plot_performance.py`，输出SVG及PNG。

[Copyright / 著作权声明](COPYRIGHT.md)

## 参考文献 / References

1. Miya, M., et al. (2015). MiFish, a set of universal PCR primers for metabarcoding environmental DNA from fishes: detection of more than 230 subtropical marine species. *Royal Society Open Science*, **2**, 150088. [doi:10.1098/rsos.150088](https://doi.org/10.1098/rsos.150088).
2. Meusnier, I., et al. (2008). A universal DNA mini-barcode for biodiversity analysis. *BMC Genomics*, **9**, 214. [doi:10.1186/1471-2164-9-214](https://doi.org/10.1186/1471-2164-9-214).
3. Riaz, T., et al. (2011). ecoPrimers: inference of new DNA barcode markers from whole genome sequence analysis. *Nucleic Acids Research*, **39**, e145. [doi:10.1093/nar/gkr732](https://doi.org/10.1093/nar/gkr732).
4. Untergasser, A., et al. (2012). Primer3—new capabilities and interfaces. *Nucleic Acids Research*, **40**, e115. [doi:10.1093/nar/gks596](https://doi.org/10.1093/nar/gks596).
5. Boyer, S., et al. (2012). Sliding window analyses for optimal selection of mini-barcodes, and application to 454-pyrosequencing for specimen identification from degraded DNA. *PLOS ONE*, **7**, e38215. [doi:10.1371/journal.pone.0038215](https://doi.org/10.1371/journal.pone.0038215).
6. Elbrecht, V., & Leese, F. (2015). Can DNA-based ecosystem assessments quantify species abundance? Testing primer bias and biomass–sequence relationships with an innovative metabarcoding protocol. *PLOS ONE*, **10**, e0130324. [doi:10.1371/journal.pone.0130324](https://doi.org/10.1371/journal.pone.0130324).
7. Scouras, A., & Smith, M. J. (2001). A novel mitochondrial gene order in the crinoid echinoderm *Florometra serratissima*. *Molecular Biology and Evolution*, **18**, 61–73. [doi:10.1093/oxfordjournals.molbev.a003720](https://doi.org/10.1093/oxfordjournals.molbev.a003720).
8. Rouse, G. W., et al. (2013). Fixed, free, and fixed: the fickle phylogeny of extant Crinoidea (Echinodermata) and their Permian–Triassic origin. *Molecular Phylogenetics and Evolution*, **66**, 161–181. [doi:10.1016/j.ympev.2012.09.018](https://doi.org/10.1016/j.ympev.2012.09.018).
9. Summers, M. M., Messing, C. G., & Rouse, G. W. (2014). Phylogeny of Comatulidae (Echinodermata: Crinoidea: Comatulida): a new classification and an assessment of morphological characters for crinoid taxonomy. *Molecular Phylogenetics and Evolution*, **80**, 319–339. [doi:10.1016/j.ympev.2014.06.030](https://doi.org/10.1016/j.ympev.2014.06.030).
10. Summers, M. M., Messing, C. G., & Rouse, G. W. (2017). The genera and species of Comatulidae (Comatulida: Crinoidea): taxonomic revisions and a molecular and morphological guide. *Zootaxa*, **4268**(2), 151–190. [doi:10.11646/zootaxa.4268.2.1](https://doi.org/10.11646/zootaxa.4268.2.1).
11. Rouse, G. W., et al. (2026). Phylogenomics of extant Crinoidea (Echinodermata) reveals extensive morphological homoplasies and a Permian origin. *Royal Society Open Science*, **13**, 251924. [doi:10.1098/rsos.251924](https://doi.org/10.1098/rsos.251924).
