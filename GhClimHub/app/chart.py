
from collections import defaultdict
import datetime
import logging
import urllib
import ee
import json
import calendar, time
#===========================================
#  FORMAT_DATA_FOR_HIGHCHARTS
#===========================================
#

def get_time_series(template_values,collection,point,notes):
	TV=template_values
	dS = TV['start']
	dE = TV['end']
	source=TV['datasource']
	product=TV['dataset']
	

	

	#Modify dates to give UTC and to add one to end date for exclusive python nature of this
	dSUTC = ee.Date(dS,'GMT')
	dEUTC = ee.Date(dE,'GMT').advance(1,'day')


	#==============
	#Collection
	#==============
	## This is in the commented block below
	collection = collection;


	dS_int = ee.Date(dS, 'GMT').millis().getInfo()
	dE_int = ee.Date(dE, 'GMT').millis().getInfo()

	## Extract the time series from the collection at the point
	ee_list = collection.filterDate(dS,dE).getRegion(point,1)
	p_data = collection.filterDate(dS,dE).getRegion(point,1).slice(1).getInfo()
	#print(p_data)
	## To use getDownloadUrl, data must be placced into a feature collection 
	features = ee.FeatureCollection(
		ee.Feature(None, {'sample': ee_list}))
	downloadUrl = features.getDownloadUrl('json')
	print(downloadUrl)
	
	response = urllib.urlopen(downloadUrl)
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
		'product_time':product,
		'timeSeriesData':timeSeriesTextData,
		'timeSeriesGraphData':json.dumps(timeSeriesGraphData),
		'notes_time': notes
	}

	return extra_template_values


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



def callTimeseries(collection,variable,domainType,point):
	if(domainType=='points'):
		timeSeriesData=get_timeseries(collection,point,variable)
		timeSeriesGraphData = []
		n_rows = numpy.array(timeSeriesData).shape[0];
		for i in range(2,n_rows):
			entry = {'count':timeSeriesData[i][1],'name':timeSeriesData[i][0]};
			timeSeriesGraphData.append(entry);

		template_values = {
			'timeSeriesData': timeSeriesData,
			'timeSeriesGraphData': timeSeriesGraphData,
		}
	return (timeSeriesData,timeSeriesGraphData,template_values)





def get_timeseries(collection,point,variable):
	######################################################
	#### Data in list format
	######################################################
	dataString = collection.getRegion(point,1).getInfo();
	dataString.pop(0) #remove first row of list ["id","longitude","latitude","time",variable]

	timeList = [row[3] for row in dataString]
	variableList = [row[4] for row in dataString]

	#newarray=[['Dates','NDVI']]
	#for x in zip(timeList,variableList):
	#    if x[1] is not None:
	#        newarray.append([x[0],x[1]])

	######################################################
	#### CREATE TIME SERIES ARRAY WITH DATE IN COL 1 AND VALUE IN COL 2
	######################################################
	timeSeries = []
	for i in range(0,len(variableList),1):
		time_ms = (ee.Algorithms.Date(dataString[i][3])).getInfo()['value']
		data1 = time.strftime('%m/%d/%Y',  time.gmtime(time_ms/1000))
		data2 = (dataString[i][4])
		if data2 is not None:
			timeSeries.append([data1,data2])

	######################################################
	#### SORT IN CHRONOLOGICAL ORDER
	######################################################
	timeSeries.sort(key=lambda date: datetime.datetime.strptime(date[0], "%m/%d/%Y"))

	######################################################
	#### ADD HEADER TO SORTED LIST
	######################################################
	timeSeries= [['Dates','Values']] + timeSeries

	######################################################
	#### CALCULATE NDVI STATS
	######################################################
	#### FILTER OUT "None" VALUES
	#variableList_filt = [x for x in variableList if x is not None]
	#meanNDVI = numpy.mean(variableList_filt,axis=0)
	#medianNDVI = numpy.median(variableList_filt,axis=0)
	#maxNDVI = numpy.max(variableList_filt,axis=0)
	#minNDVI = numpy.min(variableList_filt,axis=0)

	######################################################
	#### RETURN 
	######################################################
	return (timeSeries)







