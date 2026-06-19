import pandas as pd
import anndata as ad

# check if dataset has at least 200 cells per group
def check_cell_count(adata, groupby):
  if adata.obs[groupby].nunique() < 2:
    raise ValueError("Dataset must have at least 2 groups")
    return
  if adata.obs.groupby(groupby).size().min() < 200:
    raise ValueError("Dataset must have at least 200 cells per group")
    return
  dataset_to_h5ad(adata, snakemake.output[0])
  

# dataset conversion

def dataset_to_h5ad(input_file, output_file):
  # csv's or tsv's
  if input_file.endswith('.csv'):
    df = pd.read_csv(input_file)
  elif input_file.endswith('.tsv'):
    df = pd.read_csv(input_file, sep='\t')
  else:
    raise ValueError("Unsupported file format")
  print(df.head())

# create AnnData object
  adata = ad.AnnData(df)
  adata.write_h5ad(output_file)
  return adata

check_cell_count(snakemake.input[0], snakemake.params.groupby)