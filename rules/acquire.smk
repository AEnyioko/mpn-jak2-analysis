rule acquire_datasets:
    input:
        config/local.yaml
        datasets: config/local.yaml
        dataset=expand("{dataset}", dataset=config["datasets"])
    output:
        "data/raw/{dataset}.h5ad"
    script:
        "scripts/acquire.py"

rule preprocess_datasets:
    input:
        "data/raw/{dataset}.h5ad"
    output:
        "data/processed/{dataset}.h5ad"
    script:
        "scripts/preprocess.py"