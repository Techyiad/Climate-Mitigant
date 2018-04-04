import numpy as np
import ee
import datetime as dt

import math
from calendar import monthrange




	

from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(45)

def create_datelist(start_date, n_months):
	
	dates = [start_date + relativedelta(months=i) 
			  for i in range(0, n_months)]
	
	return np.array(dates)     


def calcMonthlyMean(imageCollection,years,months):
	mylist = ee.List([])
	for y in years:
		for m in months:
			
			w = imageCollection.filter(ee.Filter.calendarRange(y, y, 'year')).filter(ee.Filter.calendarRange(m, m, 'month')).sum()
			
			mylist = mylist.add(ee.Image(w.set('year', y).set('month', m).set('date', ee.Date.fromYMD(y,m,1)).set('system:time_start',ee.Date.fromYMD(y,m,1))))
	return ee.ImageCollection.fromImages(mylist)





#new landsat collection
btl5 = ee.ImageCollection("LANDSAT/LT05/C01/T1_SR").select(["B6"],["SR"])
btl7 = ee.ImageCollection("LANDSAT/LE07/C01/T1_SR").select(["B6"],["SR"])
btl8 = ee.ImageCollection("LANDSAT/LC08/C01/T1_SR").select(["B10"],["SR"])

nl5 = ee.ImageCollection("LANDSAT/LT05/C01/T1_TOA")
nl7 = ee.ImageCollection("LANDSAT/LE07/C01/T1_TOA")
nl8 = ee.ImageCollection("LANDSAT/LC08/C01/T1_TOA")



#============================
#    Download Map
#============================
def getData(collection,geometry,scale,name):
	path = ee.Image(collection).getDownloadUrl({
		'name':str(name),
		'scale':scale,
		'crs':'EPSG:4326',
		'region':str(geometry)
		
		})
	return path



def vhi(img):
	property_list = ['system:index','system:time_start', 'system:time_end']

	brightness_temp = ee.Image(img).select("SR").multiply(0.1)



	ndvi = ee.Image(img).normalizedDifference(["nir", "red"]).rename("NDVI")


	BT_max = ee.Image(brightness_temp).reduce(ee.Reducer.max())

	BT_min = ee.Image(brightness_temp).reduce(ee.Reducer.min())

	tci = ee.Image(BT_max).subtract(brightness_temp).multiply(100).divide(ee.Image(BT_max).subtract(BT_min))



	ndvi_min = ee.Image(ndvi).reduceRegion(ee.Reducer.min(),region_Gh,3000).get("NDVI")

	ndvi_max = ee.Image(ndvi).reduceRegion(ee.Reducer.max(),region_Gh,3000).get("NDVI")

	vci = ee.Image(ndvi).subtract(ee.Number(ndvi_min)).multiply(100).divide(ee.Number(ndvi_max).subtract(ee.Number(ndvi_min)))


	VHI = ee.Image(vci).multiply(0.5).add(ee.Image(tci).multiply(0.5))

	VHI_I = VHI.rename("VHI")
	return VHI_I.copyProperties(img, property_list)










def lst5(img):
	property_list = ['system:index','system:time_start', 'system:time_end']
	band_to_toa = ee.Image(img).select(["B6"])


	toa_radiance = ee.Image(band_to_toa).expression('(Ml * band) + Al', {
		  'Ml': 0.0003342,
		  'Al': 0.01,
		  'band': band_to_toa
		})

	brightness_temp = ee.Image(img).select("SR").multiply(0.1) 



	ndvi = ee.Image(img).normalizedDifference(["nir", "red"])



	ndvi_min = ee.Image(ndvi).reduce(ee.Reducer.min())

	ndvi_max = ee.Image(ndvi).reduce(ee.Reducer.max())

	pv = ee.Image(ndvi).subtract(ndvi_min).divide(ee.Image(ndvi_max).subtract(ndvi_min)).pow(2)


	lse = ee.Image(pv).expression('(0.004 * pv_img) + 0.986', {
		  'pv_img': pv
		})         

	lse_band = lse
	lse_log = ee.Image(lse_band).log()
	p = 14380
	LST = ee.Image(lse_log).expression('BT / 1 + B10 * (BT / p) * lse_log', {
		  'p': p,
		  'BT': brightness_temp,
		  'B10': toa_radiance,
		  'lse_log': lse_log
		}).subtract(273.5)     
	return ee.Image(LST).copyProperties(img, property_list)

def lst7(img):
	property_list = ['system:index','system:time_start', 'system:time_end']

	band_to_toa = img.select(["B6"])


	toa_radiance = ee.Image(band_to_toa).expression('(Ml * band) + Al', {
		  'Ml': 0.0003342,
		  'Al': 0.01,
		  'band': band_to_toa
		})
	brightness_temp = ee.Image(img).select("SR").multiply(0.1) 



	ndvi = ee.Image(img).normalizedDifference(["nir", "red"])

	ndvi_min = ee.Image(ndvi).reduce(ee.Reducer.min())

	ndvi_max = ee.Image(ndvi).reduce(ee.Reducer.max())

	pv = ee.Image(ndvi).subtract(ndvi_min).divide(ee.Image(ndvi_max).subtract(ndvi_min)).pow(2)


	lse = ee.Image(pv).expression('(0.004 * pv_img) + 0.986', {
		  'pv_img': pv
		})       
	lse_band = lse
	lse_log = ee.Image(lse_band).log()
	p = 14380
	LST = ee.Image(lse_log).expression('BT / 1 + B10 * (BT / p) * lse_log', {
		  'p': p,
		  'BT': brightness_temp,
		  'B10': toa_radiance,
		  'lse_log': lse_log
		}).subtract(273.5)
	return ee.Image(LST).copyProperties(img, property_list)



def lst8(img):
	property_list = ['system:index','system:time_start', 'system:time_end']
	band_to_toa = img.select(["B10"])

	toa_radiance = ee.Image(band_to_toa).expression('(Ml * band) + Al', {
		  'Ml': 0.0003342,
		  'Al': 0.01,
		  'band': band_to_toa
		}).rename('TOA_Radiance')
 
	brightness_temp = ee.Image(img).select("SR").multiply(0.1)       

	ndvi = ee.Image(img).normalizedDifference(["nir", "red"])

	ndvi_min = ee.Image(ndvi).reduce(ee.Reducer.min())
	ndvi_max = ee.Image(ndvi).reduce(ee.Reducer.max())

	pv = ee.Image(ndvi).subtract(ndvi_min).divide(ee.Image(ndvi_max).subtract(ndvi_min)).pow(2)

	lse = ee.Image(pv).expression('(0.004 * pv_img) + 0.986', {
		  'pv_img': pv
		}).rename('LSE')
	p = 14380
	lse_band = lse
	lse_log = ee.Image(lse_band).log()
	LST = ee.Image(img).expression('BT / 1 + B10 * (BT / p) * lse_log', {
		  'p': p,
		  'BT': brightness_temp,
		  'B10': toa_radiance,
		  'lse_log': lse_log
		}).subtract(273.5)
	return ee.Image(LST).copyProperties(img, property_list)







def cloudfunction(img):
	"""Apply basic ACCA cloud mask to a daily Landsat 4, 5, or 7 image"""
	cloud_mask = ee.Algorithms.Landsat.simpleCloudScore(img).\
		select(['cloud']).lt(ee.Image.constant(70))
	return img.mask(cloud_mask.mask(cloud_mask))



# calculate ndvi
def ndvi(img):
  property_list = ['system:index','system:time_start', 'system:time_end']
  ndvi = img.normalizedDifference(["nir", "red"]).rename(["NDVI"]).copyProperties(img, property_list)
  return ndvi

def ndwi(img):
	property_list = ['system:index','system:time_start', 'system:time_end']
	return img.normalizedDifference(["green", "nir"]).rename("NDWI").copyProperties(img, property_list)




#===========================================
#			NDWI ANOMALY
#===========================================
def ndwi_anomaly(options):



	
	

	# rename the used option values

		date_month = int(options["date_month"])

		date_year = int(options["date_year"])

		satelite = options["satelite"]
	
		region_selected = str(options["region_selected"])
		region = options["region"]	

		global region_Gh

		if region is not None:
			region_Gh = ee.Geometry.Polygon(region)
		else:
			if region_selected == "ghana":
				countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
				region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
			else:
				Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
				region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  

	
	# Define time range

		startyear = 2000
		endyear = 2018

	#    Set date in ee date format
		startdate = ee.Date.fromYMD(startyear,1,1)
		enddate = ee.Date.fromYMD(endyear,12,31)

	# make a list with years
		years = range(startyear, endyear)
		global scale, name
		months = range(1,12)
		if satelite == "modis":
			collection = ee.ImageCollection('MODIS/MCD43A4_006_NDWI').filterDate(startdate,enddate).filterBounds(region_Gh)
			scale = 250

	
		elif satelite == "landsat":
			scale = 250

			#   filter on date and bounds
			l5images = nl5.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B2","B4"],["green","nir"]).map(ndwi)
			l7images = nl7.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B2","B4"],["green","nir"]).map(ndwi)
			l8images = nl8.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B3","B5"],["green","nir"]).map(ndwi)


	# make a list with years
			year = date_year

			month = date_month

			endingInDays = monthrange(date_year,month)[1]
		
			startMonth = '-' + str(month) + '-01'
			endMonth = '-' + str(month) + '-' + str(endingInDays)
  

 #setting up the start and ending date
			startDate = str(year) + startMonth
			endDate = str(year) + endMonth


			#calculate ndwi for each image in imagecollection
			l578NDWI = ee.ImageCollection(ee.ImageCollection(l5images).merge(l7images)).merge(l8images)	

	


		if satelite == "landsat":
			selected_year_month_data = ee.ImageCollection(l578NDWI).filterDate(startDate,endDate).mean()


			col_mean = ee.Number(-0.2990153174811877)

			col_std = ee.Number( 0.1001232100835506)
			
			NDWI_anom = ee.Image(selected_year_month_data).subtract(col_mean).divide(col_std)

			min = ee.Image(NDWI_anom).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(NDWI_anom).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']

		else:
			
	# make a list with years
			year = date_year

			month = date_month

			endingInDays = monthrange(date_year,month)[1]
		
			startMonth = '-' + str(month) + '-01'
			endMonth = '-' + str(month) + '-' + str(endingInDays)
  

 #setting up the start and ending date
			startDate = str(year) + startMonth
			endDate = str(year) + endMonth

		#select ndwi
			selected_NDWI = ee.ImageCollection(collection).filterDate(startDate,endDate).mean()


	


			histo_mean = ee.Image(ee.ImageCollection(collection).reduce(ee.Reducer.mean()))
			histo_std = ee.Image(ee.ImageCollection(collection).reduce(ee.Reducer.stdDev()))

			selected_year_month_data = ee.Image(selected_NDWI)

			NDWI_anom = ee.Image(selected_year_month_data).subtract(histo_mean).divide(histo_std)

			min = ee.Image(NDWI_anom).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(NDWI_anom).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']

			print(min,max)

		vizAnomaly = {
		'min':min, 'max':max,
		'palette': ','.join(["#e20000 ","32cd32","ffff00","ff8c00","#00f9f9","#3570dd","0000ff"])
	  }
		notes = "NORMALIZED DIFFERENCE WATER INDEX ANOMALY calculated" + " for  " + str(date_year) + "-" + str(date_month)
		name = notes
		download = getData(NDWI_anom,str(region_Gh.geometry().getInfo()['coordinates']),scale,"NDWI" + str(date_year) + "-" + str(date_month))
		mapid = ee.Image(NDWI_anom).clip(region_Gh).getMapId(vizAnomaly)
		col = {'mapid':mapid['mapid'],'token':mapid['token'],'note':notes ,'type':'ndwi_anomaly' ,'min':min,'max':max }
		col['download_data'] = download 
		return col





#===========================================
#			PRECIPITATION
#===========================================
def precipitation(options):


		# rename the used option values

		date_month = int(options["date_month"])

		date_year = int(options["date_year"])


	

	
		region_selected = str(options["region_selected"])
		region = options["region"]	

		global region_Gh,scale, name

		if region is not None:
			region_Gh = ee.Geometry.Polygon(region)
		else:
			if region_selected == "ghana":
				countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
				region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
			else:
				Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
				region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  

	


	# make a list with years
		year = date_year

		month = date_month

		endingInDays = monthrange(date_year,month)[1]
		
		startMonth = '-' + str(month) + '-01'
		endMonth = '-' + str(month) + '-' + str(endingInDays)
  

 #setting up the start and ending date
		startDate = str(year) + startMonth
		endDate = str(year) + endMonth

		print(startDate, endDate)
	
		collection1 = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY').filterDate(startDate,endDate).filterBounds(region_Gh).mean()
	


		#select Precipitation
		selected_Precipitation = ee.Image(collection1)

		max = ee.Image(selected_Precipitation).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo().get("precipitation")

		min = ee.Image(selected_Precipitation).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo().get("precipitation")





		vizAnomaly = {
		'min':min, 'max':max, 
		'palette': ','.join(['#730000', '#E60000', '#FFAA00', '#FCD37F', '#FFFF00', '#FFFFFF', '#AAFF55', '#00FFFF', '#00AAFF', '#0000FF', '#0000AA'])
	  }
		notes = "PRECIPITATION calculated" + " for  " + str(date_year) + "-" + str(date_month)
		name = notes
		scale = 600
		download = getData(selected_Precipitation,str(region_Gh.geometry().getInfo()['coordinates']),scale,"Precipitation" + str(date_year) + "-" + str(date_month))
		mapid = ee.Image(selected_Precipitation).clip(region_Gh).getMapId(vizAnomaly)
		col = {'mapid':mapid['mapid'],'token':mapid['token'],'note':notes,'type':'precipitation','min':min,'max':max }
		col['download_data'] = download 
		return col




#===========================================
#			PRECIPITATION ANOMALY
#===========================================
def precipitation_anom(options):


		# rename the used option values

		date_month = int(options["date_month"])

		date_year = int(options["date_year"])


	

	
		region_selected = str(options["region_selected"])
		region = options["region"]	

		global region_Gh,scale, name

		if region is not None:
			region_Gh = ee.Geometry.Polygon(region)
		else:
			if region_selected == "ghana":
				countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
				region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
			else:
				Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
				region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  

	


	# make a list with years
		year = date_year

		month = date_month

		endingInDays = monthrange(date_year,month)[1]
		
		startMonth = '-' + str(month) + '-01'
		endMonth = '-' + str(month) + '-' + str(endingInDays)
  

 #setting up the start and ending date
		startDate = str(year) + startMonth
		endDate = str(year) + endMonth


	
		col = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY').filterBounds(region_Gh.geometry())
		collection1 = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY').filterDate(startDate,endDate).filterBounds(region_Gh.geometry())
	

		#anom = precip- avg_precip divided by std_precip
		#select Precipitation



		selected_Precipitation = ee.ImageCollection(collection1).mean()

		std_precip=ee.ImageCollection(col).reduce(ee.Reducer.stdDev())
		avg_precip=ee.ImageCollection(col).reduce(ee.Reducer.mean())

		precip_anom= ee.Image(selected_Precipitation).subtract(avg_precip).divide(std_precip)

		max = ee.Image(precip_anom).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['precipitation']
		

		min = ee.Image(precip_anom).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['precipitation']
		print(min,max)




		vizAnomaly = {
		'min':min, 'max':max, 
		'palette': ','.join(['#730000', '#E60000', '#FFAA00', '#FCD37F', '#FFFF00', '#FFFFFF', '#AAFF55', '#00FFFF', '#00AAFF', '#0000FF', '#0000AA'])
	  }
		notes = "PRECIPITATION Anomaly calculated" + " for  " + str(date_year) + "-" + str(date_month)
		name = notes
		scale = 600
		download = getData(precip_anom,str(region_Gh.geometry().getInfo()['coordinates']),scale,"Precipitation" + str(date_year) + "-" + str(date_month))
		mapid = ee.Image(precip_anom).clip(region_Gh).getMapId(vizAnomaly)
		col = {'mapid':mapid['mapid'],'token':mapid['token'],'note':notes,'type':'precipitation','min':min,'max':max }
		col['download_data'] = download 
		return col




#===========================================
#			NDVI ANOMALY
#===========================================
def ndvi_anomaly(options):


	  
	

		# rename the used option values

		date_month = int(options["date_month"])

		date_year = int(options["date_year"])



	
		region_selected = str(options["region_selected"])
		region = options["region"]

		satelite = options["satelite"]

		global region_Gh,scale,name

		if region is not None:
			region_Gh = ee.Geometry.Polygon(region)
		else:
			if region_selected == "ghana":
				countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
				region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
			else:
				Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
				region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  

	
	# Define time range

		startyear = 2000
		endyear = 2018

	# Set date in ee date format
		startdate = ee.Date.fromYMD(startyear,1,1)
		enddate = ee.Date.fromYMD(endyear ,12,31)


	# make a list with years
		years = range(startyear, endyear)

		months = range(1,12)
	
		if satelite == "modis":

			scale = 250
			startyear = 2000
			endyear = 2018

	# Set date in ee date format
			startdate = ee.Date.fromYMD(startyear,1,1)
			enddate = ee.Date.fromYMD(endyear + 1 ,12,31)


	# make a list with years
			years = range(startyear, endyear)


			collection = ee.ImageCollection('MODIS/006/MOD13Q1').select('NDVI').filterDate(startdate,enddate).filterBounds(region_Gh)

		elif satelite == "landsat":
			scale = 250

			l5images = nl5.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B4","B3"],["nir","red"]).map(ndvi)
			l7images = nl7.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B4","B3"],["nir","red"]).map(ndvi)
			l8images = nl8.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B5","B4"],["nir","red"]).map(ndvi)


			#calculate ndwi for each image in imagecollection
			l578NDVI = ee.ImageCollection(ee.ImageCollection(l5images).merge(l7images)).merge(l8images)


	# make a list with years
			year = date_year

			month = date_month

			endingInDays = monthrange(date_year,month)[1]
		
			startMonth = '-' + str(month) + '-01'
			endMonth = '-' + str(month) + '-' + str(endingInDays)
  

 #setting up the start and ending date
			startDate = str(year) + startMonth
			endDate = str(year) + endMonth





						
		elif satelite == "avhrr":
	# make a list with years
			scale = 5000
			year = date_year

			month = date_month

			endingInDays = monthrange(date_year,month)[1]
		
			startMonth = '-' + str(month) + '-01'
			endMonth = '-' + str(month) + '-' + str(endingInDays)
  

 #setting up the start and ending date
			startDate = str(year) + startMonth
			endDate = str(year) + endMonth

			collection = ee.ImageCollection('NOAA/CDR/AVHRR/NDVI/V4').select('NDVI').filterDate('1982-01-01','2018-12-31').filterBounds(region_Gh)
			




		
		#select ndvi


		if satelite == "avhrr":
			selected_ndvi = ee.ImageCollection(collection).filterDate(startDate,endDate).mean()
	


			histo_mean = ee.Image(ee.ImageCollection(collection).reduce(ee.Reducer.mean())).multiply(0.0001)
			histo_std = ee.Image(ee.ImageCollection(collection).reduce(ee.Reducer.stdDev())).multiply(0.0001)

			selected_year_month_data = ee.Image(selected_ndvi)

			ndvi_anom = ee.Image(selected_year_month_data).subtract(histo_mean).divide(histo_std)
			min = ee.Image(ndvi_anom).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(ndvi_anom).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']

			print(max,min)
	

		elif satelite == "landsat":
			selected_year_month_data = ee.ImageCollection(l578NDVI).filterDate(startDate,endDate).mean()
	
			col_mean = ee.Number( 0.33004655922067055)

			col_std = ee.Number(0.11068838329126819)
			
			ndvi_anom = ee.Image(selected_year_month_data).subtract(col_mean).divide(col_std)

			min = ee.Image(ndvi_anom).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(ndvi_anom).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']


		else:

	# make a list with years
			year = date_year

			month = date_month

			endingInDays = monthrange(date_year,month)[1]
		
			startMonth = '-' + str(month) + '-01'
			endMonth = '-' + str(month) + '-' + str(endingInDays)
  

 #setting up the start and ending date
			startDate = str(year) + startMonth
			endDate = str(year) + endMonth


			selected_ndvi = ee.ImageCollection(collection).filterDate(startDate,endDate).mean()


	


			histo_mean = ee.Image(ee.ImageCollection(collection).reduce(ee.Reducer.mean()))
			histo_std = ee.Image(ee.ImageCollection(collection).reduce(ee.Reducer.stdDev()))

			selected_year_month_data = ee.Image(selected_ndvi)




			ndvi_anom = ee.Image(selected_year_month_data).subtract(histo_mean).divide(histo_std)

			min = ee.Image(ndvi_anom).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(ndvi_anom).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']

			print(max,min)
		



		vizAnomaly = {
		'min':min, 'max':max, 
		'palette': ','.join(["87000A","7C3E28","EC712C","FABF45","FFFFFF","51FF78","3DCF4C","215229"])
	  }
		notes = "NORMALIZED DIFFERENCE VEGETATION INDEX ANOMALY calculated" + " for  " + str(date_year) + "-" + str(date_month)
		name = notes
		download = getData(ndvi_anom,str(region_Gh.geometry().getInfo()['coordinates']),scale,"NDVI" + str(date_year) + "-" + str(date_month))
		mapid = ee.Image(ndvi_anom).clip(region_Gh).getMapId(vizAnomaly)
		col = {'mapid':mapid['mapid'],'token':mapid['token'],'note':notes ,'type':'ndvi_anomaly' ,'min':min,'max':max }
		col['download_data'] = download 
		return col






#===========================================
#			VEGETATION HEALTH INDEX
#===========================================
def VHI(options):
	# rename the used option values

	date_month = int(options["date_month"])

	date_year = int(options["date_year"])


	satelite = options["satelite"]
	
	region_selected = str(options["region_selected"])
	region = options["region"]

	global region_Gh,scale, name

	if region is not None:
		region_Gh = ee.Geometry.Polygon(region)
	else:
		if region_selected == "ghana":
			countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
			region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
		else:
			Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
			region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  

	
	# Define time range


	if satelite == "avhrr":
		scale = 600
		# make a list with years
		year = date_year

		month = date_month

		endingInDays = monthrange(date_year,month)[1]
		
		startMonth = '-' + str(month) + '-01'
		endMonth = '-' + str(month) + '-' + str(endingInDays)
  

 #setting up the start and ending date
		startDate = str(year) + startMonth
		endDate = str(year) + endMonth

	


		collection = ee.ImageCollection('NOAA/CDR/AVHRR/NDVI/V4').select('NDVI').filterDate(startDate,endDate).filterBounds(region_Gh).mean()
	



		
		#select ndvi
		selected_ndvi = ee.Image(collection).multiply(0.0001)


		print(ee.Image(selected_ndvi).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo())
		Brightness_Temp = ee.ImageCollection('NOAA/CDR/AVHRR/SR/V4').select('BT_CH4').filterDate(startDate,endDate).filterBounds(region_Gh).mean()

		selected_bt = ee.Image(Brightness_Temp).multiply(0.01)


	# Normalize THe NDVI
		min = ee.Image(selected_ndvi).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']

	


		max = ee.Image(selected_ndvi).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']



		VCI = ee.Image(selected_ndvi).subtract(ee.Number(min)).multiply(100).divide(ee.Number(max).subtract(ee.Number(min)))

		bt_min = ee.Image(selected_bt).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo().get("BT_CH4")

		bt_max = ee.Image(selected_bt).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo().get("BT_CH4")





		TCI = selected_bt.subtract(ee.Number(bt_max)).multiply(-100).divide(ee.Number(bt_max).subtract(bt_min))


	


		VHI = VCI.multiply(0.5).add(TCI.multiply(0.5))


		vhi_min = ee.Image(VHI).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
		vhi_max = ee.Image(VHI).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
		vizAnomaly = {
		'min':vhi_min, 'max':vhi_max, 
		'palette': ','.join(['#087702','#52f904','#ffee00','#ff7700','#ef0404'])
	  }
		

	elif satelite == "landsat":
		scale = 250
		# make a list with years
		year = date_year

		month = date_month

		endingInDays = monthrange(date_year,month)[1]
		
		startMonth = '-' + str(month) + '-01'
		endMonth = '-' + str(month) + '-' + str(endingInDays)
  

 #setting up the start and ending date
		startDate = str(year) + startMonth
		endDate = str(year) + endMonth


		l5images = ee.ImageCollection(nl5.combine(btl5).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B4","B3","SR"],["nir","red","SR"]).map(vhi)
		l7images = ee.ImageCollection(nl7.combine(btl7).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B4","B3","SR"],["nir","red","SR"]).map(vhi)
		l8images = ee.ImageCollection(nl8.combine(btl8).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B5","B4","SR"],["nir","red","SR"]).map(vhi)

		total_col = ee.ImageCollection(ee.ImageCollection(l5images).merge(l7images)).merge(l8images)

		VHI = ee.ImageCollection(total_col).filterDate(startDate,endDate).mean()
		vhi_min = ee.Image(VHI).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['VHI']

		vhi_max = ee.Image(VHI).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['VHI']
	
		vizAnomaly = {
		'min':vhi_min, 'max':vhi_max, 
		'palette': ','.join(['#087702','#52f904','#ffee00','#ff7700','#ef0404'])
	  }
		

	notes = "VEGETATION HEALTH INDEX calculated from NOAA/CDR/AVHRR data" + " for  " + str(date_year) + "-" + str(date_month)
	name = notes
	download = getData(VHI,str(region_Gh.geometry().getInfo()['coordinates']),scale,"VHI" + str(date_year) + "-" + str(date_month))
	mapid = ee.Image(VHI).clip(region_Gh).getMapId(vizAnomaly)
	col = {'mapid':mapid['mapid'],'token':mapid['token'] ,'note':notes , 'type':'vhi','min':vhi_min,'max':vhi_max }
	col['download_data'] = download 
	return col





def lst_map(img):
	return img.multiply(0.02).subtract(273.15).copyProperties(img,['system:time_start','syst em:time_end'])




#===========================================
#			LST
#===========================================
def LST(options):
	# rename the used option values

	date_month = int(options["date_month"])

	date_year = int(options["date_year"])

	satelite = options["satelite"]
	hist_year_start = 2000

	hist_year_end = 2018
	
	region_selected = str(options["region_selected"])
	region = options["region"]

	global region_Gh,scale,name

	if region is not None:
		region_Gh = ee.Geometry.Polygon(region)
	else:
		if region_selected == "ghana":
			countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
			region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
		else:
			Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
			region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  

	
	# Define time range
	if satelite == "modis":
		startyear = hist_year_start
		endyear = hist_year_end
		scale = 250

	# Set date in ee date format
		startdate = ee.Date.fromYMD(startyear,1,1)
		enddate = ee.Date.fromYMD(endyear,12,31)


	# make a list with years
		years = range(startyear, endyear)

		months = range(1,12)
	
	
		collection = ee.ImageCollection('MODIS/006/MOD11A2').select('LST_Day_1km').filterDate(startdate,enddate).filterBounds(region_Gh)
		modLSTday = collection.map(lst_map)
	

		monthlyLST = ee.ImageCollection(calcMonthlyMean(modLSTday,years,months))

		#select LST
		selected_LST = ee.Image(monthlyLST.filter(ee.Filter.eq('year',date_year)).filter(ee.Filter.eq('month',date_month)).mean())




		max = ee.Image(selected_LST).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()["LST_Day_1km"]

		min = ee.Image(selected_LST).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()["LST_Day_1km"]

		vizAnomaly = {
		'min':min, 'max':max, 
		'palette': ','.join(["0000ff","32cd32","ffff00","ff8c00", "#e20000 "])
	  }

		
	elif satelite == "landsat":
	# make a list with years
		year = date_year
		scale = 250
		month = date_month

		endingInDays = monthrange(date_year,month)[1]
		
		startMonth = '-' + str(month) + '-01'
		endMonth = '-' + str(month) + '-' + str(endingInDays)
  

 #setting up the start and ending date
		startDate = str(year) + startMonth
		endDate = str(year) + endMonth

		l5images = ee.ImageCollection(nl5.combine(btl5).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B4","B3","B6","SR"],["nir","red","B6","SR"]).map(lst5)
		l7images = ee.ImageCollection(nl7.combine(btl7).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B4","B3","B6_VCID_1","SR"],["nir","red","B6","SR"]).map(lst7)
		l8images = ee.ImageCollection(nl8.combine(btl8).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B5","B4","B10","SR"],["nir","red","B10","SR"]).map(lst8)

		total_col = ee.ImageCollection(ee.ImageCollection(l5images).merge(l7images)).merge(l8images)

		LST = ee.ImageCollection(total_col).filterDate(startDate,endDate).mean()
		selected_LST = ee.Image(LST)
		max = ee.Image(selected_LST).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()["SR"]
		print(max)
		min = ee.Image(selected_LST).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()["SR"]
	
		vizAnomaly = {
		'min':0, 'max':max, 
		'palette': ','.join(["0000ff","32cd32","ffff00","ff8c00", "#e20000 "])
	  }

	mapid = ee.Image(selected_LST).clip(region_Gh).getMapId(vizAnomaly)

	notes = "LAND SURFACE TEMPERATURE calculated" + " for  " + str(date_year) + "-" + str(date_month)
	name = notes
	download = getData(selected_LST,region_Gh.geometry().getInfo()['coordinates'],scale,"LST" + str(date_year) + "-" + str(date_month))
	print(download)
	col = {'mapid':mapid['mapid'],'token':mapid['token'] ,'note':notes, 'type':'lst','min':min,'max':max }
	col['download_data'] = download 
	return col




#===========================================
#			SMI
#===========================================
def SMI(options):


		# rename the used option values

		date_month = int(options["date_month"])

		date_year = int(options["date_year"])

		satelite = options["satelite"]
	
		region_selected = str(options["region_selected"])
		region = options["region"]

		global region_Gh, scale,name

		if region is not None:
			region_Gh = ee.Geometry.Polygon(region)
		else:
			if region_selected == "ghana":
				countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
				region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
			else:
				Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
				region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  

		
		year = date_year

		month = date_month

		endingInDays = monthrange(date_year,month)[1]
		
		startMonth = '-' + str(month) + '-01'
		endMonth = '-' + str(month) + '-' + str(endingInDays)
  

 #setting up the start and ending date
		startDate = str(year) + startMonth
		endDate = str(year) + endMonth

	
#****************************** LST
		if satelite=="modis":
			collection = ee.ImageCollection('MODIS/006/MOD11A2').select('LST_Day_1km').filterDate(startDate,endDate).filterBounds(region_Gh.geometry())
	
			modLSTday = collection.map(lst_map)

		 
			selected_LST=modLSTday.mean();

			min_LST=modLSTday.reduce(ee.Reducer.min())
			max_LST=modLSTday.reduce(ee.Reducer.max())
		else:

			l5images = ee.ImageCollection(nl5.combine(btl5).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B4","B3","B6","SR"],["nir","red","B6","SR"]).map(lst5)
			l7images = ee.ImageCollection(nl7.combine(btl7).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B4","B3","B6_VCID_1","SR"],["nir","red","B6","SR"]).map(lst7)
			l8images = ee.ImageCollection(nl8.combine(btl8).filterBounds(region_Gh.geometry())).map(cloudfunction).select(["B5","B4","B10","SR"],["nir","red","B10","SR"]).map(lst8)


			if year>1999 & year<2015:
				total_col = ee.ImageCollection(l7images)
			elif year<1999:
				total_col = ee.ImageCollection(l5images)
			elif year>2015:
				total_col = ee.ImageCollection(l8images)


			LST = ee.ImageCollection(total_col).filterDate(startDate,endDate)
			selected_LST=LST.mean();

			min_LST=LST.reduce(ee.Reducer.min())
			max_LST=LST.reduce(ee.Reducer.max())	
	
#****************************** NDVI		
		if satelite=="modis":
			MODIS_NDVI= ee.ImageCollection('MODIS/006/MOD13Q1').select('NDVI').filterDate(startDate,endDate).filterBounds(region_Gh.geometry())
		
			selected_NDVI=MODIS_NDVI
		
			NDVI=selected_NDVI.mean().divide(10000).clip(region_Gh)
			median_NDVI=selected_NDVI.reduce(ee.Reducer.median())
		else:
			l5images = nl5.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B4","B3"],["nir","red"]).map(ndvi)
			l7images = nl7.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B4","B3"],["nir","red"]).map(ndvi)
			l8images = nl8.filterBounds(region_Gh.geometry()).map(cloudfunction).select(["B5","B4"],["nir","red"]).map(ndvi)



			if year>1999 & year<2015:
				total_col = ee.ImageCollection(l7images)
			elif year<1999:
				total_col = ee.ImageCollection(l5images)
			elif year>2015:
				total_col = ee.ImageCollection(l8images)


			l578NDVI = total_col
			selected_year_month_data = ee.ImageCollection(l578NDVI).filterDate(startDate,endDate)

			selected_NDVI=selected_year_month_data 
		
			NDVI=selected_NDVI.mean().clip(region_Gh)
			median_NDVI=selected_NDVI.reduce(ee.Reducer.median())

#*************************************Linear Regression




#****************************MIN LST*************************
 
#Dependent: LST
		y = ee.Image(min_LST)
#Independent: ndvi
		x = ee.Image(median_NDVI)
#Intercept: b
		b = ee.Image(1).rename('b')
#create an image collection with the three variables by concatenating them
		reg_img = ee.Image.cat(b,x,y)

# fit the model
		fit = ee.Image(reg_img).reduceRegion(ee.Reducer.linearRegression(2,1),region_Gh.geometry(), 3000)
		
		fit = fit.combine({"coefficients": ee.Array([[1],[1]])}, False)


#Get the coefficients as a nested list,
#cast it to an array, and get just the selected column
		slo = (ee.Array(fit.get('coefficients')).get([1,0])).getInfo()
		inte = (ee.Array(fit.get('coefficients')).get([0,0])).getInfo()


 
 
 
#******************MAX LST ******************************* 
 
# Dependent: lst
		y1 = max_LST
#Independent: ndvi
		x1 = median_NDVI
#Intercept: b
		b1 = ee.Image(1).rename('b')
#create an image collection with the three variables by concatenating them
		reg_img1 = ee.Image.cat(b1,x1,y1)
		
#fit the model
		fit1 = ee.Image(reg_img1).reduceRegion(ee.Reducer.linearRegression(2,1),region_Gh.geometry(),3000)
		
		fit1 = fit1.combine({"coefficients": ee.Array([[1],[1]])}, False)
		

#Get the coefficients as a nested list,
#cast it to an array, and get just the selected column
		slo1 = (ee.Array(fit1.get('coefficients')).get([1,0])).getInfo()
		int1 = (ee.Array(fit1.get('coefficients')).get([0,0])).getInfo()

		
 
 
#****************************SMI*************************
# LST_max=a*NDVI +b
# LST_min=a1*NDVI + b1


		LST_max=ee.Image(NDVI).multiply(ee.Number(slo1)).add(ee.Number(int1))

		LST_min=ee.Image(NDVI).multiply(ee.Number(slo)).add(ee.Number(inte))



		SMI=ee.Image(LST_max).subtract(selected_LST).divide(ee.Image(LST_max).subtract(LST_min))
		if satelite=="modis":
			max = ee.Image(SMI).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
			min = ee.Image(SMI).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
		else:
			max=2.3
			min=-2.3



		vizAnomaly = {
		'min':min, 'max':max, 
		'palette': ','.join(['#730000', '#E60000', '#FFAA00', '#FCD37F', '#FFFF00', '#FFFFFF', '#AAFF55', '#00FFFF', '#00AAFF', '#0000FF', '#0000AA'])
	  }
		notes = "SOIL MOISTURE INDEX calculated" + " for  " + str(date_year) + "-" + str(date_month)
		scale = 300
		name = notes
		mapid = ee.Image(SMI).clip(region_Gh).getMapId(vizAnomaly)
		download = getData(SMI,str(region_Gh.geometry().getInfo()['coordinates']),scale,"SMI" + str(date_year) + "-" + str(date_month))
		col = {'mapid':mapid['mapid'],'token':mapid['token'] , 'note':notes,'type':'smi' ,'min':min,'max':max }
		col['download_data'] = download 
		return col





#===========================================
#			COMPUTE INDICES
#===========================================
def indices(options):
	global data

	selected_indices = options["indices"]


	
	if selected_indices == "ndvi anomaly":
	
		try:
			data = ndvi_anomaly(options)
			return data
		except ee.EEException as e :
			data = {'error':'Failed to Compute NORMALIZED DIFFERENCE VEGETATION INDEX ANOMALY Data . Error Stated::, ' + str(e)}
			return data
	elif selected_indices == "ndwi anomaly":
		try:
			data = ndwi_anomaly(options)
			return data
		except ee.EEException as e :
			data = {'error':'Failed to Compute  NORMALIZED DIFFERENCE WATER INDEX  ANOMALY Data . Error Stated::, ' + str(e)}
			return data

	elif selected_indices == "precipitation anom":
		try:
			data = precipitation_anom(options)
			return data
		except ee.EEException as e :
			data = {'error':'Failed to Compute  Precipitation   ANOMALY Data . Error Stated::, ' + str(e)}
			return data

	elif selected_indices == "smi":
		
		data = SMI(options)
		return data

	elif selected_indices == "lst":
		
		data = LST(options)
		return data


	elif selected_indices == "vhi":
		try:
			data = VHI(options)
			return data
		except ee.EEException as e :
			data = {'error':'Failed to Compute VEGETATION HEALTH INDEX Data . Error Stated::, ' + str(e)}
			return data

	elif selected_indices == "precipitation":
		try:
			data = precipitation(options)
			return data
		except ee.EEException as e :
			data = {'error':'Failed to Compute PRECIPITATION  Data . Error Stated::, ' + str(e)}
			return data

	elif selected_indices == "spi":
		data = spi(options)
		return data
		#except ee.EEException as e :
		#	data={'error':'Failed to Compute STANDARDIZED PRECIPITATION INDEX Data .
		#	Error Stated::, '+str(e)}
		#	return data

	






def log(img):
	return ee.Image(img).log()

# calculate the monthly mean
def Cdf(x,shape,scale):
	a = shape
	b = ee.Image(x).divide(ee.Image(scale))
	incom_gam = ee.Image(a).gammainc(b)
	
	return incom_gam


def norm_ppf(x,mean,std):

	return ee.Image(mean).subtract(ee.Image(std)).multiply(ee.Number(2).sqrt()).multiply(ee.Image(x).multiply(2).erfcInv())





#===========================================
#			SPI
#===========================================





###### 3 MONTHS SELECTING

def hist_datelist(yearlist,selected):
	f1 = [11,12]
	f2 = [12]
	f3 = [1,2,3,4,5,6,7,8,9,10,11,12]
	li = []
	if selected == 1:        
		for y in yearlist:
			y = y - 1           
			for b in f1:
				li.append(ee.Date.fromYMD(y,b,1))
			li.append(ee.Date.fromYMD(y + 1,selected,1))   
	elif selected == 2:
		for y in yearlist:
			y = y - 1           
			for b in f2:
				li.append(ee.Date.fromYMD(y,b,1))
			li.append([ee.Date.fromYMD(y + 1,selected - 1,1),ee.Date.fromYMD(y + 1,selected,1)])  
		
	elif selected >= 3:
		f3 = f3[selected - 3:selected]      
		for y in yearlist:
			for b in f3:
				li.append(ee.Date.fromYMD(y,b,1))        
	return ee.List(li)


def mlog(img):
	return ee.Image(img).log()
	

def MLestimator(data,img):
	
	x_ = ee.ImageCollection(data).reduce(ee.Reducer.mean()).log()
	y_ = ee.ImageCollection(data).map(mlog).reduce(ee.Reducer.mean())
	A = ee.Image(x_).subtract(y_)
	B = ee.Image(1).add(ee.Image(1).add(A.multiply(4).divide(3)).sqrt()).divide(A.multiply(4))
	a = ee.ImageCollection(data).reduce(ee.Reducer.mean()).divide(B)
	theta = ee.Image(img).divide(a)
	return ee.Image(theta).gammainc(B)


def norm_inverseCDF(x):
	pass

def getallnonzeros(img):
	return ee.Image(img).gt(0)

def getallzeros(img):
	return ee.Image(img).lt(1)




def spi(options):

		# rename the used option values

		date_month = int(options["date_month"])

		date_year = int(options["date_year"])

		region_selected = str(options["region_selected"])
		region = options["region"]	

		global region_Gh,scale, name

		if region is not None:
			region_Gh = ee.Geometry.Polygon(region)
		else:
			if region_selected == "ghana":
				countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
				region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
			else:
				Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
				region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  

	

# set start and end year
		startyear = 1981
		endyear = 2017

 

# make a date object
		startdate = ee.Date.fromYMD(startyear, 1, 1)
		enddate = ee.Date.fromYMD(endyear + 1, 12, 30)
 
 
 
#make a list with years
		years = range(1981, 2018)


#make a list with months
		months = range(1, 12)


	

		rainfal_data = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY').filterDate('1981-01-01','2018-12-31').filterBounds(region_Gh)
# this is the ish
		def calcMonthlyMean1(imageCollection):
			mylist = []
			for y in years:
				for m in months:
					w = imageCollection.filter(ee.Filter.calendarRange(y, y, 'year')).filter(ee.Filter.calendarRange(m, m, 'month')).sum()
					mylist.append(ee.Image(w.set('year', y).set('month', m).set('date', ee.Date.fromYMD(y,m,1)).set('system:time_start',ee.Date.fromYMD(y,m,1))))
			return ee.ImageCollection.fromImages(ee.List(mylist))


		monthlyPrecip = ee.ImageCollection(calcMonthlyMean1(rainfal_data))


		years_list = range(1982, 2017)

		date_hist = ee.List(hist_datelist(years_list,date_month))

		
		col_hist = ee.ImageCollection(monthlyPrecip).filter(ee.Filter.inList('system:time_start', date_hist))
		
		year_on = [date_year]

		dates_year = ee.List(hist_datelist(year_on,date_month))

		col_year = monthlyPrecip.filter(ee.Filter.inList('system:time_start',dates_year))
		 
		v_img = ee.ImageCollection(col_year).reduce(ee.Reducer.mean())

		allnonz = ee.ImageCollection(col_hist).map(getallnonzeros)


		zero = ee.ImageCollection(col_hist).map(getallzeros)

		allnonzero = ee.Image(ee.ImageCollection(allnonz).reduce(ee.Reducer.sum())).reduceRegion(ee.Reducer.sum(),region_Gh,30000).getInfo()['precipitation_sum']

		zero_p = ee.Image(ee.ImageCollection(zero).reduce(ee.Reducer.sum())).reduceRegion(ee.Reducer.sum(),region_Gh,30000).getInfo()['precipitation_sum']

		
		q = ee.Number(zero_p).divide(allnonzero)
		Gx = MLestimator(col_hist,v_img)
		inv_cum = ee.Image(Gx)
		H = ee.Image(inv_cum).multiply(ee.Number(1).subtract(q)).add(q)


		SPI_exp = ee.Image(H).expression('(b <0 || b<= 0.5) ? -1*(t1- (c0+c1*t1+c2*t1**2)/(1+d1*t1+d2*t1**2+d3*t1**3))  ' + ':(b <0.5 || b<= 1)? (t2- (c0+c1*t2+c2*t2**2)/(1+d1*t2+d2*t2**2+d3*t2**3)) : null',{
  'b':H.select('precipitation_mean'),
  'null':ee.Image(0),
  't1':ee.Image(1).divide(ee.Image(H).pow(2)).log().sqrt(),
  't2':ee.Image(1).divide(ee.Image(1).subtract(H).pow(2)).log().sqrt(),
  'c0':2.515517,
  'c1':0.802583,
  'c2':0.010328,
  'd1':1.432788,
  'd2':0.189269,
  'd3':0.001308

})

	
		min = ee.Image(SPI_exp).reduceRegion(ee.Reducer.percentile([0]), region_Gh,300000).getInfo()['constant']
	
		max = ee.Image(SPI_exp).reduceRegion(ee.Reducer.percentile([100]), region_Gh, 300000).getInfo()['constant']

	
		



		vizAnomaly = {
		'min':-1, 'max':max, 
		'palette': ','.join(['#730000','#E60000','#FFAA00','#FCD37F','#FFFF00','#FFFFFF','#AAFF55','#00FFFF','#00AAFF','#0000FF','#0000AA'])
	  }
		notes = "Standardized Precipitation Index calculated" + " for  " + str(date_year) + "-" + str(date_month)
		scale = 1000
		name = notes
		download = getData(SPI_exp,str(region_Gh.geometry().getInfo()['coordinates']),scale,"SPI" + str(date_year) + "-" + str(date_month))
		mapid = ee.Image(SPI_exp).clip(region_Gh).getMapId(vizAnomaly)
		col = {'mapid':mapid['mapid'],'token':mapid['token'],'note':notes ,'type':'spi' ,'min':min,'max':max }
		col['download_data'] = download 
		return col





	
	
