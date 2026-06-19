from fileinput import filename

import numpy as np
import anndata as ad
import pandas as pd

# acquire files
def acquire_dataset(import_path, output_path):
  # csv's or tsv's
  if import_path.endswith('.csv'):
    df = pd.read_csv(import_path)
  elif import_path.endswith('.tsv'):
    df = pd.read_csv(import_path, sep='\t')
  else:
    raise ValueError("Unsupported file format")
  
  # create AnnData object
  adata = ad.AnnData(df)
  adata.write_h5ad(filename, output_path)
  # saving metadata as a string
  obs = adata.obs.astype(str)