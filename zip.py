import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas
import rasterio
from rasterio import features

data_dir_dsm = "C:/Users/gulce/geoproject/k22/DSM-k22"
image_dsm = os.path.join(data_dir_dsm, "DHMVIIDSMRAS1m_k22.tif")

raster_dsm = rasterio.open(image_dsm)

print(raster_dsm.bounds.left)


