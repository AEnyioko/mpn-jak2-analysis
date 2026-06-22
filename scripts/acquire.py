import GEOparse as gp
import gzip as gz
import os

# acquire datasets
def geo_parse(dataset_id):
  gse = gp.GEOparse.get_GEO(dataset_id, destdir="data/raw/")
  with gz.open(snakemake.output[0] + '.gz', 'rb') as f_in:
    with open(snakemake.output[0], 'wb') as f_out:
      f_out.write(f_in.read())
  # Remove the compressed file
  try:
    os.remove(snakemake.output[0] + '.gz')
  except OSError:
    pass

  return gse

geo_parse(snakemake.params.dataset)

