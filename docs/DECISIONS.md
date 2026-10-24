# Retention decisions / 保留决策

每个长度只保留一套D方案，固定普通/A/B/D共同坐标，普通单对不变，A/B已重新选配。扩大简并候选后，在覆盖与完全匹配不低于原D的方案中，优先选取接近最佳评分但简并度更低的候选；收益不足以抵偿复杂度时不追求最高评分。

Retain one D portfolio per length at the existing shared ordinary/A/B/D coordinates; ordinary single pairs remain unchanged; A/B have since been re-selected. Among candidates that do not reduce either coverage or exact matching relative to the original D, prefer lower degeneracy near the best combined score, rather than maximizing matching at any complexity.

S采用32/64，M采用16/8，L采用1/8，XL采用48/6。M舍弃仅多4个百分点完全匹配率的24/8档，XL舍弃仅多4个百分点完全匹配率的72/6档。

Retained F/R degeneracies: S 32/64, M 16/8, L 1/8, XL 48/6. Reject M 24/8 and XL 72/6 options that add only four percentage points of exact matching.

| D | F/R degeneracy | Coverage before → after % | Exact before → after % | WC≤3 | GT≤2 | WC≤4 |
|---|---|---|---|---:|---:|---:|
| SD | 32/64 | 72.00 → 88.00 | 46.00 → 66.00 | 0 | 12 | 15 |
| MD | 16/8 | 68.00 → 100.00 | 16.00 → 84.00 | 16 | 14 | 29 |
| LD | 1/8 | 88.00 → 88.00 | 30.00 → 38.00 | 0 | 0 | 0 |
| XLD | 48/6 | 88.00 → 96.00 | 62.00 → 66.00 | 3 | 3 | 121 |

This is a post-search benefit–complexity judgment, not a preregistered optimum. The near-best screen uses coverage+exact within five percentage points of the thermally feasible maximum; MiUrchin S additionally caps each direction at 64 variants. / 这是搜索后的收益与复杂度取舍，并非预注册最优阈值。

Current A/B selection / 当前A/B筛选：[expanded same-coordinate search and independent verification / 扩大同坐标搜索与独立复核](AB_COMPLEMENTARITY.md).
