import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas
import rasterio
from rasterio import plot
from rasterio.plot import show
from rasterio.windows import Window
from rasterio.windows import from_bounds
from rasterio.enums import Resampling
import requests
import json

r = requests.get(
    "http://loc.geopunt.be/geolocation/location?q=spoorstraat 45, 9340 Lede"
)
house_info_nested = json.loads(r.content)
house_info = pd.json_normalize(house_info_nested)
# print(house_info_nested)

r = requests.get("https://api.basisregisters.vlaanderen.be/v1/gebouweenheden/9044795")
json_test_gebouwheden = json.loads(r.content)
print(json_test_gebouwheden)

r = requests.get("https://api.basisregisters.vlaanderen.be/v1/gebouwen/9043815")
json_test_gebouw = json.loads(r.content)
print(json_test_gebouw)


'geometriePolygoon': {'polygon': {'coordinates': [[[123577.47845698893, 184179.58982590958], [123579.22296898812, 184181.67456191406], [123582.27551299334, 184179.19212991], [123589.99429699779, 184188.29062591866], [123587.06565699726, 184190.85792192072], [123589.83660099655, 184194.16416192055], [123583.58226499707, 184199.39782592654], [123571.26636098325, 184184.78240191564], [123577.47845698893, 184179.58982590958]]], 'type': 'Polygon'}}
# # open dtm file as a part of the raster

# data_dir_dtm = "C:/Users/gulce/geoproject/DTM-k22"
# image_dtm = os.path.join(data_dir_dtm, "DHMVIIDTMRAS1m_k22.tif")
# with rasterio.open(image_dtm) as src:
#     w = src.read(1, masked=True, window=from_bounds)

# # open dsm file as a part of the raster

# data_dir_dsm = "C:/Users/gulce/geoproject/DSM-k22"
# image_dsm = os.path.join(data_dir_dsm, "DHMVIIDSMRAS1m_k22.tif")
# with rasterio.open(image_dsm) as krc:
#     x = krc.read(1, masked=True)
