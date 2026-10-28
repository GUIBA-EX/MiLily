# Methods

Reference coordinates use ungapped mitochondrial 16S rRNA of AF049132.1 (1-based). Within each S–XL window ordinary and degenerate primers share the forward and reverse endpoints.

The target library contains 269 records; quality and taxonomy review retains one reference per species, giving 128 species. S–XL each have 19 evaluable species; the remaining 109 lack the required sites. XS retains its original sequence and is assessed separately. The non-target library contains 7177 records. Primary coverage and exact-match metrics weight evaluable species equally; each order is also reported separately. Missing binding windows are not counted as failures.

Coverage requires at most two mismatches per primer with IUPAC-compatible final 3 nt. Exact matching requires zero mismatches at both primer sites. For S–XL, target scans require a 150–500 bp product and at least 50 bp between primer sites; background internal distance is 0–1,000 bp. Strict WC/GT preserve the terminal constraint; WC3/GT2 are permissive background screens. Counts refer to reference records.

D oligos have at most eight concrete variants with ambiguity confined to the 3′ half. Terminal checks exclude terminal homotriplets and homopolymers longer than four bases and require GC in the final 3 nt. Primer3 evaluates 50 mM monovalent salt, 1.5 mM Mg²⁺, 0.6 mM dNTP, 50 nM per variant and 200 nM per direction; structure Tm must be below 55°C and the forward/reverse duplex-Tm midpoint difference at most 5°C. XS is a fixed external candidate whose structure and non-target assessment is reported separately in [XS assessment](../results/xs/assessment.json).

Independent C++ and Python scans evaluate the same reference data; they are algorithmic verification, not independent biological validation. Computational predictions require experimental validation.
