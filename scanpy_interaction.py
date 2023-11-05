# for example there is a data loaded:
#>>> data
#AnnData object with n_obs × n_vars = 88374 × 18823
#    obs: 'Sample', 'Barcode', 'cell_type', 'sum', 'detected', 'subsets_Mt_sum', 'subsets_Mt_detected', 'subsets_Mt_percent', 'total', 'nCount_RNA', 'nFeature_RNA', 'RNA_snn_res.0.8', 'seurat_clusters', 'patient', 'sex', 'days', 'condition', 'doublet', 'ident'
#    uns: 'X_name'
#    obsm: 'MNN', 'UMAP'
#    layers: 'logcounts'

# to check the counts data matrix:
a = data.X[:10,:10]
a
#<10x10 sparse matrix of type '<class 'numpy.float32'>'
#        with 4 stored elements in Compressed Sparse Column format>
print(a)
#  (9, 1)        1.0
#  (2, 5)        1.0
#  (4, 5)        1.0
#  (5, 5)        1.0

# Similarly, to check the logcounts from layer:
a = data.layers['logcounts'][:10,:10]
a
#<10x10 sparse matrix of type '<class 'numpy.float64'>'
#        with 4 stored elements in Compressed Sparse Column format>
print(a)

# sometimes, the adata.X stored the scaled data, while the raw counts can be access by: 
print(adata.raw.X[:4,:4])

# Save Plot a name in a specified path.
# Traindata:
Test_INPUT_FILE = "/mnt/pixstor/dbllab/suli/Alg_development/use_geneformer/data/ms/ms_train/ms/ms_test.h5ad"
import scanpy as sc
test_ad = sc.read_h5ad(Test_INPUT_FILE)
sc.set_figure_params(format="png")
from matplotlib import pyplot as plt
sc.settings.vector_friendly = False
with plt.rc_context({"figure.figsize": (8, 8), "figure.dpi": (300)}):  # Use this to set figure params like size and dpi
    sc.pl.umap(test_ad, color="celltype", show=False)
    plt.savefig("/mnt/pixstor/dbllab/suli/Alg_development/use_geneformer/tem/test_ad.umap.png", bbox_inches="tight")

