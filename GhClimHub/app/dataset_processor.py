###############################################################################
#                                   Helpers.                                  #
###############################################################################



import ee
import datetime as dt
import json
import urllib
from chart import get_time_series, set_time_series_data

import numpy 


##############################################################################
#                               Initialization.                               #
###############################################################################

#############################

ee.Initialize()

	 
#countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
#region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  



def _ReadOptions(request):
 
		
			options = {}
			options["dataset"] = request.POST.get('dataset')
			options["datasource"] = request.POST.get('datasource')
			options["date_indices"]=request.POST.get('date_indices')
			
	   
			options["start"] = request.POST.get('start')
			options["end"] = request.POST.get('end')
			options["cloudscore"] = request.POST.get('cloudscore')
			options["region"] = json.loads(request.POST.get("region")) if request.POST.get("region") is not None else None
			options["filename"] = request.POST.get('filename')
			options["palette"] = request.POST.get('palette')
			options["scale"] = request.POST.get('scale',int(3000))
			options["name"] = request.POST.get('name')
			options["download"] = request.POST.get('download')
			options["date_year"] = request.POST.get('date_year')
			options["date_month"] = request.POST.get('date_month')
			options["Variable"] = request.POST.get('Variable')
			options["satelite"] = request.POST.get('satelite')
			
			options["chart_point"]= json.loads( request.POST.get('chart_point')) if request.POST.get("chart_point") is not None else None

			options["region_selected"]=request.POST.get('region_selected')

			options["indices"] = request.POST.get('indices')

			# TODO logic checking
			
			return options
	
def _Getcollection(options,palete):
	"""Creates a ee.Imagecollection with the given options. Also the ee.Algorithms.Landsat.simpleCloudScore is used
		on each image with the cloudscore from the options and the bands are reduced and renamed.
	Args:
	   options: a dict created by _ReadOptions()
		point: boolean if the point coordinates should be used to locate the Imagecollection
		region: boolean if the region coordinates should be used to locate the Imagecollection
	Returns:
		A ee.Imagecollection where each image has 2 bands RED and NIR and is cloudscore masked or None if collection is empty.
	"""
	global collection_info,date_info 
	global notes,name
	try:	
		if options["dataset"]=='NDVI':
			notes= "NDVI calculated from Norm. Diff. of Near-IR and Red bands"
			name="NDVI" +"Target Peroid from :" + options["start"]+ " to "+ options["end"]
		elif options["dataset"]=='EVI':
			notes= "EVI calculated from Near-IR, Red and Blue bands"
			name="EVI" +"Target Peroid from :" + options["start"]+ " to "+ options["end"]
		elif options["dataset"]=='NDWI':
			notes= "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"
			name="NDWI" +"Target Peroid from :" + options["start"]+ " to "+ options["end"]


		date_info  = "Target Peroid from :" + options["start"]+ " to "+ options["end"]
		if options["datasource"]== 'M':
			 coll = get_modis_collection(options["dataset"],options,palete)
			 collection_info ="MODIS"	 
		elif options["datasource"] == '8':
			 coll=get_landsat8_daily_collection(options["dataset"],options,palete)
			 collection_info ="Landsat 8"
		elif options["datasource"] == '7':
			 coll=get_landsat7_daily_collection(options["dataset"],options,palete)
			 collection_info ="Landsat 7"
		elif options["datasource"] == '5':
			 coll=get_landsat5_daily_collection(options["dataset"],options,palete)
			 collection_info ="Landsat 5"
		elif options["datasource"] == 'all':
			 coll=get_landsat457_daily_collection(options["dataset"],options,palete)
		 
			 collection_info ="Landsats 4/5/7"


		col={'mapid':coll['mapid'],'token':coll['token'] ,'collection_info': collection_info,'date_info':date_info,'notes':notes,'download_data':coll['download_data']}
		return col
	except ee.EEException as ex:
		return {'error':'Failed to Compute Data . Error Stated::, '+str(ex)}
	








def chart_it(options,palete):
	"""Creates a ee.Imagecollection with the given options. Also the ee.Algorithms.Landsat.simpleCloudScore is used
		on each image with the cloudscore from the options and the bands are reduced and renamed.
	Args:
	   options: a dict created by _ReadOptions()
		point: boolean if the point coordinates should be used to locate the Imagecollection
		region: boolean if the region coordinates should be used to locate the Imagecollection
	Returns:
		A ee.Imagecollection where each image has 2 bands RED and NIR and is cloudscore masked or None if collection is empty.
	"""
	chart_point=options['chart_point']
	print(chart_point)
	point_gh= ee.Geometry.Point(chart_point)
	global collection_info
	global date_info 
	global notes,name
	if options["dataset"]=='NDVI':
		notes= "NDVI calculated from Norm. Diff. of Near-IR and Red bands"
		name="NDVI" +"Target Peroid from :" + options["start"]+ " to "+ options["end"]
	elif options["dataset"]=='EVI':
		notes= "EVI calculated from Near-IR, Red and Blue bands"
		name="EVI" +"Target Peroid from :" + options["start"]+ " to "+ options["end"]
	elif options["dataset"]=='NDWI':
		notes= "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"
		name="NDWI" +"Target Peroid from :" + options["start"]+ " to "+ options["end"]

   
	date_info  = "Target Peroid from :" + options["start"]+ " to "+ options["end"]
	if options["datasource"]== 'M':
		 coll = get_modis_collection_chart(options["dataset"],options)

		 collection_info ="MODIS"
		 
	elif options["datasource"] == '8':
		 coll=get_landsat8_daily_collection_chart(options["dataset"],options,palete)
		 collection_info ="Landsat 8"
		 chart=get_time_series(options,coll,point,notes)
	elif options["datasource"] == '7':
		 coll=get_landsat7_daily_collection_chart(options["dataset"],options,palete)
		 chart=get_time_series(options,coll,point,notes)
		 collection_info ="Landsat 7"
	elif options["datasource"] == '5':
		 coll=get_landsat5_daily_collection_chart(options["dataset"],options,palete)
		 chart=get_time_series(options,coll,point,notes)
		 collection_info ="Landsat 5"
	elif options["datasource"] == 'all':
		 coll=get_landsat457_daily_collection_chart(options["dataset"],options,palete)
		 chart=get_time_series(options,coll, point_gh,notes)
		 print(chart)
		 collection_info ="Landsats 4/5/7"
		 
	
 
  # send number of images over Channel API to client
  #  _SendMessage(client_id,"collection-info","info","Your collection contains %s images." % collection_size, collection_line2)
	

	col=chart
 
	return col




def _SendMessage(client_id, id, style, line1, line2=None):
	"""Sends messages to the client over the Channel API

	Args:
		client_id: the clients channel api id
		id: id of the alert
		style: type of the alert for Bootstrap CSS styling
		line1: The first line of the alert text
		line2: optinal second line of the alert text
	"""
	params = {"id": id, "style": style, "line1": line1}

	if line2 is not None:
		params["line2"] = line2

	logging.info("Sent to client: " + json.dumps(params))
	channel.send_message(client_id, json.dumps(params))


 # Reduce a collection to a specific region or point (or both)
def filterRegions(collection,region):
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			
			return collection.filterBounds(geometry)
	   
		elif region is None :
			countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
			region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
			return collection.filterBounds(region_Gh.geometry())
		else:
			raise Exception("No location selected")

def palletedata(palettechoice,palette):
	palettendwi =','.join(["#e20000 ", "32cd32", "ffff00", "ff8c00", "#00f9f9", "#3570dd", "0000ff"])

	palettehot=','.join(['#0B0000','#150000','#200000','#150000','#210000','#2B0000','#350000','#400000','#410000','#4A0000','#550000',
  '#560000','#600000','#6A0000','#750000','#760000','#800000','#890000',
  '#940000','#950000','#9F0000','#B40000','#B50000','#BF0000','#D40000','#D50000',
  '#DF0000','#EA0000','#EF0000','#F40000','#FD0000','#FF0A00','#FF1400','#FF1B00',
  '#FF2000','#FF3500','#FF3F00','#FF4400','#FF4A00','#FF5500','#FF5F00','#FF6000','#FF6900'
  ,'#FF6A00','#FF7500','#FF7D00','#FF8100','#FF8A00','#FF9500','#FF9E00','#FFA900','#FFB300','#FFB500','#FFBF00','#FFC900',
  '#FFD400','#FFD500','#FFDF00','#FFE900','#FFEA00','#FFFF00','#FFFF10','#FFFF20','#FFFF30','#FFFF3C','#FFFF3C',
  '#FFFF40','#FFFF67','#FFFF7B','#FFFF80','#FFFF8E','#FFFF93','#FFFFAD','#FFFFAF','#FFFFBF','#FFFFCF','#FFFFDF','#FFFFEF','#FFFFFC',
  '#FFFFFF' ])

	palettendvi=','.join( ['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00'])
	# A nice EVI palette.
	paletteevi =','.join( ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33','#a65628','#f781bf'])
	
	if palettechoice is None and palette is not None:
		ndwiViz = palette
		return ndwiViz 
	elif  palettechoice is not None and palette is None :
		ndwiViz =palettendvi  if palettechoice=='NDVI' else paletteevi if palettechoice=='EVI' else palettendwi if palettechoice=='NDWI' else palettendvi
		return ndwiViz

collection_line2 = None  # line2 of the information about the collection returned over the channel api


cdict = {'red':   ((0.0, 1.0, 1.0), 
				   (0.1, 1.0, 1.0),  # red 
				   (0.4, 1.0, 1.0),  # violet
				   (1.0, 0.0, 0.0)), # blue

		 'green': ((0.0, 0.0, 0.0),
				   (1.0, 0.0, 0.0)),

		 'blue':  ((0.0, 0.0, 0.0),
				   (0.1, 0.0, 0.0),  # red
				   (0.4, 1.0, 1.0),  # violet
				   (1.0, 1.0, 0.0))  # blue
		  }


def cloudMask(img,cloudscore):
	 
		cloud = ee.Algorithms.Landsat.simpleCloudScore(img).select("cloud")
		return img.updateMask(cloud.lt(cloudscore))


#===========================================
#    LANDSAT457 Daily
#===========================================
def get_landsat457_daily_collection(dataset,options,palete):
	"""Return the daily merged image collection for Landsat 4, 5, and 7

	Args:
		dataset: string indicating the dataset/band to return
			(NDVI, NDWI, or EVI)
	Returns:
		EarthEngine image collection object
		String of the collection name
		String of the collection description
		String of the input dataset
		String of additional notes about the collection
	"""


	 # rename the used option values
	source = options["datasource"]
	region=options["region"]
	start = options["start"]
	end = options["end"]
	cloudscore=options["cloudscore"]
	start = ee.ee_date.Date(start,'GMT')
	end = ee.Date(end, 'GMT') 
	
	
	sourceSwitch = {"land4": "LANDSAT/LT4_L1T_TOA", "land5": "LANDSAT/LT5_L1T_TOA", "land7": "LANDSAT/LE7_L1T_TOA"}
   
 


	## This string could/should be built based on the date range or looking at
	##   or looking atthe images in the collection
	coll_name = 'LT4_L1T_TOA,LT5_L1T_TOA,LE7_L1T_TOA'
	coll_desc = 'Landsat 4/5/7 Daily {0} (cloud mask applied)'.format(dataset)
	var_desc = dataset

 
  

	nl5 = ee.ImageCollection("LANDSAT/LT05/C01/T1_TOA")
	nl7 = ee.ImageCollection("LANDSAT/LE07/C01/T1_TOA")



	filterRegions(nl5,region)

	l5images = ee.ImageCollection(filterRegions(nl5,region)).map(landsat457_cloud_mask_func)
	l7images =ee.ImageCollection(filterRegions(nl7,region)).map(landsat457_cloud_mask_func)



	#calculate ndwi for each image in imagecollection
	collection = ee.ImageCollection(ee.ImageCollection(l5images).merge(l7images))

			
	collection = ee.ImageCollection(collection).filterDate(start ,end)

	region_selected = str(options["region_selected"])

	if region_selected == "ghana":
		countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
		region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
	else:
		Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
		region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  



	ndwiViz=palete
	if dataset == 'NDVI':
		notes = "NDVI calculated from Norm. Diff. of Near-IR and Red bands"
		dfm=collection.map(landsat457_ndvi_func).mean() 
		print(region)
		if region is not None:
			geometry =ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)


			download= getData(dfm, region,options["scale"],options["name"])
			print(download)
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }

			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			print(download)
			mapid['download_data']=download
		
		return mapid

	elif dataset == 'NDWI':
		notes = "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"
		dfm=collection.map(landsat457_ndwi_func).mean()  
		if region is not None:
			
			geometry =ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm, region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download
		return mapid

	elif dataset == 'EVI':
		notes = "EVI calculated from Near-IR, Red and Blue bands"
		dfm=collection.map(landsat457_evi_func).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)

			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['EVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['EVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['EVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['EVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download
		return mapid
	## How should this function fail gracefully if the inputs are bad?
	## Should it return an exception?
	else:
		notes = ''
		return collection.select(dataset)

	# Check if the collection conatins images if not return none
	collection_size = collection.size().getInfo()
	print(collection_size + 'checked if its nothin')
	if collection_size == 0:
		return None
 
	# send number of images over Channel API to client


#===========================================
#    LANDSAT5 Daily
#===========================================
def get_landsat5_daily_collection(dataset,options,palete):
	"""Return the daily image collection for only Landsat 5

	Args:
		dataset: string indicating the dataset/band to return
			(NDVI, NDWI, or EVI)
	Returns:
		EarthEngine image collection object
		String of the collection name
		String of the collection description
		String of the input dataset
		String of additional notes about the collection
	"""
	
	source = options["datasource"]
	start = options["start"]
	end = options["end"]
	region= options["region"]
	start = ee.Date(start, 'GMT')
	end = ee.Date(end, 'GMT')
	coll_name = 'LANDSAT/LT05/C01/T1_TOA'
	coll_desc = 'Landsat 5, daily {0} (cloud mask applied)'.format(dataset)
	var_desc = dataset
	## Select dataset after calculating index
	collection = ee.ImageCollection(coll_name).filterDate(start,end)
   
	collection = filterRegions(collection,region)

	region_selected = str(options["region_selected"])

	if region_selected == "ghana":
		countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
		region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
	else:
		Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
		region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  



	ndwiViz=palete
	if dataset == 'NDVI':
		notes = "NDSI calculated from Norm. Diff. of Near-IR and Red bands"
		
		dfm=collection.map(landsat457_ndvi_func).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download
		
		return mapid
	elif dataset == 'NDSI':
		notes = "NDSI calculated from Norm. Diff. of Green and mid-IR bands"
		collection.map(landsat457_ndsi_func)
		print(collection.getMapId(ndwiViz))
		return collection.getMapId(ndwiViz) 
	elif dataset == 'NDWI':
		notes = "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"     
		dfm=collection.map(landsat457_ndwi_func).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download
		
		return mapid
	elif dataset == 'EVI':
		notes = "EVI calculated from Near-IR, Red and Blue bands"
		dfm=collection.map(landsat457_evi_func).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['EVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['EVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['EVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['EVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download
		
		return mapid
	## How should this function fail gracefully if the inputs are bad?
	## Should it return an exception?
	else:
	  notes = ''
	  collection.select(dataset)
	  print(collection.getMapId(ndwiViz))
	  return collection.getMapId(ndwiViz) 





#===========================================
#    LANDSAT7 Daily
#===========================================
def get_landsat7_daily_collection(dataset,options,palete):
	"""Return the daily image collection for only Landsat 7

	Args:
		dataset: string indicating the dataset/band to return
			(NDVI, NDSI, NDWI, or EVI)
	Returns:
		EarthEngine image collection object
		String of the collection name
		String of the collection description
		String of the input dataset
		String of additional notes about the collection
	"""

	source = options["datasource"]
	start = options["start"]
	end = options["end"]
	region= options["region"]
	
	start = ee.Date(start, 'GMT')
	end = ee.Date(end, 'GMT')

	palettejet = ['#00008F', '#0000AC', '#0000CF', '#0000DF', '#0000EF', '#0000FF',
			   '#0010FF', '#0025FF', '#0040FF', '#0050FF', '#0070FF', '#0080FF',
			   '#009FFF', '#009FFF', '#00AFFF', '#00BFFF', '#00D2FF','#00D2FF','#00DFFF','#00FFFF',
			   '#10FFEF','#30FFCF','#44FFBB','#6FFF90','#8FFF70','#AFFF50','#CFFF30','#DFFF20','#FFFF00','#FFDF00',
			   '#FFCF00','#FFAF00','#FF9F00','#FF8000','#FF7000','#FF6000','#FF4000','#FF3000','#FF2000',
			   '#FF1000','#F70000','#EF0000','#DF0000','#CF0000','#BF0000','#AF0000','#9C0000','#8F0000','#860000',
			   '#800000']

	countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
	region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
	coll_name = 'LANDSAT/LE07/C01/T1_TOA'
	coll_desc = 'Landsat 7, daily {0} (cloud mask applied)'.format(dataset)
	var_desc = dataset
	## Select dataset after calculating index
	collection = ee.ImageCollection(coll_name).filterDate(start,end)
	collection=collection.map(landsat457_cloud_mask_func)
	ndwiViz=palete

	region_selected = str(options["region_selected"])

	if region_selected == "ghana":
		countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
		region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
	else:
		Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
		region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  



	if region is not None:
		 collection.filterBounds(region)

	else: 
		collection.filterBounds(region_Gh)



	if dataset == 'NDVI':
		notes = "NDVI calculated from Norm. Diff. of Near-IR and Red bands"    
		dfm=collection.map(landsat457_ndvi_func).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download
		
		return mapid
	elif dataset == 'NDWI':
		notes = "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"
		dfm=collection.map(landsat457_ndwi_func).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download
		
		return mapid
	elif dataset == 'EVI':
		notes = "EVI calculated from Near-IR, Red and Blue bands"
		dfm=collection.map(landsat457_evi_func).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['EVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['EVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['EVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['EVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download
		
		return mapid
	## How should this function fail gracefully if the inputs are bad?
	## Should it return an exception?
	else:
		notes = ''
		collection.select(dataset)
		return collection.getMapId() 




#===========================================
#    LANDSAT8 Daily
#===========================================
def get_landsat8_daily_collection(dataset,options,palete):
	"""Return the daily image collection for only Landsat 8

	Args:
		dataset: string indicating the dataset/band to return
			(NDVI, NDSI, NDWI, or EVI)
	Returns:
		EarthEngine image collection object
		String of the collection name
		String of the collection description
		String of the input dataset
		String of additional notes about the collection
	"""
	 # rename the used option values
	source = options["datasource"]
	start = options["start"]
	end = options["end"]
	region= options["region"]           

	
	start = ee.Date(start, 'GMT')
	end = ee.Date(end, 'GMT')    
		   

  
	ndwiViz=palete
	palettejet = ['#00008F', '#0000AC', '#0000CF', '#0000DF', '#0000EF', '#0000FF',
			   '#0010FF', '#0025FF', '#0040FF', '#0050FF', '#0070FF', '#0080FF',
			   '#009FFF', '#009FFF', '#00AFFF', '#00BFFF', '#00D2FF','#00D2FF','#00DFFF','#00FFFF',
			   '#10FFEF','#30FFCF','#44FFBB','#6FFF90','#8FFF70','#AFFF50','#CFFF30','#DFFF20','#FFFF00','#FFDF00',
			   '#FFCF00','#FFAF00','#FF9F00','#FF8000','#FF7000','#FF6000','#FF4000','#FF3000','#FF2000',
			   '#FF1000','#F70000','#EF0000','#DF0000','#CF0000','#BF0000','#AF0000','#9C0000','#8F0000','#860000',
			   '#800000']

	coll_name = 'LANDSAT/LC08/C01/T1_TOA'
	coll_desc = 'Landsat 8, daily {0} (cloud mask applied)'.format(dataset)
	var_desc = dataset
	collection = ee.ImageCollection(coll_name).filterDate(start,end)
	collection = filterRegions(collection,region)
	## Select dataset after calculating index
	region_selected = str(options["region_selected"])

	if region_selected == "ghana":
		countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
		region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
	else:
		Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
		region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  
   
	
	## Need to code in Landsat 8 cloud masking
	##collection = ee.Imagecollection(coll_name).map(landsat8_cloud_mask_func)
	if dataset == 'NDVI':
		notes = "NDSI calculated from Norm. Diff. of Near-IR and Red bands"    
		dfm=collection.map(landsat8_ndvi_func).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download
		
		return mapid
	elif dataset == 'NDSI':
		notes = "NDSI calculated from Norm. Diff. of Green and mid-IR bands"
		dfm=collection.map(landsat8_ndvi_func).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			mapid=ee.Image(dfm).clip(geometry).getMapId(ndwiViz)
		else:
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(ndwiViz)
		
		return mapid
	elif dataset == 'NDWI':
		notes = "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"
		dfm=collection.map(landsat8_ndwi_func).mean()  
		if region is not None:
			geometry =ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download
		
		return mapid
	elif dataset == 'EVI':
		notes = "EVI calculated from Near-IR, Red and Blue bands"
		dfm=collection.map(landsat8_evi_func).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['EVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['EVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['EVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['EVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download
		
		return mapid
	## How should this function fail gracefully if the inputs are bad?
	## Should it return an exception?
	else:
		collection.select(dataset)
		return collection.getMapId() 

#===========================================
#    MODIS 
#===========================================
def get_modis_collection(dataset,options,palete):
	"""Return the 8 or 16 day composite image collection for MODIS

	Args:
		dataset: string indicating the dataset/band to return
			(LST_Day_1km, NDVI, NDSI, NDWI, or EVI)
	Returns:
		EarthEngine image collection object
		String of the collection name
		String of the collection description
		String of the input dataset
		String of additional notes about the collection
	"""
	coll_name = 'MODIS/MCD43A4_006_{0}'.format(dataset)
	coll_desc = 'MODIS 16-day {0}'.format(dataset)
	var_desc = dataset
	 # rename the used option values
	
	start = options["start"]
	end = options["end"]
	region= options["region"]
	
	start = ee.Date(start, 'GMT')
	end = ee.Date(end, 'GMT')
	collection = ee.ImageCollection(coll_name).filterDate(start,end)
	region_selected = str(options["region_selected"])

	if region_selected == "ghana":
		countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
		region_Gh = countries.filter(ee.Filter.eq('Country', 'Ghana'))  
	else:
		Ghana = ee.FeatureCollection('ft:1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr')
		region_Gh = Ghana .filter(ee.Filter.eq('name', region_selected))  


	ndwiViz=palete
	if dataset == 'NDVI':
		notes = "NDSI calculated from Norm. Diff. of Near-IR and Red bands"
		dfm=collection.select(dataset).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download 
		return mapid

	elif dataset == 'NDWI':
		notes = "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"

		dfm=collection.select(dataset).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			print( ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo())
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDWI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['NDWI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download 
		return mapid



	elif dataset == 'EVI':
		notes = "EVI calculated from Near-IR,Red and Blue bands"
		dfm=collection.select(dataset).mean()  
		if region is not None:
			geometry = ee.Geometry.Polygon(region)
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['EVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['EVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(geometry).getMapId(vizAnomaly)
			download= getData(dfm, region,options["scale"],options["name"])
			mapid['download_data']=download
		else:
			min = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['EVI']
			max = ee.Image(dfm.clip(region_Gh)).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo()['EVI']
			vizAnomaly = {
		'min':min, 'max':max, 
		'palette':ndwiViz
	  }
			mapid=ee.Image(dfm).clip(region_Gh).getMapId(vizAnomaly)
			download= getData(dfm,region_Gh.geometry().getInfo()['coordinates'],options["scale"],options["name"])
			mapid['download_data']=download 
		return mapid
 
   

			

   
   ## return collection, coll_name, coll_desc, var_desc, notes
   


   
#===========================================
#   chart
#===========================================


def get_modis_collection_chart(dataset,options,palete):
	"""Return the 8 or 16 day composite image collection for MODIS

	Args:
		dataset: string indicating the dataset/band to return
			(LST_Day_1km, NDVI, NDSI, NDWI, or EVI)
	Returns:
		EarthEngine image collection object
		String of the collection name
		String of the collection description
		String of the input dataset
		String of additional notes about the collection
	"""
	coll_name = 'MCD43A4_{0}'.format(dataset)
	coll_desc = 'MODIS 16-day {0}'.format(dataset)
	var_desc = dataset
	 # rename the used option values
	
	start = options["start"]
	end = options["end"]
	region= options["region"]
	
	start = ee.Date(start, 'GMT')
	end = ee.Date(end, 'GMT')
	collection = ee.ImageCollection(coll_name).filterDate(start,end)


	ndwiViz=palete
	if dataset == 'NDVI':
		notes = "NDSI calculated from Norm. Diff. of Near-IR and Red bands"
		dfm=ee.ImageCollection(collection.select(dataset).mean()  )

		return dfm

	elif dataset == 'NDWI':
		notes = "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"

		dfm=ee.ImageCollection(collection.select(dataset).mean()  ) 

		return dfm



	elif dataset == 'EVI':
		notes = "EVI calculated from Near-IR,Red and Blue bands"
		dfm=ee.ImageCollection(collection.select(dataset).mean()  ) 

		return dfm
 
   


def get_landsat457_daily_collection_chart(dataset,options,palete):
	"""Return the daily merged image collection for Landsat 4, 5, and 7

	Args:
		dataset: string indicating the dataset/band to return
			(NDVI, NDWI, or EVI)
	Returns:
		EarthEngine image collection object
		String of the collection name
		String of the collection description
		String of the input dataset
		String of additional notes about the collection
	"""


	 # rename the used option values
	source = options["datasource"]
	region=options["region"]
	start = options["start"]
	end = options["end"]
	cloudscore=options["cloudscore"]
	start = ee.ee_date.Date(start,'GMT')
	end = ee.Date(end, 'GMT') 
   
	
	sourceSwitch = {"land4": "LANDSAT/LT4_L1T_TOA", "land5": "LANDSAT/LT5_L1T_TOA", "land7": "LANDSAT/LE7_L1T_TOA"}
   
 

	## This string could/should be built based on the date range or looking at
	##   or looking atthe images in the collection
	coll_name = 'LT4_L1T_TOA,LT5_L1T_TOA,LE7_L1T_TOA'
	coll_desc = 'Landsat 4/5/7 Daily {0} (cloud mask applied)'.format(dataset)
	var_desc = dataset

 
  

		# select only the images that were took between start and end
	land5 = ee.ImageCollection(sourceSwitch["land4"]) 
	land7 = ee.ImageCollection(sourceSwitch["land5"])
	land8 = ee.ImageCollection(sourceSwitch["land7"])

		# only select the images that intersect with the coordinates of point or region
	land5 = filterRegions(land5,region)
	land7 = filterRegions(land7,region)
	land8 = filterRegions(land8,region)

			
	# use the simpleCloudScore algorithm on each collection

		# merge the 3 collections
	collection = ee.ImageCollection(land5.merge(land7))
	collection = ee.ImageCollection(collection.merge(land8)).filterDate(start ,end)
	collection=collection.map(landsat457_cloud_mask_func)
	ndwiViz=palete
	if dataset == 'NDVI':
		notes = "NDVI calculated from Norm. Diff. of Near-IR and Red bands"
		dfm= ee.ImageCollection(collection.map(landsat457_ndvi_func))

		return dfm

	elif dataset == 'NDWI':
		notes = "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"
		dfm=collection.map(landsat457_ndwi_func)

		return dfm

	elif dataset == 'EVI':
		notes = "EVI calculated from Near-IR, Red and Blue bands"
		dfm= collection.map(landsat457_evi_func)

		return dfm
	## How should this function fail gracefully if the inputs are bad?
	## Should it return an exception?
	else:
		notes = ''
		return collection.select(dataset)

	# Check if the collection conatins images if not return none
	collection_size = collection.size().getInfo()
	print(collection_size + 'checked if its nothin')
	if collection_size == 0:
		return None














def get_landsat5_daily_collection_chart(dataset,options,palete):
	"""Return the daily image collection for only Landsat 5

	Args:
		dataset: string indicating the dataset/band to return
			(NDVI, NDWI, or EVI)
	Returns:
		EarthEngine image collection object
		String of the collection name
		String of the collection description
		String of the input dataset
		String of additional notes about the collection
	"""
	
	source = options["datasource"]
	start = options["start"]
	end = options["end"]
	region= options["region"]
	start = ee.Date(start, 'GMT')
	end = ee.Date(end, 'GMT')
	coll_name = 'LANDSAT/LT5_L1T_TOA'
	coll_desc = 'Landsat 5, daily {0} (cloud mask applied)'.format(dataset)
	var_desc = dataset
	## Select dataset after calculating index
	collection = ee.ImageCollection(coll_name).filterDate(start,end)
   
	collection = filterRegions(collection,region)
	ndwiViz=palete
	if dataset == 'NDVI':
		notes = "NDSI calculated from Norm. Diff. of Near-IR and Red bands"
		
		dfm= collection.map(landsat457_ndvi_func)

		return dfm

	elif dataset == 'NDWI':
		notes = "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"     
		dfm=   collection.map(landsat457_ndwi_func)

		return dfm
	elif dataset == 'EVI':
		notes = "EVI calculated from Near-IR, Red and Blue bands"
		dfm= collection.map(landsat457_evi_func)

		return dfm
	## How should this function fail gracefully if the inputs are bad?
	## Should it return an exception?
	else:
	  notes = ''
	  collection.select(dataset)
	  print(collection.getMapId(ndwiViz))
	  return collection.getMapId(ndwiViz) 










def get_landsat7_daily_collection_chart(dataset,options,palete):
	"""Return the daily image collection for only Landsat 7

	Args:
		dataset: string indicating the dataset/band to return
			(NDVI, NDSI, NDWI, or EVI)
	Returns:
		EarthEngine image collection object
		String of the collection name
		String of the collection description
		String of the input dataset
		String of additional notes about the collection
	"""

	source = options["datasource"]
	start = options["start"]
	end = options["end"]
	region= options["region"]
	
	start = ee.Date(start, 'GMT')
	end = ee.Date(end, 'GMT')




	coll_name = 'LE7_L1T_TOA'
	coll_desc = 'Landsat 7, daily {0} (cloud mask applied)'.format(dataset)
	var_desc = dataset
	## Select dataset after calculating index
	collection = ee.ImageCollection(coll_name).filterDate(start,end)
	collection=collection.map(landsat457_cloud_mask_func)
	ndwiViz=palete
	if region is not None:
		 collection.filterBounds(region)

	else: 
		collection.filterBounds(region_Gh)



	if dataset == 'NDVI':
		notes = "NDVI calculated from Norm. Diff. of Near-IR and Red bands"    
		dfm= collection.map(landsat457_ndvi_func)

		return dfm
	elif dataset == 'NDWI':
		notes = "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"
		dfm=  collection.map(landsat457_ndwi_func)

		return dfm
	elif dataset == 'EVI':
		notes = "EVI calculated from Near-IR, Red and Blue bands"
		dfm= collection.map(landsat457_evi_func)

		return dfm
	## How should this function fail gracefully if the inputs are bad?
	## Should it return an exception?
	else:
		notes = ''
		collection.select(dataset)
		return collection.getMapId() 





def get_landsat8_daily_collection_chart(dataset,options,palete):
	"""Return the daily image collection for only Landsat 8

	Args:
		dataset: string indicating the dataset/band to return   for chart
			(NDVI, NDWI, or EVI)
	Returns:
		EarthEngine image collection object
		String of the collection name
		String of the collection description
		String of the input dataset
		String of additional notes about the collection
	"""
	 # rename the used option values
	source = options["datasource"]
	start = options["start"]
	end = options["end"]
	region= options["region"]           

	
	start = ee.Date(start, 'GMT')
	end = ee.Date(end, 'GMT')   
		   

  
	ndwiViz=palete
   

	coll_name = 'LC8_L1T_TOA'
	coll_desc = 'Landsat 8, daily {0} (cloud mask applied)'.format(dataset)
	var_desc = dataset
	collection = ee.ImageCollection(coll_name).filterDate(start,end)
	collection = filterRegions(collection,region)
	## Select dataset after calculating index
   
	
	## Need to code in Landsat 8 cloud masking
	##collection = ee.Imagecollection(coll_name).map(landsat8_cloud_mask_func)
	if dataset == 'NDVI':
		notes = "NDSI calculated from Norm. Diff. of Near-IR and Red bands"    
		dfm = collection.map(landsat8_ndvi_func)  

		return dfm

	elif dataset == 'NDWI':
		notes = "NDWI calculated from Norm. Diff. of near-IR and mid-IR bands"
		dfm=  collection.map(landsat8_ndwi_func)
		return dfm
	elif dataset == 'EVI':
		notes = "EVI calculated from Near-IR, Red and Blue bands"
		dfm=   collection.map(landsat8_evi_func)

		return dfm
	## How should this function fail gracefully if the inputs are bad?
	## Should it return an exception?
	else:
		collection.select(dataset)
		return collection.getMapId() 






#===========================================
#    collection Functions
#===========================================
property_list = ['system:index','system:time_start', 'system:time_end']
def landsat457_cloud_mask_func(img):
	"""Apply basic ACCA cloud mask to a daily Landsat 4, 5, or 7 image"""
	cloud_mask = ee.Algorithms.Landsat.simpleCloudScore(img).\
		select(['cloud']).lt(ee.Image.constant(50))
	return img.mask(cloud_mask.mask(cloud_mask))



def landsat457_ndvi_func(img):
	"""Calculate NDVI for a daily Landsat 4, 5, or 7 image"""
	## Remove .clamp(-0.1, 1)
	return img.normalizedDifference(["B4","B3"]).select([0], ['NDVI'])\
		.copyProperties(img, property_list)

def landsat457_ndsi_func(img):
	"""Calculate NDSI for a daily Landsat 4, 5, or 7 image"""
	## Removed .clamp(-0.1, 1)
	return img.normalizedDifference(["B2", "B5"]).select([0], ['NDSI'])\
		.copyProperties(img, property_list)

def landsat457_ndwi_func(img):
	"""Calculate NDWI (Gao 1996 formulation) for a daily Landsat 4, 5, or 7 image"""
	## Removed .clamp(-0.1, 1)
	return img.normalizedDifference(["B4", "B5"]).select([0], ['NDWI'])\
		.copyProperties(img, property_list)

def landsat457_evi_func(img):
	"""Calculate EVI for a daily Landsat 4, 5, or 7 image"""
	return img.expression('(2.5 * (b("B4") - b("B3"))) / (b("B4") + 6 * b("B3") - 7.5 * b("B1") + 1)')\
		.select([0], ['EVI']).copyProperties(img, property_list)

## DEADBEEF - Need to code in Landsat 8 cloud masking
def landsat8_cloud_mask_func(img):
	return img

def landsat8_ndvi_func(img):
	"""Calculate NDVI for a daily Landsat 8 image"""
	## Removed .clamp(-0.1, 1)
	return img.normalizedDifference(["B5","B4"]).select([0], ['NDVI'])\
		.copyProperties(img, property_list)

def landsat8_ndsi_func(img):
	"""Calculate NDSI for a daily Landsat 8 image"""
	## Removed .clamp(-0.1, 1)
	return img.normalizedDifference(["B3","B6"]).select([0], ['NDSI'])\
		.copyProperties(img, property_list)

def landsat8_ndwi_func(img):
	"""Calculate NDWI for a daily Landsat 8 image"""
	## Removed .clamp(-0.1, 1)
	return img.normalizedDifference(["B6","B5"]).select([0], ['NDWI'])\
		.copyProperties(img, property_list)

def landsat8_evi_func(img):
	"""Calculate EVI for a daily Landsat 8 image"""
	##This formulation should be double checked
	return img.expression('(2.5 * (b("B5") - b("B4"))) / (b("B5") + 6 * b("B4") - 7.5 * b("B2") + 1)')\
		.select([0], ['EVI']).copyProperties(img, property_list)




def landsat457_cloud_mask_func(img):
	"""Apply basic ACCA cloud mask to a daily Landsat 4, 5, or 7 image"""
	cloud_mask = ee.Algorithms.Landsat.simpleCloudScore(img).\
		select(['cloud']).lt(ee.Image.constant(50))
	return img.mask(cloud_mask.mask(cloud_mask))

#===========================================
#   MAP_collection
#===========================================
def map_collection(collection, opacity, palette, minColorbar, maxColorbar):
	""""""
	colorbarOptions = {
		'min':minColorbar,
		'max':maxColorbar,
		'palette':palette,
		'opacity':opacity, #range [0,1]
	}
	mapid = collection

   
	return mapid





#===========================================
#    Chart Functions
#===========================================

def _GetChart2(options):
	"""Generates html code for a small chart and prepares the creation of a full sceen view by saving
		the chart options under a unique id in the Memcache.
	Args:
		options: a option dic created by _ReadOptions()
	Returns:
		Html code with the small chart view or None if collection is empty.
	"""
	regression = options["regression"]
	point = options["point"]
	start = options["start"]
	end = options["end"]

	collection = _GetCollection(options,region=False)  # only use point to filter region

	# _GetCollection() returns None if collection is empty
	if collection is None:
		return None

	# Generates an image with a band "nd" that contains the NDVI
	# and a band "system:time_start" that contains the creation date of the image as seconds since epoch
	def calcValues(img):
		return (img.select()
				.addBands(img.metadata("system:time_start").divide(1000).floor())  # convert to seconds
				.addBands(img.normalizedDifference(["NIR","RED"])))  # NDVI

	collection = collection.map(calcValues)

	# Extracts the pixel values at a specific point and adds them as array called "vlaues" to the image properties
	def getValues(img):
		# useing that the mean reducer only got one value because the poi_geometry is just a point
		return img.reduceRegions(ee.Geometry.Point(point), ee.Reducer.mean(),EXPORT_RESOLUTION).makeArray(["system:time_start","nd"],"values")

	# Creates a list of arrays like [[<image1 epoch seconds>,<image1 ndvi>],[<image2 epoch seconds>,<image2 ndvi>],...]
	# aggregate_array also filters the masked pixels out
	raw_data = ee.FeatureCollection(collection.map(getValues)).flatten().aggregate_array("values").getInfo()


	# style information for the different chart types
	if regression == "zhuWood":

		# get the regression coefficients at the point of interest (makes chart creation a lot slower)
		image = _GetImage(options)
		coeff = image.reduceRegion(ee.Reducer.mean(),ee.Geometry.Point(point),EXPORT_RESOLUTION).getInfo()

		coeff_map = {"a0":coeff["a0_sec"],"a1":coeff["a1_sec"],"a2":coeff["a2_sec"],"a3":coeff["a3_sec"],"rmse":coeff["rmse"]}
		# describe xAxis and yAxis
		description = [("Date","date"),("NDVI", "number"),("Regression: a0=%(a0)s, a1=%(a1)s, a2=%(a2)s, a3=%(a3)s, rmse=%(rmse)s" % coeff_map,"number")]

		hAxis = """{title:"Date"},"""
		chartArea = "{width: \"75%\"}"
		per = "Date"

		# start and end epoch seconds of the collection
		seconds_start = calendar.timegm(time.strptime("%s-01-01" % start, "%Y-%m-%d"))
		seconds_end = calendar.timegm(time.strptime("%s-12-31T23:59:59" % end, "%Y-%m-%dT%H:%M:%S"))

		# convert raw_data to data
		data = []
		for x in raw_data:
			seconds = x[0]
			ndvi = x[1]

			# convert epoch seconds to datetime object
			# not using the seconds because the Google Visualization API can display dates nicely
			data.append([datetime.utcfromtimestamp(seconds),ndvi,None])


		# calculate and add the values of the regression every 45 days
		for x in range(seconds_start,seconds_end,45*24*60*60):
			offset = x - seconds_start

			# calculate the regression ndvi value
			reg_ndvi = coeff["a0_sec"] + coeff["a1_sec"] * math.cos((2*math.pi/(365*24*60*60))*offset) + coeff["a2_sec"] * math.sin((2*math.pi/(365*24*60*60))*offset) + coeff["a3_sec"] * offset

			# convert time_struct to datetime and add it with the regression value to the data
			data.append([datetime(*time.gmtime(x)[:6]),None,reg_ndvi])

		trendline = """legend:{position:"bottom"},series:{1:{lineWidth: 1}},"""
	else:
		hAxis = """{title:"DOY",minValue:0,maxValue:365},"""
		chartArea = "{width: \"50%\"}"
		per = "DOY"

		# is for all points to display the regression (0_ prefix so it is always the first)
		reg_name = "0_%s" % regression
		yAxis = {reg_name:"number"}
		for year in range(start,end + 1):
			# add yAxis description per year
			yAxis[str(year)] = "number"

		# DataTable description
		description = {("DOY","number"): yAxis}

		data = {}
		for x in raw_data:
			# converts epoch seconds to day of year
			date = datetime.utcfromtimestamp(x[0])
			doy = date.timetuple().tm_yday

			year = str(date.timetuple().tm_year)

			data[doy] = {reg_name:x[1],year:x[1]}

		degree = {"poly1":1,"poly2":2,"poly3":3}
		# hide dataset that holds all points and only display the regression for it
		trendline = """series:{0:{visibleInLegend: false}},trendlines:{0:{type:"polynomial",degree:%s,showR2: true, visibleInLegend: true}},""" % degree[regression]



	# Create the DataTable and load the data into it
	# more details about the Google Visualization API at https://developers.google.com/chart/interactive/docs/reference
	data_table = gviz_api.DataTable(description)
	data_table.LoadData(data)

	# Creating a JavaScript code string that represents the chart
	jscode = data_table.ToJSCode("data")

	# Create temporary chart id
	chart_id = _GetUniqueString()

	# Set request options as chart options, and add some extra values
	chart_options = options.copy()
	chart_options.update({"jscode":jscode,"lat":point[1],"lon":point[0],"trendline":trendline,"hAxis":hAxis,"chart_id":chart_id,"chartArea":chartArea,"per":per})

	# Save the chart options temporary in Memcache
	memcache.set(chart_id,chart_options)

	if len(jscode) < 31000:  # max 32767 chars per channel api message
		# Load small chart template
		f = open("templates/small_chart.html", "r")
		small_chart = f.read()
		f.close()

		# Fill in chart options an return template
		return small_chart % chart_options
	else:
		return """No small chart available.<br><a href="/chart?id=%(chart_id)s" target="_blank">Full screen url (only temporary valid)</a>""" % chart_options


#============================
#    Download Map
#============================

def getData(collection,geometry,scale,name):
	path=collection.getDownloadUrl({
		'name': name,
		'scale':scale,
		'crs':'EPSG:4326',
		'region':str( geometry )
		
		})
	return path