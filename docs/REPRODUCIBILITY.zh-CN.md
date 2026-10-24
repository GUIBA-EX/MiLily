# Reproduction / 复现

Install the pinned dependencies in `requirements.txt`. XS and S–XL have distinct reproduction entry points. / 安装固定依赖后，XS与S–XL分别复核。

## XS

From the repository root, with a C++17 compiler available:

```sh
python scripts/verify_xs.py --output /tmp/milily-xs-check
```

The script compiles the shipped exhaustive scanner, scans the frozen target/background FASTA, calculates weighted panel metrics, compares local target windows and independent bit-parallel background sets, and checks the frozen XS assessment. It requires no network access. / 脚本编译随附扫描器，使用冻结参考核对目标指标及非目标集合，无需联网。

XS structure predictions are recorded for all three concrete F variants in `results/xs/thermal.json` and `results/xs/structures.json`. To repeat them with the same Primer3 dependency:

```sh
python scripts/xs_thermodynamics.py --output /tmp/milily-xs-thermal.json
```

## S–XL

Extract `reproduction_sources.zip` into a clean directory. The original `work/milily/selected.json` freezes the 16 S–XL pairs; `work/milily_xs/assessment.json` freezes XS separately. Re-run the per-project `verify.py`, `summarize.py` and figure scripts for S–XL. The earlier `choose_joint.py` produces a search baseline, not the later retention decisions. / 复现包内S–XL冻结16对，XS另存；早期选配程序并不直接重现后续保留决策。

The expanded A/B search sources retain the multi-project workspace layout; use the frozen release selection for a standalone audit. / 扩大A/B搜索保留多项目目录依赖，单项目复核使用冻结结果。

## Release checks / 发布检查

```sh
python scripts/check_release.py
python scripts/check_joint.py
python scripts/check_ab.py
```

These check 13 portfolios, 17 paired records, 34 oligos, exact S–XL coordinate equality and mutual A/B contributions, XS candidate status, raw-hit metrics, linked files, reproduction archive integrity and SHA-256 hashes. / 检查序列、坐标、A/B互补、XS状态、原始命中指标、链接、复现包及校验和。
