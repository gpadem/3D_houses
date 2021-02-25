import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas
import rasterio
import rioxarray as rxr
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

data_dir_dtm = "C:/Users/gulce/geoproject/DTM-k22"
image_dtm = os.path.join(data_dir_dtm, "DHMVIIDTMRAS1m_k22.tif")

raster_dtm = rxr.open_rasterio(image_dtm, masked=True)

# data_dir_dsm = "C:/Users/gulce/geoproject/DSM-k22"
# image_dsm = os.path.join(data_dir_dsm, "DHMVIIDSMRAS1m_k22.tif")

# raster_dsm = rxr.open_rasterio(image_dsm, masked=True)

# print("The CRS of this data is:", raster_dtm.rio.crs)

# print("The CRS of this data is:", raster_dsm.rio.crs)

# proj4 = et.epsg["31370"]
# print(proj4)

# print(raster_dtm.rio.bounds())
# print(raster_dsm.rio.bounds())

print(type(raster_dtm))
