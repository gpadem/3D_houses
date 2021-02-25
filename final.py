
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import rasterio
from rasterio.mask import mask
from rasterio import plot
from rasterio.plot import show
import requests
import json
import plotly.graph_objects as go

#Get the address
introduction_message = print("Due to connection problems please choose an address from the zones 1,3,7,22,43. Thank you for your understanding.")
postcode = input("Enter the postcode of the address and hit enter: ")
streetname = input("Enter the streetname of the address and hit enter: ")
house_number = input("Enter the house number of the address and hit enter: ")


#Double-check the address
print("Postcode: ", postcode)
print("Streetname: ", streetname)
print("House number: ", house_number)


#Get a request from the API to get information about the object id of the single house entity
r = requests.get(
    "https://api.basisregisters.vlaanderen.be/v1/adresmatch", params={"postcode":int(postcode), "straatnaam":streetname, "huisnummer":int(house_number) }
)
house_info_nested = json.loads(r.content)

house_info = pd.json_normalize(house_info_nested)
df = pd.json_normalize(house_info.adresMatches[0][0])
dff = pd.json_normalize(df.adresseerbareObjecten[0][0])

#Get a request from the API to get information about the object id of the building
r = requests.get(dff.detail[0])
house_gebouweenheden_nested = json.loads(r.content)
9260

house_gebouweenheden = pd.json_normalize(house_gebouweenheden_nested)
url_gebouwen = house_gebouweenheden['gebouw.detail'][0]

#Get a request from the API to get information about the polygon
r = requests.get(url_gebouwen)
house_gebouw_nested = json.loads(r.content)
house_polygon_nested = house_gebouw_nested["geometriePolygoon"]
house_polygon = house_polygon_nested.get('polygon')

#Make a closed loop of the polygon
house_gebouw = pd.json_normalize(house_gebouw_nested)
house_polygon_list = house_gebouw['geometriePolygoon.polygon.coordinates'][0]
house_polygon_list[0].append((house_polygon_list[0])[0]) 

#Create lists of x and y values of the polygon
xs, ys = zip(*house_polygon_list[0])

#Plot the shape of the polygon to see what we can expect as the shape of the house
plt.figure()
plt.plot(xs,ys) 
plt.show()

#Create min and max x and y coordinates for the house
x_min_house = min(xs)
x_max_house = max(xs)
y_min_house = min(ys)
y_max_house = max(ys)


#Create the bounds of the zones
'''
It is important to notice that the file path seen here is the used file path in the local computer this code was produced. 
Please change this to your local folder and file names to be able to run the code.
'''
df_zone_bounds = pd.DataFrame(columns = ['xmin', 'ymin', 'xmax', 'ymax', 'zone'])
for zone in range(1,43):
    if zone < 10:
        if os.path.isfile('C:/Users/gulce/geoproject/k/DHMVIIDSMRAS1m_k0'+str(zone)+'.tif'):
            file = 'C:/Users/gulce/geoproject/k/DHMVIIDSMRAS1m_k0'+str(zone)+'.tif'
            raster = rasterio.open(file)
            xmin = raster.bounds.left
            ymin = raster.bounds.bottom
            xmax = raster.bounds.right
            ymax = raster.bounds.top
            bound = pd.DataFrame([[xmin, ymin, xmax, ymax, zone]], columns = ['xmin', 'ymin', 'xmax', 'ymax', 'zone'])
            df = pd.concat([df, bound])
    else:
        if os.path.isfile('C:/Users/gulce/geoproject/k/DHMVIIDSMRAS1m_k'+str(zone)+'.tif'):
            file = 'C:/Users/gulce/geoproject/k/DHMVIIDSMRAS1m_k'+str(zone)+'.tif'
            raster = rasterio.open(file)
            xmin = raster.bounds.left
            ymin = raster.bounds.bottom
            xmax = raster.bounds.right
            ymax = raster.bounds.top
            bound = pd.DataFrame([[xmin, ymin, xmax, ymax, zone]], columns = ['xmin', 'ymin', 'xmax', 'ymax', 'zone'])
            df = pd.concat([df, bound])
#Reset the index of teh dataframe
df.reset_index(drop=True, inplace=True)
#Compare the zone bounds with the house bounds to see if the house is in the zone
zone_bounds = df[(df['xmin']<x_min_house) & (df['xmax']>x_max_house) & (df['ymin']<y_min_house) & (df['ymax']>y_max_house)]
#Print the zone number of the house
zone_number = int(zone_bounds.zone.iloc[0])
print(zone_number)

#Mask and crop the DSM and DTM files from the zone
'''
It is important to notice that the file path seen here is the used file path in the local computer this code was produced. 
Please change this to your local folder and file names to be able to run the code.
'''
if zone_number < 10:
    if os.path.isfile('C:/Users/gulce/geoproject/k/DHMVIIDSMRAS1m_k0'+str(zone_number)+'.tif') and os.path.isfile('C:/Users/gulce/geoproject/k/DHMVIIDTMRAS1m_k0'+str(zone_number)+'.tif') :
        dsm_file = 'C:/Users/gulce/geoproject/k/DHMVIIDSMRAS1m_k0'+str(zone_number)+'.tif'
        with rasterio.open(dsm_file) as src_dsm:
            out_img_dsm, out_transform_dsm = rasterio.mask.mask(src_dsm, [house_polygon], crop=True)
            dsm = out_img_dsm[0]
        dtm_file = 'C:/Users/gulce/geoproject/k/DHMVIIDTMRAS1m_k0'+str(zone_number)+'.tif'
        with rasterio.open(dtm_file) as src_dtm:
            out_img_dsm, out_transform_dsm = rasterio.mask.mask(src_dtm, [house_polygon], crop=True)
            dtm = out_img_dtm[0]
else:
    if os.path.isfile('C:/Users/gulce/geoproject/k/DHMVIIDSMRAS1m_k'+str(zone_number)+'.tif') and os.path.isfile('C:/Users/gulce/geoproject/k/DHMVIIDTMRAS1m_k'+str(zone_number)+'.tif'):
        dsm_file = 'C:/Users/gulce/geoproject/k/DHMVIIDSMRAS1m_k'+str(zone_number)+'.tif'
        with rasterio.open(dsm_file) as src_dsm:
            out_img_dsm, out_transform_dsm = rasterio.mask.mask(src_dsm, [house_polygon], crop=True)
            dsm = out_img_dsm[0]
        dtm_file = 'C:/Users/gulce/geoproject/k/DHMVIIDTMRAS1m_k'+str(zone_number)+'.tif'
        with rasterio.open(dtm_file) as src_dtm:
            out_img_dtm, out_transform_dtm = rasterio.mask.mask(src_dtm, [house_polygon], crop=True)
            dtm = out_img_dtm[0]


#Calculate the masked Canopy Height Model of the address
chm_masked = dsm - dtm

#Plot the 2D model of the house
fig, ax = plt.subplots(figsize=(10, 5))

chm_plot = ax.imshow(chm_masked)

ax.set_title("Lidar Canopy Height Model (CHM)")


plt.show()

#Plot the 3D model of the house
fig = go.Figure(data=go.Surface(z=chm_masked))

fig.update_scenes(yaxis_autorange="reversed")

fig.update_layout(title='3D Canopy Height Model')

fig.show()
