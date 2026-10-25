# 方法

MiLily包括一个固定XS候选和S、M、L、XL四个按共同坐标设计的窗口。XS原序列固定纳入并单独报告结构与非目标筛查结果；S–XL沿用受约束搜索。

参考坐标为Florometra serratissima的AF049132.1，使用提取、去gap的16S序列，1-based计数。冻结评价面板包含27条记录、25个分类标签，四目等权；标签内任一参考命中即算检出，旧参考加权值作次要比较；目标FASTA含269条记录，非目标库含7,177条非海百合记录。不同窗口的参考完整度不同，主表统一使用冻结面板。

覆盖要求两条引物各不超过2个错配且末端3 nt按IUPAC兼容；完全匹配要求两端无错配。非目标WC3允许每条最多3错配，GT2允许G–T配对且每条最多2错配；WC4仅用于更宽松的敏感性检查。XS另报告与目标覆盖判据相同的严格非目标命中。所有非目标数值均为数据库记录数，不是环境样本中的扩增比例。

S–XL每个长度的普通、A、B、D起止坐标完全一致。A/B为分别PCR后取并集，双方须各有独有覆盖或完全匹配贡献。搜索纳入观测单倍型、具体展开序列和受支持的碱基替换；当前扩大A/B搜索见[互补性分析](AB_COMPLEMENTARITY.md)。D方案在覆盖、完全匹配和复杂度间取舍，见[保留决策](DECISIONS.md)。当前D的宽松WC3/GT2各≤100条、严格WC/GT各≤20条；普通/A/B保留原有门槛。

末端规则：无末端三连碱基，末端3 nt至少1个GC，末端5 nt含1–4个GC，无超过4个碱基的同聚物；允许3′简并。Primer3参数为单价盐50 mM、Mg²⁺ 1.5 mM、dNTP 0.6 mM，分别计算每变体50 nM与每方向总计200 nM两种浓度。S–XL要求结构Tm低于55°C、正反向双链Tm范围中点差不超过5°C。XS通过末端和双链Tm配对检查，但超过结构及非目标筛选门槛，详见[XS评价](XS.md)及温度相关ΔG记录。

独立C++穷举扫描核查正反两链、配对方向和扩增距离。XS额外使用同源位置附近±5 nt窗口预测目标状态，并用独立Python位并行替换匹配核对非目标集合。全发布共918项目标判定与34项非目标集合检查，差异均为0。将XS目标产物长度范围扩大至1–5,000 bp后，主指标不变。这些是相同参考数据上的独立算法复核，尚不构成独立生物学验证。

## 目间等权D优化 / Order-balanced D optimization

主指标、候选门槛、分类映射、逐类群增减和独立复核以[D优化](D_OPTIMIZATION.md)为准。当前D由2,360组同坐标组合筛选；普通/A/B与XS未改变。/ Current D selection uses 2,360 same-coordinate pairs, equal order weighting and explicit label safeguards, as documented in [D optimization](D_OPTIMIZATION.md). Ordinary/A/B and XS remain unchanged.
