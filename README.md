# Ghana Climate Hub

This project is to develop web-based national drought monitoring system over Ghana to serve  as an early warning system to mitigate the effect of drought in Ghana. 
The Ghana Climate Hub is an online platform that was developed to provide easy access to real-time information on drought conditions, vegetation health, soil moisture, rainfall, surface temperature over Ghana and its regions.


# Functionality of the application

This project relies on the use of drought indices such as Standardized Precipitation Index(SPI), Normalized Difference Vegetation Index(NDVI) Anomaly, Normalized Difference Water Index(NDWI) Anomaly, and Vegetation Health Index(VHI) to monitor drought conditions over Ghana. These algorithms use data obtained from satellite sensors. Multispectral satellite images at different spectrums are essential for the calculation of the indexes. These datasets were derived from existing Google Earth Engine image collections that are constantly updated.

The Ghana Climate Hub was developed using Earth Engine API. The structure of the system allows faster and easy computation of very large hydro-meteorological data. It also provides the system with up to date satellite images. This structure drought information system provides several benefits. 

* First, it allows the monitoring of a community or a larger region for droughts within a single interface. 

* Second, real-time data from the satellite images helps decision makers and the public to take the necessary action to prepare or plan for impending drought occurrences. 

* Third, its availability on the web allows users to access data and information anywhere.

* The Ghana Climate Hub will help communities make better informed decisions regarding the occurrence of drought and alert communities in advance to help them reduce the damaging effect of drought in Ghana.


Satellite and climate dataset available on Ghana Climate Hub and their respective variables


|Data               | Variables                                               | Spatial Resolution | Temporal resolution | Duration    | References        |
|-------------------|---------------------------------------------------------|--------------------|---------------------|-------------|-------------------|
|Landsat-4,-5,-7,-8  LST, NDVI,EVI, NDWI, SAVI, NDVI, NDWI anomalies,VHI        |     30m            |    16days           | 1984-present|  NASA/USGS        | 
|MODIS              |LST, NDVI, EVI   NDWI,SMI                                |    250m            |    8-16ays          | 2000-present| NASA              |
|AVHRR              |VHI and  NDVI anomaly,                                   |    4km             |    daily            | 1981-present| NOAA              |
|CHIRPS DAILY       |P, SPI,   P anomaly                                      |   4.8km            |   daily             | 1980-present|                   |
|SENTINEL           |LCI, NDMI,SAVI, PPR,  NDVI, NWI, EVI                     |  10m, 20m, 60m     |   5days             | 23 June 2015--present|EUROPEAN UNION/ESA/ COPERNICUS|
 

## Spatial Indexes 

* `LST` - Land Surface Temperature

* `NDVI` - Normalized Difference Vegetation Index

* `NDWI` - Normalized Difference Water Index

* `VHI` - Vegetation Health Index

* `EVI` - Enhanced Vegetation Index

* `P` - Precipitation

* `SPI` - Standardized Precipitation Index

* `SAVI` - Soil-Adjusted Vegetation Index 

* `LCI` - Leaf Chlorophyll Index



# Structure of the web app

* `Google App Engine` - A serverless framework on GCP for developing and deploying the web application. It is also compactible and easy to ingerate Google Earth engine.The App Engine hosts the Django python framework of the drought monitoring system to scale the application and manage requests from users. The App Engine authenticates to Earth Engine when a user makes a request and then computes based on the algorithms created in the python environment. To find out more [clicke here]('https://cloud.google.com/appengine/docs')

* `Google Earth Engine` - Google Earth Engine combines a multi-petabyte catalog of satellite imagery and geospatial datasets with planetary-scale analysis capabilities and makes it available for scientists, researchers, and developers to detect changes, map trends, and quantify differences on the Earth's surface. For more information [visit Google Earth Engine]('https://earthengine.google.com/')

* `Django Framework` - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.



# Runin the Web App locally


## Initialize the web app

 set up a Python development environment, including Python, pip , and virtualenv
 
 install the dependencies by running the below code in your terminal
 
 ```
 cd gheco-eng/GhClimHub
 
 pip install requirements.txt
 ```

## Run the app

```
cd gheco-eng/GhClimHub


python manage.py runserver

```


# Deploy the web app To App Engine

*  Install Google cloud CLI - check it [here]('https://cloud.google.com/sdk/install')

*  Locate the yamle file in the project and make your configurations

*  finally run:
```
gcloud app deploy app.yaml

```





## Sample Web App running


![alt text](https://github.com/ian0549/gheco-eng/blob/master/Ashampoo_Snap_Sunday%2C%2015%20April%202018_09h56m32s_002_.png)




# Acknowledgement




