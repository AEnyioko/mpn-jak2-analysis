configfile: "config/local.yaml"

rule all:
    input:
        expand("data/processed/{dataset}.h5ad", dataset=config["datasets"])

rule acquire_datasets:
    params:
        dataset = lambda wildcards: wildcards.dataset
    log:
        "logs/acquire_{dataset}.log"
    output:
        "data/raw/{dataset}_family.soft"
    conda:
        "../envs/environment.yml"
    script:
        "../scripts/acquire.py"


# rule preprocess_datasets:
#     input:
#         "data/raw/{dataset}_family.soft"
#     output:
#         "data/processed/{dataset}.h5ad"
#     conda: 
#         "envs/environment.yml"
#     script:
#         "scripts/preprocess.py"