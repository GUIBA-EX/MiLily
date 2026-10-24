# Reproduction / 复现

Extract `reproduction_sources.zip` into a fresh folder. Install Python 3.12 requirements, MAFFT 7 and a C++17 compiler. Candidate selection can be replayed from the frozen background-site file and oligo list:

```sh
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 python work/milily/optimize.py
c++ -O3 -std=c++17 work/micucumber_nondegenerate/independent_scan.cpp -o work/micucumber_nondegenerate/independent_scan
python work/milily/verify.py
python work/milily/summarize.py
python work/milily/extra_audit.py
python work/milily/same_locus_audit.py
python work/milily/figures.py
```

Results are written to `work/milily/release`. To repeat upstream discovery, run `discover.py`, compile `scan_sites.cpp`, then run the scanner with `work/milily/sites` as its argument before optimization. All supplied input FASTAs are frozen; no network retrieval is needed. Source inputs, weights and search constraints are described in METHODS.md.

解包后从冻结候选与背景位点重算选择，随后进行独立全序列扫描、末端检查与图件生成。`prepare.py`保留原始提取逻辑及来源路径，仅供追溯；复现直接使用随包提供的FASTA，不依赖原项目目录。

The frozen `fixed_single_pairs.json` preserves the eight single-pair portfolios while A/B is reselected under identical-coordinate constraints. / 冻结单对文件保留8套单对方案，A/B在完全相同坐标约束下重新选择。

Fresh-directory rerun of the same-locus selection reproduced identical records. / 新目录重跑同位点选择，结果完全一致。
