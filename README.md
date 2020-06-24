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


Data               | Variables      | Spatial Resolution | Temporal resolution | Duration    | References
-------------------|----------------|--------------------|---------------------|-------------|-------------------
Landsat-4,-5,-7,-8 |LST, NDVI,      |     30m            |    16days           |1984-present |NASA/USGS
                   | EVINDWI, SAVI  |                    |                     |             |
                   | NDVI           |                    |                     |             |
                   | NDWI anomalies |                    |                     |             |
                   | VHI            |                    |                     |             |
-------------------|----------------|--------------------|---------------------|-------------|----------------------
MODIS              |LST, NDVI, EVI  |    250m            |    8-16ays          | 2000-present| NASA
                   | NDWI,SMI       |                    |                     |             |
-------------------|----------------|--------------------|---------------------|-------------|----------------------
AVHRR              |VHI and         |    4km             |    daily            | 1981-present| NOAA
                   | NDVI anomaly,  |                    |                     |             |
-------------------|----------------|--------------------|---------------------|-------------|----------------------
CHIRPS DAILY       |P, SPI,         |   4.8km            |   daily             | 1980-present|
                   | P anomaly      |                    |                     |             |
-------------------|----------------|--------------------|---------------------|-------------|----------------------
SENTINEL           |LCI, NDMI,      |  10m, 20m, 60m     |   5days             | 23 June 2015|EUROPEAN 
                   | SAVI, PPR,     |                    |                     | -present    |UNION/ESA/COPERNICUS
                   | NDVI, NWI, EVI |                    |                     |             |
-------------------|----------------|--------------------|---------------------|-------------|----------------------




