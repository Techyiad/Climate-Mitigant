import numpy as np
import ee
import datetime as dt
from numpy import polyfit
import pandas as pd
import math
from calendar import monthrange
ee.Initialize()



	

geometryGH = ee.Geometry.Polygon([[[-2.84271240234375, 10.964407406892343],
		  [-2.81524658203125, 10.93204830297375],
		  [-2.8619384765625, 10.891594459751865],
		  [-2.889404296875, 10.783690724613116],
		  [-2.9443359375, 10.71083379257758],
		  [-2.90863037109375, 10.689243182249529],
		  [-2.95257568359375, 10.62716163281584],
		  [-2.9058837890625, 10.52726485464839],
		  [-2.86468505859375, 10.448944731763113],
		  [-2.77130126953125, 10.421933206636895],
		  [-2.8619384765625, 10.323616849342223],
		  [-2.7520751953125, 10.22632559332376],
		  [-2.8179931640625, 10.188482038665908],
		  [-2.7850341796875, 9.961326922955207],
		  [-2.735595703125, 9.842277522029486],
		  [-2.8070068359375, 9.728599402991875],
		  [-2.7520751953125, 9.66903825636035],
		  [-2.779541015625, 9.56613509648869],
		  [-2.7081298828125, 9.479455625458918],
		  [-2.7410888671875, 9.333134455664538],
		  [-2.6641845703125, 9.26808304825559],
		  [-2.7960205078125, 9.159637288435146],
		  [-2.7850341796875, 9.040308729266782],
		  [-2.6641845703125, 9.00775769070097],
		  [-2.6092529296875, 8.779818903544244],
		  [-2.515869140625, 8.203929637502366],
		  [-2.6202392578125, 8.13324302660295],
		  [-2.6806640625, 8.02990943258469],
		  [-2.7410888671875, 7.915668036108836],
		  [-2.779541015625, 7.9646325397584965],
		  [-2.83447265625, 7.839489477618971],
		  [-2.9168701171875, 7.648982348475696],
		  [-2.9937744140625, 7.2949591706812305],
		  [-2.9718017578125, 7.2295700052671],
		  [-3.0926513671875, 7.049701233586126],
		  [-3.251953125, 6.815222222102454],
		  [-3.2794189453125, 6.651564033219323],
		  [-3.0267333984375, 5.863603975677071],
		  [-3.043212890625, 5.710579321395293],
		  [-2.96356201171875, 5.716045197981245],
		  [-2.9827880859375, 5.653184478495978],
		  [-2.9443359375, 5.620384866252641],
		  [-2.867431640625, 5.647718005233668],
		  [-2.76580810546875, 5.587583406107884],
		  [-2.7301025390625, 5.355187750782526],
		  [-2.779541015625, 5.352453150739988],
		  [-2.7829742431640625, 5.276680660689631],
		  [-2.77679443359375, 5.25890327940111],
		  [-2.76580810546875, 5.243860483222971],
		  [-2.7637481689453125, 5.218560418171606],
		  [-2.758941650390625, 5.20009756427037],
		  [-2.7500152587890625, 5.198729923899719],
		  [-2.74658203125, 5.1645379513162695],
		  [-2.7307891845703125, 5.141286355747783],
		  [-2.7431488037109375, 5.123505150776171],
		  [-2.76031494140625, 5.108459129273213],
		  [-2.7870941162109375, 5.118033911163583],
		  [-2.8035736083984375, 5.113930450742871],
		  [-2.8173065185546875, 5.105039529632952],
		  [-2.823486328125, 5.120769536822237],
		  [-2.83447265625, 5.124189052435081],
		  [-2.838592529296875, 5.109143047012258],
		  [-2.8516387939453125, 5.115298273806442],
		  [-2.867431640625, 5.128292447012573],
		  [-2.890777587890625, 5.133079707351237],
		  [-2.89215087890625, 5.123505150776171],
		  [-2.9278564453125, 5.1248729533619555],
		  [-2.948455810546875, 5.129660239345242],
		  [-2.9560089111328125, 5.105039529632952],
		  [-2.9724884033203125, 5.10025205950784],
		  [-2.9937744140625, 5.118717818675223],
		  [-3.0095672607421875, 5.124189052435081],
		  [-3.11187744140625, 5.139117160783533],
		  [-3.11187744140625, 5.0898755229548955],
		  [-2.7520751953125, 5.021478113350183],
		  [-2.27691650390625, 4.9065543621082375],
		  [-2.2487640380859375, 4.879306219346514],
		  [-2.245330810546875, 4.8546761104108125],
		  [-2.2075653076171875, 4.838255537896997],
		  [-2.204132080078125, 4.8211503512890435],
		  [-2.1759796142578125, 4.812255483935228],
		  [-2.1746063232421875, 4.801992031004971],
		  [-2.1718597412109375, 4.788307186898774],
		  [-2.1636199951171875, 4.796518126268445],
		  [-2.1553802490234375, 4.79378115744099],
		  [-2.1196746826171875, 4.787622937499694],
		  [-2.1086883544921875, 4.775990593079715],
		  [-2.11212158203125, 4.766410867141555],
		  [-2.11212158203125, 4.75683100764787],
		  [-2.097015380859375, 4.748619593412709],
		  [-2.0935821533203125, 4.737670889057711],
		  [-2.0798492431640625, 4.74656672457246],
		  [-2.0647430419921875, 4.744513849624847],
		  [-2.05718994140625, 4.739723784344284],
		  [-2.04345703125, 4.752725312760706],
		  [-1.9933319091796875, 4.757515287749456],
		  [-1.9850921630859375, 4.753409596941137],
		  [-1.9782257080078125, 4.755462445404653],
		  [-1.9713592529296875, 4.76777940760151],
		  [-1.9411468505859375, 4.78351742673601],
		  [-1.934967041015625, 4.808150121318067],
		  [-1.91436767578125, 4.814308155958491],
		  [-1.9136810302734375, 4.825939847021319],
		  [-1.89239501953125, 4.824571423116963],
		  [-1.8848419189453125, 4.832097720432811],
		  [-1.856689453125, 4.847150064208675],
		  [-1.8354034423828125, 4.848518442484756],
		  [-1.808624267578125, 4.869043783536398],
		  [-1.772918701171875, 4.87383293975394],
		  [-1.746826171875, 4.877937903630787],
		  [-1.7475128173828125, 4.8854636055353104],
		  [-1.7351531982421875, 4.886831905898856],
		  [-1.7420196533203125, 4.890252644583061],
		  [-1.745452880859375, 4.9011988908909405],
		  [-1.73858642578125, 4.918302041597345],
		  [-1.7049407958984375, 4.933352450864703],
		  [-1.7049407958984375, 4.94908660476962],
		  [-1.69189453125, 4.962084101934849],
		  [-1.643829345703125, 4.968657574204802],
		  [-1.630096435546875, 4.991915381636319],
		  [-1.619110107421875, 5.024748528593368],
		  [-1.355438232421875, 5.072627233101678],
		  [-1.3458251953125, 5.089041973101215],
		  [-1.23870849609375, 5.099984900524659],
		  [-1.175537109375, 5.139651445943173],
		  [-1.09588623046875, 5.184786233557572],
		  [-0.80474853515625, 5.2162419067060934],
		  [-0.7525634765625, 5.265473704920039],
		  [-0.723724365234375, 5.283250898132045],
		  [-0.72509765625, 5.296925315162276],
		  [-0.624847412109375, 5.3229058733002015],
		  [-0.6097412109375, 5.350252643389027],
		  [-0.495758056640625, 5.377598191153183],
		  [-0.462799072265625, 5.4295513422895],
		  [-0.406494140625, 5.470563827447078],
		  [-0.3350830078125, 5.504738751751842],
		  [-0.20599365234375, 5.5438452698044305],
		  [-0.02197265625, 5.609451251001029],
		  [0.06317138671875, 5.696914401910348],
		  [0.37078857421875, 5.787096826137783],
		  [0.89813232421875, 5.7788990149807],
		  [0.97503662109375, 5.833548839091356],
		  [0.98602294921875, 5.920977461018268],
		  [1.043701171875, 6.002929234128989],
		  [1.1370849609375, 6.087599783708456],
		  [1.20025634765625, 6.109448089560764],
		  [1.1865234375, 6.158134168061196],
		  [1.03271484375, 6.234589170386485],
		  [0.933837890625, 6.332872065842108],
		  [0.791015625, 6.442053330405442],
		  [0.714111328125, 6.5730398113581945],
		  [0.648193359375, 6.72581372578923],
		  [0.54931640625, 6.791273621594483],
		  [0.50537109375, 6.933072734145719],
		  [0.582275390625, 6.976694687480041],
		  [0.604248046875, 7.107536065343662],
		  [0.6591796875, 7.216542123820367],
		  [0.6591796875, 7.423580986248919],
		  [0.54931640625, 7.369106413086054],
		  [0.50537109375, 7.576073740079281],
		  [0.582275390625, 7.6849641597750145],
		  [0.648193359375, 7.80471136163048],
		  [0.59326171875, 7.967947633491558],
		  [0.582275390625, 8.18549455344362],
		  [0.7470703125, 8.27248024299783],
		  [0.68115234375, 8.392054181774837],
		  [0.59326171875, 8.533321348391821],
		  [0.362548828125, 8.772269406898898],
		  [0.54931640625, 8.848266300238533],
		  [0.439453125, 9.065313388771576],
		  [0.516357421875, 9.206323879509743],
		  [0.54656982421875, 9.33336736537918],
		  [0.56854248046875, 9.398406593067481],
		  [0.55206298828125, 9.422793157890089],
		  [0.525970458984375, 9.43634050546696],
		  [0.4998779296875, 9.434985794653103],
		  [0.503997802734375, 9.451241972902867],
		  [0.50262451171875, 9.474270244201993],
		  [0.4559326171875, 9.497296971037086],
		  [0.416107177734375, 9.494588024630845],
		  [0.3680419921875, 9.502714799563549],
		  [0.344696044921875, 9.494588024630845],
		  [0.336456298828125, 9.455305897552844],
		  [0.26092529296875, 9.430921630277611],
		  [0.2252197265625, 9.482397500805122],
		  [0.259552001953125, 9.476979351120892],
		  [0.2911376953125, 9.49052456485929],
		  [0.31036376953125, 9.509486964624676],
		  [0.284271240234375, 9.525739613539953],
		  [0.262298583984375, 9.520322149792745],
		  [0.23345947265625, 9.535219968242464],
		  [0.237579345703125, 9.574492913688278],
		  [0.262298583984375, 9.566367848610538],
		  [0.3350830078125, 9.578555373356105],
		  [0.358428955078125, 9.57178458024888],
		  [0.383148193359375, 9.588034256852247],
		  [0.37353515625, 9.611053299174694],
		  [0.38177490234375, 9.644901986299589],
		  [0.369415283203125, 9.669270937656893],
		  [0.3515625, 9.68010101615937],
		  [0.344696044921875, 9.718003538696156],
		  [0.319976806640625, 9.723417834658404],
		  [0.32684326171875, 9.761315449022936],
		  [0.330963134765625, 9.792442407297953],
		  [0.34332275390625, 9.816800600296395],
		  [0.352935791015625, 9.865511606965537],
		  [0.355682373046875, 9.922332011223736],
		  [0.391387939453125, 9.9426226271324],
		  [0.37078857421875, 9.962911983508498],
		  [0.362548828125, 10.033238632582115],
		  [0.37628173828125, 10.029181739964601],
		  [0.3955078125, 10.018363111339735],
		  [0.410614013671875, 10.022420139385279],
		  [0.416107177734375, 10.052170125837161],
		  [0.407867431640625, 10.072452638146375],
		  [0.372161865234375, 10.084621533545043],
		  [0.35430908203125, 10.088677729895336],
		  [0.355682373046875, 10.107605970344872],
		  [0.362548828125, 10.142755458159623],
		  [0.355682373046875, 10.177901088783987],
		  [0.361175537109375, 10.258991598864634],
		  [0.384521484375, 10.273855944422634],
		  [0.37353515625, 10.284665938597891],
		  [0.402374267578125, 10.315742609165545],
		  [0.384521484375, 10.315742609165545],
		  [0.3570556640625, 10.313040411637914],
		  [0.31585693359375, 10.310338190920042],
		  [0.339202880859375, 10.322498001489173],
		  [0.3350830078125, 10.340061342394424],
		  [0.319976806640625, 10.336008350847187],
		  [0.31585693359375, 10.358974610993034],
		  [0.292510986328125, 10.377886738430476],
		  [0.300750732421875, 10.410304867640694],
		  [0.28564453125, 10.425162051376178],
		  [0.25543212890625, 10.41300622645111],
		  [0.21697998046875, 10.425162051376178],
		  [0.20050048828125, 10.400322299710362],
		  [0.17578125, 10.438140403175062],
		  [0.142822265625, 10.521864103805452],
		  [0.0604248046875, 10.556967292045066],
		  [0.05767822265625, 10.597465990033827],
		  [-0.0494384765625, 10.63525994365502],
		  [-0.10162353515625, 10.702737493871993],
		  [-0.07415771484375, 10.713532510733474],
		  [-0.07415771484375, 10.76480357975497],
		  [-0.02197265625, 10.810670302696625],
		  [-0.02471923828125, 10.848437635560716],
		  [-0.0054931640625, 10.915867426529687],
		  [-0.0054931640625, 10.962500930136633],
		  [0.00823974609375, 10.963849158064976],
		  [0.0295257568359375, 10.973960671575778],
		  [0.0350189208984375, 10.983397772011523],
		  [0.0281524658203125, 11.056862003336118],
		  [0.0089263916015625, 11.079773691783673],
		  [-0.0034332275390625, 11.103357379441855],
		  [-0.01922607421875, 11.114811626350068],
		  [-0.042572021484375, 11.10537874980026],
		  [-0.06317138671875, 11.085164416708741],
		  [-0.0954437255859375, 11.089881219506323],
		  [-0.1263427734375, 11.10537874980026],
		  [-0.141448974609375, 11.10537874980026],
		  [-0.146942138671875, 11.11589596649572],
		  [-0.133209228515625, 11.137455600901948],
		  [-0.2801513671875, 11.179222845313173],
		  [-0.2911376953125, 11.148234819406285],
		  [-0.274658203125, 11.126675983142837],
		  [-0.3110504150390625, 11.116964511335615],
		  [-0.3357696533203125, 11.108542376871245],
		  [-0.34091949462890625, 11.086306774368971],
		  [-0.35396575927734375, 11.086306774368971],
		  [-0.35808563232421875, 11.069460495013146],
		  [-0.37078857421875, 11.08490120002543],
		  [-0.37353515625, 11.125328502868602],
		  [-0.39825439453125, 11.130718386566889],
		  [-0.428466796875, 11.119938519459785],
		  [-0.43670654296875, 11.081795225272437],
		  [-0.4387664794921875, 11.031926660994637],
		  [-0.4593658447265625, 11.028556857754126],
		  [-0.476531982421875, 11.039340092099271],
		  [-0.479278564453125, 11.02383906832552],
		  [-0.50262451171875, 11.01709923786892],
		  [-0.5074310302734375, 10.988790265407673],
		  [-0.528717041015625, 10.999574956510521],
		  [-0.5417633056640625, 10.990812425026844],
		  [-0.545196533203125, 10.9759829327661],
		  [-0.5500030517578125, 10.991486475153192],
		  [-0.5678558349609375, 10.99350861629086],
		  [-0.58502197265625, 10.965197379847382],
		  [-0.594635009765625, 10.924748055804807],
		  [-0.6172943115234375, 10.911263721810856],
		  [-0.6227874755859375, 10.937557605772177],
		  [-0.6488800048828125, 10.947670017497623],
		  [-0.6427001953125, 10.953737298844484],
		  [-0.6543731689453125, 10.964523269724461],
		  [-0.660552978515625, 10.955085566703993],
		  [-0.6708526611328125, 10.962500930136633],
		  [-0.6591796875, 10.97463476017718],
		  [-0.6516265869140625, 10.977331099202617],
		  [-0.652313232421875, 10.987442151295708],
		  [-0.6735992431640625, 10.992160523739365],
		  [-0.6777191162109375, 10.982049633269774],
		  [-0.6859588623046875, 10.988116209121543],
		  [-0.685272216796875, 10.998226891692575],
		  [-0.8074951171875, 10.997552856971954],
		  [-0.8054351806640625, 11.006315188111143],
		  [-0.82672119140625, 11.009011237576388],
		  [-0.8301544189453125, 10.998900924872125],
		  [-0.8548736572265625, 10.998900924872125],
		  [-0.8713531494140625, 10.96587148843361],
		  [-0.885772705078125, 10.963175044869002],
		  [-0.8878326416015625, 10.978679259486007],
		  [-0.9166717529296875, 10.980701488372368],
		  [-0.9173583984375, 11.002271067650755],
		  [-1.001129150390625, 10.998900924872125],
		  [-1.001129150390625, 11.007663215928416],
		  [-1.1144256591796875, 11.005641171889241],
		  [-1.116485595703125, 10.986768091930216],
		  [-1.388397216796875, 10.985419968580738],
		  [-1.4247894287109375, 11.021817135401466],
		  [-1.6156768798828125, 11.021143154671575],
		  [-1.616363525390625, 10.984071839073803],
		  [-1.690521240234375, 10.985419968580738],
		  [-1.6912078857421875, 10.97126430179276],
		  [-1.750946044921875, 10.97193839654495],
		  [-1.7502593994140625, 10.984745904596913],
		  [-2.8399658203125, 11.014582292843404]]])


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

			col_mean = ee.ImageCollection(l578NDWI).reduce(ee.Reducer.mean())

			col_std = ee.ImageCollection(l578NDWI).reduce(ee.Reducer.stdDev())
			
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

			col_mean = ee.ImageCollection(l578NDVI).reduce(ee.Reducer.mean())

			col_std = ee.ImageCollection(l578NDVI).reduce(ee.Reducer.stdDev())
			
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




		max = ee.Image(selected_LST).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo().get("LST_Day_1km")

		min = ee.Image(selected_LST).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo().get("LST_Day_1km")

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
		max = ee.Image(selected_LST).reduceRegion(ee.Reducer.max(), region_Gh, 3000).getInfo().get("SR")
		print(max)
		min = ee.Image(selected_LST).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo().get("SR")
	
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

			total_col = ee.ImageCollection(ee.ImageCollection(l5images).merge(l7images)).merge(l8images)

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

			l578NDVI = ee.ImageCollection(ee.ImageCollection(l5images).merge(l7images)).merge(l8images)
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
			max=ee.Image(SMI).reduceRegion(ee.Reducer.percentile([90]), region_Gh, 300).getInfo()['NDVI']
			min=ee.Image(SMI).reduceRegion(ee.Reducer.min(), region_Gh, 3000).getInfo()['NDVI']
			print(min,max)


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





	
	
