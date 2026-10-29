![MiLily](figures/MiLily_overview_current.png)

# MiLily

[English](README.md)

## 摘要

线粒体 16S rRNA 环境 DNA 候选引物，包含 XS、S、M、L、XL。S–XL 各保留普通单对及简并单对 D，同长度共享参考坐标；XS 为固定单对。
每个物种保留一条参考序列；主指标对可评价物种等权，各目单列。
海百合参考面板为 128 个物种，但 S–XL 只有 19 个物种可评价；XS 为手动设计并独立评价。

S–XL 在 19 个物种上评价，手动设计的 XS 单独评价。当前 S–XL 面板中 SD 覆盖 17/19，MD 覆盖 19/19；仍需补充参考序列并进行实验验证。

五窗口共同面板包含19个物种。本轮增加统一分母比较、去引物条码唯一性与最近邻分析，以及属级条件性选配测试。正式引物序列保持不变。

## 引言

海百合环境 DNA 宏条形码分析需要参考序列同时覆盖目标类群和引物结合位点。MiLily 比较不同线粒体 16S 引物窗口，并纳入一对手动设计、使用独立参考面板评价的 XS 引物。 海洋环境 DNA 宏条形码研究显示，标记和参考数据库的选择会影响检测结果（Gold 等，2022）；MiFish 则提供了基于序列比对设计鱼类引物的实例（Miya 等，2015）。线粒体 16S 曾与其他分子标记共同用于海百合系统发育研究（Taylor 等，2023）。

[参考面板 / Reference panel](results/species_qc/panel.csv) · [参考序列审核 / Reference curation](results/species_qc/README.md)

![Reference binding positions](figures/amplicon_regions.zh.svg)

## 方法

### 参考数据与序列比对

目标数据库包含 269 条海百合线粒体序列，非目标数据库包含 7,177 条参考记录。经序列质量和分类审核，每个可确认物种保留一条代表，共 128 个物种。代表序列依据结合窗口完整性、模糊碱基和参考位点覆盖情况选择，不以引物匹配结果为筛选依据。保留序列使用 MAFFT 7.526（Katoh & Standley，2013）重新比对，参考坐标采用去除空位的线粒体 16S rRNA 序列 AF049132.1，从 1 开始计数。清理后的物种面板中，正、反向窗口均需跨越参考区域，A/C/G/T 数量达到参考位点数的 90% 且无模糊碱基，允许比对空位；符合条件的物种才纳入该窗口的评价分母。可评价物种数为 S–XL 各为 19 个。缺失窗口不计为漏检，筛选标准及 accession 记录见[参考序列审核](results/species_qc/README.md)。

### 引物设计与筛选

在固定的正、反向参考窗口内比较普通和简并候选。S–XL 每个长度的普通引物与 D 引物使用相同参考起止坐标。每条 D 引物最多包含 8 种具体序列，IUPAC 简并碱基限于 3′ 半段。末端筛查排除末端三连和超过 4 bp 的同聚物，要求末端 3 nt 至少含一个 G 或 C。Primer3（Untergasser 等，2012）计算采用单价盐 50 mM、Mg²⁺ 1.5 mM、dNTP 0.6 mM，分别评估每变体 50 nM 和每方向总浓度 200 nM 两种情景。S–XL 的结构筛查要求预测结构最高 Tm 低于 55 °C，正、反向双链 Tm 区间中点之差不超过 5 °C。XS 为手动设计的引物，使用原有的 27 条参考序列、25 个分类标签面板单独评价；其非目标和二级结构结果单独记录，不事后套用 S–XL 候选的筛选门槛。

### 计算评价

预测覆盖要求每条引物最多 2 个错配，且末端 3 nt 与模板按 IUPAC 规则兼容；完全匹配要求两个结合位点均无错配。S–XL 目标双引物扫描要求产物长 150–500 bp、双引物之间的内部长度至少 50 bp；非目标扫描允许内部距离 0–1,000 bp。严格 Watson–Crick（WC）和 G–T 模型保留末端约束；WC≤3 和 GT≤2 为不施加末端约束的宽松筛查。当前 S–XL 物种面板的覆盖率和完全匹配率对可评价物种等权，并分别汇总各目结果；非目标数字为参考记录数。使用 C++ 与 Python 对同一参考数据的目标及严格非目标命中集合进行独立算法复核。结果为计算兼容性预测。

### 共同面板、条码分辨率与属级留出测试

按accession对五个窗口取交集，得到19个共同物种，用于统一长度比较的分母；各窗口完整面板另报。条码提取自正反向结合窗口之间的同源比对列，去除空位并排除内部模糊碱基。唯一性相对于该窗口全部可用明确条码判断，包括共同面板以外的物种。单位代价Levenshtein编辑距离用于寻找最近的其他物种参考。这将引物兼容性与条码区分能力分开评价（Riaz等，2011）。

属级五折选配使用种子20261030；完整代表序列相同的跨属记录绑定成同一分组，避免重复序列泄漏。每折只用训练物种生成F/R，不以正式引物或全数据候选池为种子。确定性贪心搜索每端最多使用24个符合要求的高频普通序列种子，简并限于3′半段，每条≤8种变体，固定寡核苷酸长度，允许在既定结合区间附近±5个比对列内搜索。留出物种使用完整原始序列成对扫描，沿用各窗口的产物长度和错配规则。窗口发现早于划分，且折内候选未执行正式热力学/背景筛查，因此属于条件性序列选配测试，不是完整设计流程的外部独立验证；折内序列不纳入正式引物集。

手动XS保持原序列，另按已发布窗口完整性规则（跨越结合窗口、A/C/G/T支持≥90%、结合区无模糊碱基）建立128物种面板并重新扫描，用独立逐位算法核对成对命中。这是新增物种代表评价，与原27条参考/25标签评价分开。XS区域的折内选配仅作诊断，不修改或替换手动XS。

[分析方法与复现](results/computational_evaluation/README.zh-CN.md)

[详细方法](docs/METHODS.zh-CN.md) · [验证](docs/VALIDATION.md)

## 结果

### 预测表现

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

覆盖要求每条引物最多 2 个错配且末端 3 nt 兼容；完全匹配要求两条引物均无错配。严格 WC/GT 含末端约束；WC≤3 / GT≤2 为宽松非目标筛查。

D 引物每条最多 8 个具体变体，简并位点限于 3′ 半段。XS 是固定命名的特殊单对。计算预测仍需实验验证。

SD 在当前 19 个可评价物种中覆盖全部 17 个 Comatulida，但未覆盖 Cyrtocrinida 和 Isocrinida 的代表。XS 的结构与非目标评估见 [XS 评估](results/xs/assessment.json)。

### 共同物种面板比较

| Name | Coverage | Exact | Covered + identity-unique |
| --- | --- | --- | --- |
| XS | 19/19 | 18/19 | 16/19 |
| S | 14/19 | 6/19 | 12/19 |
| SD | 17/19 | 10/19 | 15/19 |
| M | 17/19 | 0/19 | 15/19 |
| MD | 19/19 | 7/19 | 17/19 |
| L | 17/19 | 6/19 | 15/19 |
| LD | 17/19 | 8/19 | 15/19 |
| XL | 12/19 | 0/19 | 10/19 |
| XLD | 18/19 | 2/19 | 16/19 |

此表全部引物使用相同19物种分母。末列为同时匹配引物且内部条码不与该窗口其他可用物种重复的物种数。缺失窗口不计为漏检。

![共同面板比较](results/computational_evaluation/figures/common_panel.svg)

### 去除引物后的条码分辨率

| Window | Unambiguous inserts | Identity-unique species | Insert length (bp) |
| --- | --- | --- | --- |
| XS | 128 | 120/128 | 123–158 |
| S | 19 | 17/19 | 157–164 |
| M | 19 | 17/19 | 201–212 |
| L | 19 | 17/19 | 248–257 |
| XL | 19 | 17/19 | 403–431 |

长度不含两端引物。唯一性描述每种一条代表的参考集合，不等同于种群范围的分辨率或实测鉴定准确率。跨物种同条码列为待核查参考冲突，需结合来源与分类解释。共同面板的唯一性仍对该窗口全部可用条码判断，因此共同子集内不重复的序列也可能在子集外有竞争条码。

![参考条码唯一性](results/computational_evaluation/figures/resolution.svg)

[同条码冲突](results/computational_evaluation/results/barcode_collisions.csv) · [最近邻编辑距离](results/computational_evaluation/results/nearest_neighbors.csv) · [剔除冲突记录的敏感性结果](results/computational_evaluation/results/conflict_exclusion_sensitivity.csv)

### 属级条件性留出测试

| Window | Held-out coverage | Held-out exact |
| --- | --- | --- |
| XS | 125/128 (97.66%) | 118/128 (92.19%) |
| S | 15/19 (78.95%) | 6/19 (31.58%) |
| M | 16/19 (84.21%) | 4/19 (21.05%) |
| L | 15/19 (78.95%) | 5/19 (26.32%) |
| XL | 15/19 (78.95%) | 1/19 (5.26%) |

此表汇总25组逐折训练选配候选的预测，不是正式普通/D引物的性能表。每个窗口内每种物种仅测试一次。折内候选未执行热力学与背景门槛，不能仅凭兼容性分数替换正式方案。逐折规模和逐物种预测均公开，以显示属间采样不均衡。

![属级条件性留出](results/computational_evaluation/figures/holdout.svg)

[逐折候选](results/computational_evaluation/results/cv_folds.csv) · [逐物种留出预测](results/computational_evaluation/results/cv_predictions.csv) · [共同/各自面板完整结果](results/computational_evaluation/results/panel_comparison.csv)

### 手动XS在新增物种面板上的表现

手动XS在128物种面板上预测覆盖127/128（99.22%），双端完全匹配114/128（89.06%）；共同19物种上覆盖19/19，完全匹配18/19。128条明确内部片段中120种条码唯一，119/128同时满足覆盖和条码唯一。这些目标端结果不改变原XS热力学/背景评估，也不表示其通过S–XL筛选门槛。序列和原面板碱基图均保留。

### XS

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XS | `TTGGGGCAACCDCGAAG` | `CAACATCGAGGTCGCAAAC` |

![XS base matching](figures/base_matching_XS.svg)

XS 图沿用其原参考面板。

### S

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| S | `GATCTAATGAAACCCCAA` | `TATCCCTTTTGGTTTAGC` |
| SD | `GATCTAATGAARYYCCAA` | `TATCCCTTTTRGTTTWGY` |

![S base matching](results/current_primers/S/base_matching_S.svg)

![SD base matching](results/current_primers/S/base_matching_SD.svg)

[S · 各目](results/current_primers/S/S_by_order.csv) · [各物种](results/current_primers/S/S_by_taxon.csv)

[SD · 各目](results/current_primers/S/SD_by_order.csv) · [各物种](results/current_primers/S/SD_by_taxon.csv)

### M

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| M | `TTACTGTTGCAAAAGTAAACTAAGAG` | `GGCTGTTTCTAGGCCTAC` |
| MD | `TTACTGTTGCAAAAGTAAAYWAAGAR` | `GGCTGCTTCTAGGCCTAC` |

![M base matching](results/current_primers/M/base_matching_M.svg)

![MD base matching](results/current_primers/M/base_matching_MD.svg)

[M · 各目](results/current_primers/M/M_by_order.csv) · [各物种](results/current_primers/M/M_by_taxon.csv)

[MD · 各目](results/current_primers/M/MD_by_order.csv) · [各物种](results/current_primers/M/MD_by_taxon.csv)

### L

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| L | `CAAGAGATCTAATGAAACCCCA` | `GGCTGCTTCTAGGCCTAC` |
| LD | `CAAGAGATCTAATGAARMCCCA` | `GGCTGCTTCTAGGCCTAC` |

![L base matching](results/current_primers/L/base_matching_L.svg)

![LD base matching](results/current_primers/L/base_matching_LD.svg)

[L · 各目](results/current_primers/L/L_by_order.csv) · [各物种](results/current_primers/L/L_by_taxon.csv)

[LD · 各目](results/current_primers/L/LD_by_order.csv) · [各物种](results/current_primers/L/LD_by_taxon.csv)

### XL

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XL | `AGGCAAGACGAAAGCTTAACTG` | `GACTTGCGTCGGTCTGAA` |
| XLD | `AGGCAAGACGAARRYTTAACTG` | `GACTTACGTCGGTCTGAA` |

![XL base matching](results/current_primers/XL/base_matching_XL.svg)

![XLD base matching](results/current_primers/XL/base_matching_XLD.svg)

[XL · 各目](results/current_primers/XL/XL_by_order.csv) · [各物种](results/current_primers/XL/XL_by_taxon.csv)

[XLD · 各目](results/current_primers/XL/XLD_by_order.csv) · [各物种](results/current_primers/XL/XLD_by_taxon.csv)

## 讨论

在清理后的 128 物种面板中，S–XL 的评价覆盖 19 个物种。SD 覆盖全部 17 个可评价的 Comatulida，但未覆盖所采样的 Cyrtocrinida 和 Isocrinida 代表。手动设计的 XS 使用另一套 27 条参考、25 个分类标签的面板评价，并存在预测二级结构和非目标匹配，因此应结合其面板与专门评估解释结果。进一步补充参考序列并进行实验验证，可更好地评价其在海百合中的表现。

[Copyright / 著作权](COPYRIGHT.md)

## 引用方式

使用本项目引物、参考数据或分析代码时，请引用：

Xia, F. (2026). *MiLily: candidate mitochondrial 16S rRNA primers for crinoid environmental DNA metabarcoding*. GitHub. https://github.com/GUIBA-EX/MiLily

[CITATION.cff](CITATION.cff) · [BibTeX](CITATION.bib)

## 参考文献

1. Gold, Z., Wall, A. R., Schweizer, T. M., et al. (2022). A manager’s guide to using eDNA metabarcoding in marine ecosystems. *PeerJ*, 10, e14071. https://doi.org/10.7717/peerj.14071

2. Miya, M., Sato, Y., Fukunaga, T., et al. (2015). MiFish, a set of universal PCR primers for metabarcoding environmental DNA from fishes: detection of more than 230 subtropical marine species. *Royal Society Open Science*, 2, 150088. https://doi.org/10.1098/rsos.150088

3. Taylor, K. H., Rouse, G. W., & Messing, C. G. (2023). Phylogeny and taxonomy of Himerometroidea (Echinodermata: Crinoidea). *Zootaxa*, 5277, 149–164. https://doi.org/10.11646/zootaxa.5277.1.7

4. Katoh, K., & Standley, D. M. (2013). MAFFT multiple sequence alignment software version 7: improvements in performance and usability. *Molecular Biology and Evolution*, 30, 772–780. https://doi.org/10.1093/molbev/mst010

5. Untergasser, A., Cutcutache, I., Koressaar, T., et al. (2012). Primer3—new capabilities and interfaces. *Nucleic Acids Research*, 40, e115. https://doi.org/10.1093/nar/gks596

6. Riaz, T., Shehzad, W., Viari, A., et al. (2011). ecoPrimers: inference of new DNA barcode markers from whole genome sequence analysis. *Nucleic Acids Research*, 39, e145. https://doi.org/10.1093/nar/gkr732
