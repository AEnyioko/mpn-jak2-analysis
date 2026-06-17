
# How Co-occurring Mutations Modify the Transcriptional Consequences of JAK2 V617F in Different MPN Phenotypes

**Author:** Chibuzor Anthony Enyioko

**Program:** MS Biomedical Informatics, UTHealth (exp. 2027)

**Status:** Pre-project dataset audit in progress

---

## Project Overview

Myeloproliferative neoplasms (MPNs) are clonal hematopoietic stem cell disorders driven primarily by the JAK2 V617F mutation, which is present in 95% of polycythemia vera (PV) and 50–60% of essential thrombocythemia (ET) and primary myelofibrosis (PMF) cases (Szybinski & Meyer, 2021). Despite sharing the same driver mutation, patients exhibit distinct clinical phenotypes depending on the co-occurrence of epigenetic regulators such as TET2, DNMT3A, and ASXL1.

This project uses publicly available single-cell RNA-seq datasets to characterize how these co-mutations modify JAK2 V617F transcriptional output and bias progenitor differentiation trajectories across MPN phenotypes, without requiring new data generation.

---

## Central Hypothesis

JAK2 V617F co-occurring with TET2, DNMT3A, or ASXL1 produces distinct differentiation trajectories compared to JAK2 V617F alone, such that each co-mutation specifically biases progenitor cells toward distinct endpoints consistent with the observed MPN phenotype:

* **JAK2+TET2:** progenitor expansion with delayed commitment at the myeloid-erythroid progenitor (MEP) bifurcation point (Rasmussen et al., 2019; Psaila et al., 2020)
* **JAK2+ASXL1: **myeloid-skewed trajectory consistent with PMF, via disruption of Polycomb repressive complex 2 (Bader & Meyer, 2022)
* **DNMT3A:** treated as a covariate modifier, not a standalone contrast group, following Challen et al. (2012)

---

## Aims

### Aim 1 — Harmonized Multi-omic MPN Reference Dataset

Construct a harmonized MPN single-cell reference dataset from public repositories (GEO, EGA) and define genotype-stratified transcriptional signatures.

**Output:** `results/aim1/mpn_harmonized_annotated.h5ad` — the pipeline boundary file gating all Aim 2 analyses.

### Aim 2 — Co-mutation-Specific Differentiation Trajectory Inference

Using the Aim 1 harmonized dataset, infer how each co-mutation biases progenitor differentiation trajectories using diffusion pseudotime (Haghverdi et al., 2016) and RNA velocity (La Manno et al., 2018).

**Output:** `results/aim2/mpn_pseudotime.h5ad` + trajectory figures + DNMT3A covariate model output.

---

## Quickstart

### 1. Clone the repository

bash

```bash
git clone https://github.com/cenyioko/mpn-jak2-comutation.git
cd mpn-jak2-comutation
```

### 2. Set up environments

bash

```bash
conda env create -f envs/environment.yml
conda env create -f envs/r_environment.yml
```

### 3. Configure credentials

bash

```bash
cp .env.example .env
# Add your EGA credentials to .env — this file is gitignored
```

### 4. Run locally (development)

bash

```bash
snakemake --configfile config/local.yaml --cores 4
```

---
## Repository Structure
```
mpn-jak2-comutation/
│
├── config/
│   ├── local.yaml              # Local desktop paths and thresholds
│   
│
├── profiles/
│   └── slurm/                  # Snakemake SLURM cluster profile
│
├── rules/
│   ├── acquire.smk             # Data download from GEO/EGA
│   ├── qc.smk                  # QC, doublet removal, preflight check
│   ├── aim1.smk                # scVI integration, annotation, DE, cNMF
│   └── aim2.smk                # Pseudotime, RNA velocity, DNMT3A covariate
│
├── scripts/
│   ├── acquire.py              # GEO/EGA download logic
│   ├── qc.py                   # Scanpy QC + Scrublet
│   ├── preflight_check.py      # Cell count validation per genotype group
│   ├── integrate.py            # scVI batch correction
│   ├── annotate.py             # CellTypist cell type annotation
│   ├── de_analysis.py          # pyDESeq2 + MAST + cNMF
│   ├── pseudotime.py           # Diffusion pseudotime
│   ├── rna_velocity.py         # scVelo RNA velocity
│   ├── dnmt3a_covariate.py     # DNMT3A covariate model
│   └── report.py               # Quarto report generation
│
├── envs/
│   ├── environment.yml         # Python conda environment (pinned)
│   ├── environment.lock        # Full resolved dependency tree
│   └── r_environment.yml       # R conda environment for MAST
│
├── results/
│   ├── aim1/                   # Harmonized .h5ad + DE outputs
│   ├── aim2/                   # Trajectory outputs + figures
│   └── report/                 # HTML report (mpn_analysis_report.html)
│
├── Snakefile                   # Master workflow (imports all rules/)
├── .env                        # EGA credentials — gitignored
├── .gitignore
└── README.md
```
---
## Data
### Data Requirements
|Requirement|Value|
|-----|-----|
|Minimum format|Raw counts only|
|Cell count minimum|200 cells per genotype group for primary trajectory result|
### Data Availability
|Asset|Location|
|-----|-----|
|Raw public MPN datasets|GEO / EGA databases, listed in [config/local.yaml](https://github.com/AEnyioko/MPNDataset/blob/main/config/local.yaml )|
|Processed .h5ad outputs|TBD|
|Analysis code|[Current repository](https://github.com/AEnyioko/MPNDataset)|
---
## Validation Plan
1. Held-out cohort replication: Genotype × phenotype signatures tested on an independent dataset not used in harmonization
2. Literature benchmarking: Trajectory predictions compared against Psaila et al. (2020) MEP bifurcation findings and Rasmussen et al. (2019) TET2 enhancer data
3. Sensitivity analysis: Pipeline rerun at two alternative values for minimum gene count threshold and doublet score threshold; genotype group cell counts verified above 200-cell minimum at each threshold

## References

Bader, M. S., & Meyer, S. C. (2022). JAK2 in myeloproliferative neoplasms: Still a protagonist.  *Pharmaceuticals, 15* (2), 160.

Challen, G. A., et al. (2012). Dnmt3a is essential for hematopoietic stem cell differentiation.  *Nature Genetics, 44* (1), 23–31.

Haghverdi, L., et al. (2016). Diffusion pseudotime robustly reconstructs lineage branching.  *Nature Methods, 13* (10), 845–848.

La Manno, G., et al. (2018). RNA velocity of single cells.  *Nature, 560* (7719), 494–498.

Psaila, B., et al. (2020). Single-cell analyses reveal megakaryocyte-biased hematopoiesis in myelofibrosis and identify mutant clone-specific targets.  *Molecular Cell, 78* (3), 477–492.

Rasmussen, K. D., et al. (2019). TET2 binding to enhancers facilitates transcription factor recruitment in hematopoietic cells.  *Genome Research, 29* (4), 564–575.

Szybinski, J., & Meyer, S. C. (2021). Genetics of myeloproliferative neoplasms.  *Hematology/Oncology Clinics of North America, 35* (2), 217–236.

Velten, L., et al. (2017). Human haematopoietic stem cell lineage commitment is a continuous process.  *Nature Cell Biology, 19* (4), 271–281.
