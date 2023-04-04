
# =============================================================== # 
# TSNE
# =============================================================== # 

#Load the necessary libraries
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Load your data into a numpy array
data = np.load('your_data.npy')

#Initialize a t-SNE object and fit it to your data
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200)
embedded_data = tsne.fit_transform(data)

#"""The n_components parameter specifies the number of dimensions in the embedded space. Since we want to visualize our data in 2D, we set n_components=2.

#The perplexity parameter controls the balance between local and global aspects of the data. A higher perplexity value tends to preserve global structure, while a lower value focuses more on local structure. You may need to experiment with different values to find the best one for your data.

#The learning_rate parameter controls the step size during optimization. A higher learning rate may lead to faster convergence, but can also cause the algorithm to get stuck in local minima."""

# Plot the embedded data
plt.scatter(embedded_data[:, 0], embedded_data[:, 1])
plt.show()

# Save plot to file
plt.savefig('tsne_plot.png')

# =============================================================== # 
# UMAP
# =============================================================== # 

import numpy as np
import umap
import matplotlib.pyplot as plt

data = np.load('your_data.npy')
reducer = umap.UMAP(n_components=2, n_neighbors=30, min_dist=0.1)
embedding = reducer.fit_transform(data)

# The n_neighbors parameter controls the balance between preserving global versus local structure. Higher values tend to preserve global structure, while lower values tend to focus more on local structure. You may need to experiment with different values to find the best one for your data.

#The min_dist parameter controls the minimum distance between points in the embedded space. Smaller values tend to preserve more of the original distance structure, while larger values tend to emphasize more distinct clusters.
plt.scatter(embedding[:, 0], embedding[:, 1])
plt.show()
plt.savefig('umap_plot.png')

# =============================================================== # 
# scanpy's TNSE
# =============================================================== # 

import scanpy as sc
import numpy as np
data = np.load('your_data.npy')
adata = sc.AnnData(data)

# Perform normalization and filtering of the data (if necessary)
# Seems to be optional

sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)

sc.tl.tsne(adata, n_pcs=50, perplexity=30)
adata = adata[:, adata.var['highly_variable']]
sc.pp.scale(adata, max_value=10)

sc.pl.tsne(adata, color=['gene1', 'gene2', ...], save='tsne_plot.png')

# =============================================================== # 
# scanpy's UMAP
# =============================================================== # 

import scanpy as sc
import numpy as np
data = np.load('your_data.npy')
adata = sc.AnnData(data)

# optional:
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
adata = adata[:, adata.var['highly_variable']]
sc.pp.scale(adata, max_value=10)

sc.tl.umap(adata, n_components=2, n_neighbors=30, min_dist=0.1)

sc.pl.umap(adata, color=['gene1', 'gene2', ...], save='umap_plot.png')
