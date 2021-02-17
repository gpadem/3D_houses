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

data_dir_dtm = "C:/Users/gulce/geoproject/DTM-k43"
image_dtm = os.path.join(data_dir_dtm, "DHMVIIDTMRAS1m_k43.tif")

raster_dtm = rxr.open_rasterio(image_dtm, masked=True)

data_dir_dsm = "C:/Users/gulce/geoproject/DSM-k43"
image_dsm = os.path.join(data_dir_dsm, "DHMVIIDSMRAS1m_k43.tif")

raster_dsm = rxr.open_rasterio(image_dsm, masked=True)

# print("The CRS for this data is:", raster_dtm.rio.crs)
# print("The spatial extent is:", raster_dtm.rio.bounds())


# print("The CRS for this data is:", raster_dsm.rio.crs)
# print("The spatial extent is:", raster_dsm.rio.bounds())

# print("The no data value is:", raster_dtm.rio.nodata)
# print("The no data value is:", raster_dsm.rio.nodata)

# raster_dtm.plot()
# plt.show()

# raster_dsm.plot()
# plt.show()

# raster_dtm.plot.hist(color="purple")
# plt.show()

# raster_dsm.plot.hist(color="purple")
# plt.show()

# print("the minimum raster value is: ", np.nanmin(raster_dtm.values))
# print("the maximum raster value is: ", np.nanmax(raster_dtm.values))

# print("the minimum raster value is: ", np.nanmin(raster_dsm.values))
# print("the maximum raster value is: ", np.nanmax(raster_dsm.values))

# f, ax = plt.subplots(figsize=(10, 5))
# raster_dtm.plot(cmap="Greys_r", ax=ax)
# ax.set_title("Lidar Digital Elevation Model")
# plt.show()


# f, ax = plt.subplots(figsize=(10, 6))
# raster_dtm.plot.hist(color="purple", bins=20)
# ax.set_title("Histogram of the Data with No Data Values Removed")
# plt.show()

# f, ax = plt.subplots(figsize=(10, 5))
# raster_dsm.plot(cmap="Greys_r", ax=ax)
# ax.set_title("Lidar Digital Elevation Model")
# plt.show()

# f, ax = plt.subplots(figsize=(10, 6))
# raster_dsm.plot.hist(color="green", bins=20)
# ax.set_title("Histogram of the Data with No Data Values Removed")
# plt.show()

# f, ax = plt.subplots(figsize=(10, 6))
# raster_dtm.plot.hist(ax=ax, color="purple", bins=50)
# ax.set(
#     title="Distribution of Lidar DEM Elevation Values",
#     xlabel="Elevation (meters)",
#     ylabel="Frequency",
# )
# plt.show()

# f, ax = plt.subplots(figsize=(10, 6))
# raster_dsm.plot.hist(ax=ax, color="purple", bins=50)
# ax.set(
#     title="Distribution of Lidar DEM Elevation Values",
#     xlabel="Elevation (meters)",
#     ylabel="Frequency",
# )
# plt.show()

# print("The CRS of this data is:", raster_dtm.rio.crs)

# print("The CRS of this data is:", raster_dsm.rio.crs)

# proj4 = et.epsg["31370"]
# print(proj4)

# print(raster_dtm.rio.bounds())
# print(raster_dsm.rio.bounds())

# print(raster_dtm.rio.resolution())

# print("The crs of your data is:", raster_dtm.rio.crs)
# print("The nodatavalue of your data is:", raster_dtm.rio.nodata)
# print("The shape of your data is:", raster_dtm.shape)
# print("The spatial resolution for your data is:", raster_dtm.rio.resolution())
# print("The metadata for your data is:", raster_dtm.attrs)

ep.plot_bands(raster_dsm, cmap="gray")
