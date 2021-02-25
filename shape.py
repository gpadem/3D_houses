import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.colors import ListedColormap
import matplotlib.colors as colors
import geopandas
import rasterio
from rasterio import plot
from rasterio.plot import show
from rasterio.mask import mask
import rioxarray as rxr
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
from rasterio.windows import Window
import fiona

# data_dir_dtm = "C:/Users/gulce/geoproject/DTM-k22"
# image_dtm = os.path.join(data_dir_dtm, "DHMVIIDTMRAS1m_k22.tif")
# with rasterio.open(image_dtm) as src:
#     w = src.read(1, masked=True)


# data_dir_dsm = "C:/Users/gulce/geoproject/DSM-k22"
# image_dsm = os.path.join(data_dir_dsm, "DHMVIIDSMRAS1m_k22.tif")
# with rasterio.open(image_dsm) as krc:
#     x = krc.read(1, masked=True)

# y = w - x

shp_dtm_k22 = geopandas.read_file(
    "C:/Users/gulce/geoproject/DTM-k22/DHMVII_vdc_k22.shp"
)

print(shp_dtm_k22.head())

# print(type(shp_dtm_k22))

# shp_dtm_k22.crs = {"init": "epsg:4326", "no_defs": True}
# shp_dtm_k22.to_crs(epsg=31370)

# shp_dtm_k22.plot()
# plt.show()

# fig, ax = plt.subplots(figsize=(12, 10))
# show(y, ax=ax)
# shp_dtm_k22.plot(ax=ax, color="white", alpha=0.75)  ## alpha is the transparency setting
# plt.show()
