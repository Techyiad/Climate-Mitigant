import numpy as np
import ee
import datetime as dt
from numpy import polyfit
import pandas as pd
import math
from calendar import monthrange
import urllib
from collections import defaultdict
import json
import datetime




def lst_map(img):
	return img.multiply(0.02).subtract(273.15).copyProperties(img,['system:time_start','syst em:time_end'])




def Options(request):
 
		
			options = {}
			options["region"] = json.loads(request.POST.get("region")) if request.POST.get("region") is not None else None
			options["series_start"] = request.POST.get('series_start')
			options["series_end"] = request.POST.get('series_end')
			options["satelite"] = request.POST.get('satelite')		
			options["indices"] = request.POST.get('indices')

			# TODO logic checking
			
			return options


def set_time_series_data(dataList):
	'''
	Args:
		dataList: nested list of data from EarthEngine getRegion method
		template_values: dictionary
	Returns:
		time series data for displaying as text
		time series data for plotting
	'''



	# Format data for highcharts
	# Group data by point while reading
	ts_dict = defaultdict(list)
	graph_dict = defaultdict(list)
	for row in dataList:
		pnt = (float(row[1]), float(row[2]))
		##pnt = '{0:0.4f},{1:0.4f}'.format(*pnt)
		time_int = int(row[3])
		date_obj = datetime.datetime.utcfromtimestamp(float(time_int) / 1000)
		date_str = date_obj.strftime('%Y-%m-%d')
		try:
			val = float(row[4])
			ts_dict[pnt].append([date_str, '{0:0.4f}'.format(val)])
			graph_dict[pnt].append([time_int, val])
		except:
			continue
			##ts_dict[pnt].append([date_str, 'None'])
			##graph_dict[pnt].append([time_int, None])

	'''
	Note ee spits out data for points in one list,
	stringing the point data together
	'''
	timeSeriesTextData = []
	timeSeriesGraphData = []  
	for pnt, ts_data in sorted(ts_dict.items()):
		data_dict = {
			'LongLat': '{0:0.4f},{1:0.4f}'.format(*pnt),
			'Data':sorted(ts_data)
		}
		timeSeriesTextData.append(data_dict)
	for i, (pnt, graph_data) in enumerate(sorted(graph_dict.items())):
		data_dict_graph = {

			 'LongLat': '{0:0.4f},{1:0.4f}'.format(*pnt),
			 'Data':sorted(graph_data)
		}
		timeSeriesGraphData.append(data_dict_graph)
	return timeSeriesTextData, timeSeriesGraphData


def get_time_series(template_values,collection,point,notes):
	TV=template_values
	dS = TV['series_start']
	dE = TV['series_end']
	source=TV['indices']

	

	
	

	## Extract the time series from the collection at the point
	ee_list =ee.ImageCollection( collection).filterDate(dS,dE).getRegion(ee.Geometry.Point(point),1)




	## To use getDownloadUrl, data must be placced into a feature collection 
	features = ee.FeatureCollection(
		ee.Feature(None, {'sample': ee_list}))
	downloadUrl = features.getDownloadUrl('json')
	print(downloadUrl)
	
	response = urllib.request.urlopen(downloadUrl)
	json_dict = json.loads(response.read())
	print(json_dict)
	dataList = json_dict['features'][0]['properties']['sample']
	dataList.pop(0)
	
	timeSeriesTextData = []
	timeSeriesGraphData = []
	timeSeriesTextData, timeSeriesGraphData = set_time_series_data(
		dataList)
	
	print(timeSeriesGraphData)
	#Update template values
	extra_template_values = {
		'source_time':source,
		'timeSeriesData':timeSeriesTextData,
		'timeSeriesGraphData':json.dumps(timeSeriesGraphData),
		'notes_time': notes
	}

	return extra_template_values



#new landsat collection

btl5 = ee.ImageCollection("LANDSAT/LT05/C01/T1_SR").select(["B6"],["SR"])
btl7 = ee.ImageCollection("LANDSAT/LE07/C01/T1_SR").select(["B6"],["SR"])
btl8= ee.ImageCollection("LANDSAT/LC08/C01/T1_SR").select(["B10"],["SR"])


nl5 = ee.ImageCollection("LANDSAT/LT05/C01/T1_TOA")
nl7 = ee.ImageCollection("LANDSAT/LE07/C01/T1_TOA")
nl8 = ee.ImageCollection("LANDSAT/LC08/C01/T1_TOA")

def vhi(img):
	property_list = ['system:index','system:time_start', 'system:time_end']

	brightness_temp=ee.Image(img).select("SR").multiply(0.1)



	ndvi = ee.Image(img).normalizedDifference(["nir", "red"]).rename("NDVI")


	BT_max=ee.Image(brightness_temp).reduce(ee.Reducer.max())

	BT_min=ee.Image(brightness_temp).reduce(ee.Reducer.min())

	tci=ee.Image(BT_max).subtract(brightness_temp).multiply(100).divide(ee.Image(BT_max).subtract(BT_min))



	ndvi_min=ee.Image(ndvi).reduceRegion(ee.Reducer.min(),region_Gh,3000).get("NDVI")

	ndvi_max= ee.Image(ndvi).reduceRegion(ee.Reducer.max(),region_Gh,3000).get("NDVI")

	vci=ee.Image(ndvi).subtract(ee.Number(ndvi_min)).multiply(100).divide(ee.Number(ndvi_max).subtract(ee.Number(ndvi_min)))


	VHI= ee.Image(vci).multiply(0.5).add(ee.Image(tci).multiply(0.5))

	VHI_I = VHI.rename("VHI")
	return VHI_I.copyProperties(img, property_list)

def lst5(img):
	property_list = ['system:index','system:time_start', 'system:time_end']
	band_to_toa=ee.Image(img).select(["B6"])


	toa_radiance =ee.Image( band_to_toa).expression(
		'(Ml * band) + Al', {
		  'Ml': 0.0003342,
		  'Al': 0.01,
		  'band': band_to_toa
		})

	brightness_temp=ee.Image(img).select("SR").multiply(0.1) 



	ndvi = ee.Image(img).normalizedDifference(["nir", "red"])



	ndvi_min=ee.Image(ndvi).reduce(ee.Reducer.min())

	ndvi_max= ee.Image(ndvi).reduce(ee.Reducer.max())

	pv= ee.Image(ndvi).subtract(ndvi_min).divide(ee.Image(ndvi_max).subtract(ndvi_min)).pow(2)


	lse=ee.Image( pv).expression(
		'(0.004 * pv_img) + 0.986', {
		  'pv_img': pv
		})         

	lse_band = lse;
	lse_log = ee.Image(lse_band).log();
	p = 14380
	LST = ee.Image(lse_log).expression(
		'BT / 1 + B10 * (BT / p) * lse_log', {
		  'p': p,
		  'BT': brightness_temp,
		  'B10': toa_radiance,
		  'lse_log': lse_log
		}).subtract(273.5)     
	return ee.Image(LST).copyProperties(img, property_list)

def lst7(img):
	property_list = ['system:index','system:time_start', 'system:time_end']

	band_to_toa=img.select(["B6"])


	toa_radiance = ee.Image(band_to_toa).expression(
		'(Ml * band) + Al', {
		  'Ml': 0.0003342,
		  'Al': 0.01,
		  'band': band_to_toa
		})
	brightness_temp=ee.Image(img).select("SR").multiply(0.1) 



	ndvi = ee.Image(img).normalizedDifference(["nir", "red"])

	ndvi_min=ee.Image(ndvi).reduce(ee.Reducer.min())

	ndvi_max=ee.Image(ndvi).reduce(ee.Reducer.max())

	pv= ee.Image(ndvi).subtract(ndvi_min).divide(ee.Image(ndvi_max).subtract(ndvi_min)).pow(2)


	lse= ee.Image(pv).expression(
		'(0.004 * pv_img) + 0.986', {
		  'pv_img': pv
		})       
	lse_band = lse
	lse_log = ee.Image(lse_band).log()
	p = 14380
	LST = ee.Image(lse_log).expression(
		'BT / 1 + B10 * (BT / p) * lse_log', {
		  'p': p,
		  'BT': brightness_temp,
		  'B10': toa_radiance,
		  'lse_log': lse_log
		}).subtract(273.5)
	return ee.Image(LST).copyProperties(img, property_list)



def lst8(img):
	property_list = ['system:index','system:time_start', 'system:time_end']
	band_to_toa= img.select(["B10"])

	toa_radiance = ee.Image(band_to_toa).expression(
		'(Ml * band) + Al', {
		  'Ml': 0.0003342,
		  'Al': 0.01,
		  'band': band_to_toa
		}).rename('TOA_Radiance')
 
	brightness_temp=ee.Image(img).select("SR").multiply(0.1)       

	ndvi = ee.Image(img).normalizedDifference(["nir", "red"])

	ndvi_min=ee.Image(ndvi).reduce(ee.Reducer.min())
	ndvi_max= ee.Image(ndvi).reduce(ee.Reducer.max())

	pv= ee.Image(ndvi).subtract(ndvi_min).divide(ee.Image(ndvi_max).subtract(ndvi_min)).pow(2)

	lse= ee.Image(pv).expression(
		'(0.004 * pv_img) + 0.986', {
		  'pv_img': pv
		}).rename('LSE')
	p = 14380;
	lse_band = lse;
	lse_log = ee.Image(lse_band).log();
	LST = ee.Image(img).expression(
		'BT / 1 + B10 * (BT / p) * lse_log', {
		  'p': p,
		  'BT': brightness_temp,
		  'B10': toa_radiance,
		  'lse_log': lse_log
		}).subtract(273.5)
	return ee.Image(LST).copyProperties(img, property_list)






def cloudfunction(img):
	"""Apply basic ACCA cloud mask to a daily Landsat 4, 5, or 7 image"""
	cloud_mask = ee.Algorithms.Landsat.simpleCloudScore(img).\
		select(['cloud']).lt(ee.Image.constant(50))
	return img.mask(cloud_mask.mask(cloud_mask))



# calculate ndvi 
def ndvi_anom(img):
	mean= 0.33004655922067055
	std =0.11068838329126819
	property_list = ['system:index','system:time_start', 'system:time_end']
	ndvi = img.normalizedDifference(["nir", "red"])
	ndvi_anom=ee.Image(ndvi).subtract(ee.Number(mean)).divide(ee.Number(std)).rename(["NDVI"]).copyProperties(img, property_list)
	return ndvi_anom

def ndwi_anom(img):
	mean=-0.2990153174811877
	std= 0.1001232100835506
	property_list = ['system:index','system:time_start', 'system:time_end']
	ndwi=img.normalizedDifference(["green", "nir"])
	ndwi_anom=ee.Image(ndwi).subtract(ee.Number(mean)).divide(ee.Number(std))

	return ee.Image(ndwi_anom).rename("NDWI").copyProperties(img, property_list)





global ndwi_mean,ndwi_std








global ndvi_mean,ndvi_std
def anomaly_ndvi(img,ndvi_mean,ndvi_std):

	return ee.Image(img).subtract(ndvi_mean).divide(ndvi_std)





def timelapse_data(options):

	indices=options["indices"]

	series_start=options["series_start"]

	series_end=options["series_end"]

	satelite=options["satelite"]


	start_date=ee.Date.fromYMD(int(series_start),1,1)

	end_date=ee.Date.fromYMD(int(series_end),12,31)

	options["series_start"]=start_date
	options["series_end"]=end_date

	region = options["region"]
	countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
	
	global region_Gh,get_data,notes
	region_Gh=countries.filter(ee.Filter.eq('Country', 'Ghana'))  

	


	if indices=="ndvi anomaly":
		l5images = nl5.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B4","B3"],["nir","red"]).map(ndvi_anom)
		l7images = nl7.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B4","B3"],["nir","red"]).map(ndvi_anom)
		l8images = nl8.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B5","B4"],["nir","red"]).map(ndvi_anom)


		#calculate ndwi for each image in imagecollection
		l578NDVI = ee.ImageCollection(ee.ImageCollection(l5images).merge(l7images)).merge(l8images)
		selected_year_month_data = ee.ImageCollection(l578NDVI).filterDate(start_date,end_date)

		notes="Normalized Difference Vegetation Index Anomaly TimeSeries"						
		return get_time_series(options,selected_year_month_data,region,notes)		
			
	elif indices=="ndwi anomaly":
		l5images = nl5.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B2","B4"],["green","nir"]).map(ndwi_anom)
		l7images = nl7.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B2","B4"],["green","nir"]).map(ndwi_anom)
		l8images = nl8.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B3","B5"],["green","nir"]).map(ndwi_anom)
			#calculate ndwi for each image in imagecollection
		l578NDWI = ee.ImageCollection(l5images.merge(l7images)).merge(l8images)	

		selected_year_month_data = ee.ImageCollection(l578NDWI).filterDate(start_date,end_date)
		NDWI_anom =ee.ImageCollection(selected_year_month_data )

		notes="Normalized Difference Water Index Anomaly TimeSeries"
		return get_time_series(options,NDWI_anom,region,notes)


			
	elif indices=="precipitation":
		collection1 = ee.ImageCollection('UCSB-CHG/CHIRPS/PENTAD').filterDate(start_date,end_date).filterBounds(region_Gh.geometry())	
		#select Precipitation
		selected_Precipitation = ee.ImageCollection(collection1).select('precipitation')
		notes="Precipitation  TimeSeries"
		return get_time_series(options,selected_Precipitation,region,notes)
	elif indices=="vhi":

		l5images = ee.ImageCollection(nl5.combine(btl5).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B4","B3","SR"],["nir","red","SR"]).map(vhi)
		l7images = ee.ImageCollection(nl7.combine(btl7).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B4","B3","SR"],["nir","red","SR"]).map(vhi)
		l8images = ee.ImageCollection(nl8.combine(btl8).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B5","B4","SR"],["nir","red","SR"]).map(vhi)

		total_col=ee.ImageCollection(ee.ImageCollection(l5images).merge(l7images)).merge(l8images)

		VHI= ee.ImageCollection(total_col).filterDate(start_date,end_date)

		notes="Vegetation Health Index TimeSeries"
		return get_time_series(options,ee.ImageCollection(VHI),region,notes)	
	elif indices=="lst":
		l5images = ee.ImageCollection(nl5.combine(btl5).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B4","B3","B6","SR"],["nir","red","B6","SR"]).map(lst5)
		l7images = ee.ImageCollection(nl7.combine(btl7).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B4","B3","B6_VCID_1","SR"],["nir","red","B6","SR"]).map(lst7)
		l8images = ee.ImageCollection(nl8.combine(btl8).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B5","B4","B10","SR"],["nir","red","B10","SR"]).map(lst8)

		total_col=ee.ImageCollection(ee.ImageCollection(l5images).merge(l7images)).merge(l8images)

		LST=ee.ImageCollection(total_col).filterDate(start_date,end_date)
		selected_LST=ee.ImageCollection(LST)
		notes="Land Surface Temperature TimeSeries"
		return get_time_series(options,selected_LST,region,notes)
	elif indices=="smi":
		collection = ee.ImageCollection('MODIS/006/MOD11A2').select('LST_Day_1km').filterDate(start_date,end_date).filterBounds(region_Gh.goemetry())
	
		modLSTday = collection.map(lst_map)



		#select LST
		selected_LST = ee.Image(monthlyLST).mean()

		collection1 = ee.ImageCollection('MODIS/006/MOD13Q1').select('NDVI').filterDate(start_date,end_date).filterBounds(region_Gh.goemetry())


		#select ndvi
		selected_ndvi = ee.Image(collection1 .mean()).multiply(0.0001)



		col_lst = ee.ImageCollection('MODIS/006/MOD11A2').select('LST_Day_1km').filterDate(start_date,end_date).filterBounds(region_Gh.goemetry()).map(lst_map).mean()

		col_ndvi = ee.ImageCollection('MODIS/006/MOD13Q1').select('NDVI').filterDate(start_date,end_date).filterBounds(region_Gh.goemetry()).reduce(ee.Reducer.median())



		######################################## Extract


		NDVI_array = ee.Image(col_ndvi.multiply(0.0001)).reduceRegion(ee.Reducer.toList(), region_Gh, 3000).getInfo().get('NDVI_median')


		LST_array = ee.Image(col_lst).reduceRegion(ee.Reducer.frequencyHistogram().toList(), region_Gh, 3000).getInfo().get('LST_Day_1km')

		


######################################## Calculate the dry and wet edges
		freq = ee.List(LST_array)



		image_list = ee.List(freq.getInfo())

		t_length = image_list.length().getInfo()

		lowerp = math.ceil(int(t_length) * 1 / 100)

		higherp = math.ceil(int(t_length) * 99 / 100)


		LSTmin = freq.slice(0,lowerp + 4000).getInfo()

		LSTmax = freq.slice(0,higherp).getInfo()


		NDVImin = ee.List(NDVI_array).slice(0,lowerp + 4000).getInfo()

		NDVImax = ee.List(NDVI_array).slice(0,higherp).getInfo()


		a,b = polyfit(NDVImax, LSTmax, 1)     # returns the slope (a) and the intercept (b), respectively



		a1,b1 = polyfit(NDVImin, LSTmin, 1) 




		LSTmax = ee.Image(selected_ndvi).multiply(ee.Number(a)).add(ee.Number(b))

		LSTmin = ee.Image(selected_ndvi).multiply(ee.Number(a1)).add(ee.Number(b1))


	#   SMI = (LSTmax – LST) / (LSTmax – LSTmin)
		notes="Soil Moisture Index TimeSeries"

		SMI = LSTmax.subtract(selected_LST).divide(LSTmax.subtract(LSTmin)).multiply(0.01)

		return get_time_series(options,SMI,region,notes)
	
	 




	


