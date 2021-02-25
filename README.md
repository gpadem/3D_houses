# 3D HOUSE PROJECT

This project outcome belongs to Gülce Padem who is currently a junior Data Scientist/AI Operator in making at BeCode's Theano 2.27 promotion.

**Repository:** 3D_houses
**Type of Challenge:** Learning & Consolidation
**Duration:** 2 weeks
**Deadline:** 25/02/21 5:00 PM
**Deployment strategy:** Github page | Presentation | Jupyter Notebook | Webpage | API
**Team challenge:** solo

## Mission objectives

Consolidate the knowledge in Python, specifically in :

+ NumPy
+ Pandas
+ Matplotlib
+ RasterIO
+ Plotly

## Learning Objectives

+ to be able to search and implement new libraries
+ to be able to read and use shapefiles
+ to be able to read and use geoTIFFs
+ to be able to render a 3D plot
+ to be able to present a final product

## The Mission

LIDAR PLANES, an active company in the Geospatial industry would like to use their data to launch a new branch in the insurance business. So, they require to build a solution with their data to model a house in 3D with only a home address.
Their data is acquired by the use of LIDAR which is a method to measure distance using light. The device will illuminate a target with a laser light and a sensor will measure the reflection. Differences in wavelength and return times will be used to get 3D representations of an area.

The data delivered by the company are the following:

+ Digital Surface Map (DSM)
+ Digital Terrain Map (DTM)

These are ready and available to download as zip files from geopunt.be under Digitaal Hoogtemodel Vlaanderen II.

## Must-have features

3D lookup of houses.

## Nice-to-have features

+ Optimize the solution to have the result as fast as possible.
+ Features like the living area of the house in m², how many floors, if there is a pool, the vegetation in the neighborhood, etc...
+ Better visualization.

---

## INSTALLATION

In this project the first thing done was to create a new anaconda working environment to avoid dependency issues.
In the new environment the following packages were installed(see the parantheses for the command to install with conda):

+ numpy (conda install -c conda-forge numpy)
+ pandas (conda install -c conda-forge pandas)
+ matplotlib (conda install -c conda-forge matplotlib)
+ rasterio (conda install -c conda-forge rasterio)
+ geopandas (conda install -c conda-forge geopandas) [only used in the development branch, more on that later]
+ plotly (conda install -c conda-forge plotly)

Jupyter Notebook was installed and launched from the Conda navigator activated in the working environment.

The zip files on geopunt.be were downloaded and the tiff files inside were extracted to the folder **k** under the project folder created called **geoproject**. Because of connection problems only 5 zones were possible for download. It is important to keep in mind that the code has parts that need the exact path of the files. It is important to change these to your local file or folder where you have the tiff files to be able to run the code.

## THE REPOSITORY

There are two branches under the repository.

+ main
+ development

### Main Branch

The structure:

+ README.md
+ final.py
+ final_notebook.ipynb

#### README.md

You are reading it now.
It is important to read the whole file before forking or cloning.

#### final.py

This python file gives the outcome in one go. If you run the program you will go from giving the address as an input until the 3D plot.

#### final_notebook.ipynb

This Jupyter notebook is where the results of each step of the code is more visible. If you would like to inspect more on the outcomes of the different parts of the code, I recommend the use of the notebook.

Here you can see an example 3D plot outcome. 

![newplot (1)](https://user-images.githubusercontent.com/57108538/109167960-a30c2980-777e-11eb-8ec6-08c482b02f8a.png)

### Development Branch

The development branch consists of notebooks and python files that are the sketches of the used code to get the final python file and final notebook in the main branch. In these sketches it is possible to see different approaches to reach a result as well as failed trials to automate the process to read the zip files without downloading to have a more generic code for everyone to use. It is only recommended to look at the development branch if one wants to see different approaches and develop them further.

## Pending things to do

+ Clean the code and adjust attributes to plot the house more accurately
+ Automate reading the zip files online for a more stable and user friendly approach
+ Look for the way to gather more information about the features of the house

## Appreciation

Many thnaks to my fellow colleagues and coaches at BeCode. I could not manage to finish this project without their support and amazing insights.

## Collaboration

This project is open to collaborations as well as forking or cloning for further development.
