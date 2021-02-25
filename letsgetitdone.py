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

coord = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]
coord.append(coord[0]) #repeat the first point to create a 'closed loop'

xs, ys = zip(*coord) #create lists of x and y values

plt.figure()
plt.plot(xs,ys) 
plt.show()