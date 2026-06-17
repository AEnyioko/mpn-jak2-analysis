configfile: "config/local.yaml"

rule all:
    input:
        expand("data/processed/{dataset}.h5ad", dataset=config["datasets"])

rule acquire_datasets:
    output:
        "data/raw/{dataset}.h5ad"
    conda:
        "envs/environment.yml"
    script:
        "scripts/acquire.py"

rule preprocess_datasets:
    input:
        "data/raw/{dataset}.h5ad"
    output:
        "data/processed/{dataset}.h5ad"
    conda: 
        "envs/environment.yml"
    script:
        "scripts/preprocess.py"