import GEOparse as gp

# acquire datasets
def geo_parse(dataset_id):
  gse = gp.GEOparse.get_GEO(dataset_id, destdir=snakemake.output[0])
  return gse

geo_parse(snakemake.params.dataset)

