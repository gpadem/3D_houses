import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.colors import ListedColormap
import matplotlib.colors as colors
import geopandas
import rasterio
import rioxarray as rxr
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
from rasterio.windows import Window


data_dir_dtm = "C:/Users/gulce/geoproject/DTM-k22"
image_dtm = os.path.join(data_dir_dtm, "DHMVIIDTMRAS1m_k22.tif")
with rasterio.open(image_dtm) as src:
    w = src.read(1, masked=True, window=Window(200, 200, 500, 500))

# # print(w.shape)

# plt.imshow(w)
# plt.show()

data_dir_dsm = "C:/Users/gulce/geoproject/DSM-k22"
image_dsm = os.path.join(data_dir_dsm, "DHMVIIDSMRAS1m_k22.tif")
with rasterio.open(image_dsm) as krc:
    x = krc.read(1, masked=True, window=Window(200, 200, 500, 500))

# print(x.shape)

# plt.imshow(x)
# plt.show()

y = w - x

# plt.imshow(y, cmap="cividis")
# plt.show()


fig, ax = plt.subplots(figsize=(10, 5))

chm_plot = ax.imshow(y)

ax.set_title("Lidar Canopy Height Model (CHM)")


plt.show()
