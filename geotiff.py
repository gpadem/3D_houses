import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas
import rasterio
import rioxarray as rxr


data_dir_dtm = "C:/Users/gulce/geoproject/DTM-k43"
image_dtm = os.path.join(data_dir_dtm, "DHMVIIDTMRAS1m_k43.tif")

raster_dtm = rxr.open_rasterio(image_dtm)

# from rasterio.plot import show

# show(raster_dtm)

# dtm_bounds = raster_dtm.bounds

# dtm_profile = raster_dtm.profile

data_dir_dsm = "C:/Users/gulce/geoproject/DSM-k43"
image_dsm = os.path.join(data_dir_dsm, "DHMVIIDSMRAS1m_k43.tif")

raster_dsm = rxr.open_rasterio(image_dsm)


# from rasterio.plot import show

# show(raster_dsm)

# dsm_bounds = raster_dsm.bounds

# dsm_profile = raster_dsm.profile

# print(dtm_bounds, dtm_profile)

# print(dsm_bounds, dsm_profile)


# print(raster_dtm)
# print(raster_dsm)


raster_chm = raster_dsm - raster_dtm


raster_chm.plot.hist()
plt.show()

print(np.nanmin(raster_chm))
print(np.nanmax(raster_chm))

fig, ax = plt.subplots(figsize=(10, 5))
raster_chm.plot(cmap="Greens")
ax.set(title="Canopy Height Model")
ax.set_axis_off()
plt.show()
