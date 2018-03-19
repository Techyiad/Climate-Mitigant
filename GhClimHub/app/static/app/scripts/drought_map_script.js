


$(document).ready(function () {
	$('#md1').find('a').trigger('click');
});





var palete = {
	'ndvi_anomaly': ["87000A", "7C3E28", "EC712C", "FABF45", "FFFFFF", "51FF78", "3DCF4C", "215229"], 'ndwi_anomaly': ["#e20000 ", "32cd32", "ffff00", "ff8c00", "#00f9f9", "#3570dd", "0000ff"], 'vhi': ['#087702', '#52f904', '#ffee00', '#ff7700', '#ef0404'], 'smi': ['#730000', '#E60000', '#FFAA00', '#FCD37F', '#FFFF00', '#FFFFFF', '#AAFF55', '#00FFFF', '#00AAFF', '#0000FF', '#0000AA'], 'lst': ["0000ff", "32cd32", "ffff00", "ff8c00", "#e20000 "], 'precipitation': ['#730000', '#E60000', '#FFAA00', '#FCD37F', '#FFFF00', '#FFFFFF', '#AAFF55', '#00FFFF', '#00AAFF', '#0000FF', '#0000AA'], 'spi': ['#730000', '#E60000', '#FFAA00', '#FCD37F', '#FFFF00', '#FFFFFF', '#AAFF55', '#00FFFF', '#00AAFF', '#0000FF', '#0000AA']
}





function action_downloadMap(downloadURL) {

	if (downloadURL != null) {

		$("#downloadURL").val(downloadURL);

		$("#downloadURLLink").attr("href", downloadURL);
		$("#downloadURLModal").click();
		$("#downloadURLModal").modal('show');


	} 
};






var styles = {
	default: null,
	silver: [
		{
			"featureType": "administrative",
			"elementType": "labels.text.fill",
			"stylers": [
				{
					"color": "#444444"
				}
			]
		},
		{
			"featureType": "landscape",
			"elementType": "all",
			"stylers": [
				{
					"color": "#f2f2f2"
				}
			]
		},
		{
			"featureType": "poi",
			"elementType": "all",
			"stylers": [
				{
					"visibility": "off"
				}
			]
		},
		{
			"featureType": "road",
			"elementType": "all",
			"stylers": [
				{
					"saturation": -100
				},
				{
					"lightness": 45
				}
			]
		},
		{
			"featureType": "road.highway",
			"elementType": "all",
			"stylers": [
				{
					"visibility": "simplified"
				}
			]
		},
		{
			"featureType": "road.arterial",
			"elementType": "labels.icon",
			"stylers": [
				{
					"visibility": "off"
				}
			]
		},
		{
			"featureType": "transit",
			"elementType": "all",
			"stylers": [
				{
					"visibility": "off"
				}
			]
		},
		{
			"featureType": "water",
			"elementType": "all",
			"stylers": [
				{
					"color": "#46bcec"
				},
				{
					"visibility": "on"
				}
			]
		}
	],

	night: [
		{ elementType: 'geometry', stylers: [{ color: '#242f3e' }] },
		{ elementType: 'labels.text.stroke', stylers: [{ color: '#242f3e' }] },
		{ elementType: 'labels.text.fill', stylers: [{ color: '#746855' }] },
		{
			featureType: 'administrative.locality',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#d59563' }]
		},
		{
			featureType: 'poi',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#d59563' }]
		},
		{
			featureType: 'poi.park',
			elementType: 'geometry',
			stylers: [{ color: '#263c3f' }]
		},
		{
			featureType: 'road',
			elementType: 'labels.icons',
			stylers: [{ visibility: 'off' }]
		}
		,
		{
			featureType: 'poi.park',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#6b9a76' }]
		},
		{
			featureType: 'road',
			elementType: 'geometry',
			stylers: [{ color: '#38414e' }]
		},
		{
			featureType: 'road',
			elementType: 'geometry.stroke',
			stylers: [{ color: '#212a37' }]
		},
		{
			featureType: 'road',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#9ca5b3' }]
		},
		{
			featureType: 'road.highway',
			elementType: 'geometry',
			stylers: [{ color: '#746855' }]
		},
		{
			featureType: 'road.highway',
			elementType: 'geometry.stroke',
			stylers: [{ color: '#1f2835' }]
		},
		{
			featureType: 'road.highway',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#f3d19c' }]
		},
		{
			featureType: 'transit',
			elementType: 'geometry',
			stylers: [{ color: '#2f3948' }]
		},
		{
			featureType: 'transit.station',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#d59563' }]
		},
		{
			featureType: 'water',
			elementType: 'geometry',
			stylers: [{ color: '#17263c' }]
		},
		{
			featureType: 'water',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#515c6d' }]
		},
		{
			featureType: 'water',
			elementType: 'labels.text.stroke',
			stylers: [{ color: '#17263c' }]
		}
	],

	retro: [
		{ elementType: 'geometry', stylers: [{ color: '#ebe3cd' }] },
		{ elementType: 'labels.text.fill', stylers: [{ color: '#523735' }] },
		{ elementType: 'labels.text.stroke', stylers: [{ color: '#f5f1e6' }] },
		{
			featureType: 'administrative',
			elementType: 'geometry.stroke',
			stylers: [{ color: '#c9b2a6' }]
		},
		{
			featureType: 'administrative.land_parcel',
			elementType: 'geometry.stroke',
			stylers: [{ color: '#dcd2be' }]
		},
		{
			featureType: 'administrative.land_parcel',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#ae9e90' }]
		},
		{
			featureType: 'landscape.natural',
			elementType: 'geometry',
			stylers: [{ color: '#dfd2ae' }]
		},
		{
			featureType: 'poi',
			elementType: 'geometry',
			stylers: [{ color: '#dfd2ae' }]
		},
		{
			featureType: 'poi',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#93817c' }]
		},
		{
			featureType: 'poi.park',
			elementType: 'geometry.fill',
			stylers: [{ color: '#a5b076' }]
		},
		{
			featureType: 'poi.park',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#447530' }]
		},
		{
			featureType: 'road',
			elementType: 'geometry',
			stylers: [{ color: '#f5f1e6' }]
		},
		{
			featureType: 'road.arterial',
			elementType: 'geometry',
			stylers: [{ color: '#fdfcf8' }]
		},
		{
			featureType: 'road.highway',
			elementType: 'geometry',
			stylers: [{ color: '#f8c967' }]
		},
		{
			featureType: 'road.highway',
			elementType: 'geometry.stroke',
			stylers: [{ color: '#e9bc62' }]
		},
		{
			featureType: 'road.highway.controlled_access',
			elementType: 'geometry',
			stylers: [{ color: '#e98d58' }]
		},
		{
			featureType: 'road.highway.controlled_access',
			elementType: 'geometry.stroke',
			stylers: [{ color: '#db8555' }]
		},
		{
			featureType: 'road',
			elementType: 'labels.icons',
			stylers: [{ visibility: 'off' }]
		}
		,
		{
			featureType: 'transit.line',
			elementType: 'geometry',
			stylers: [{ color: '#dfd2ae' }]
		},
		{
			featureType: 'transit.line',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#8f7d77' }]
		},
		{
			featureType: 'transit.line',
			elementType: 'labels.text.stroke',
			stylers: [{ color: '#ebe3cd' }]
		},
		{
			featureType: 'transit.station',
			elementType: 'geometry',
			stylers: [{ color: '#dfd2ae' }]
		},
		{
			featureType: 'water',
			elementType: 'geometry.fill',
			stylers: [{ color: '#b9d3c2' }]
		},
		{
			featureType: 'water',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#92998d' }]
		}
	],

	javis: [
		{
			"stylers": [
				{
					"hue": "#2c3e50"
				},
				{
					"saturation": 250
				}
			]
		},
		{
			"featureType": "road",
			"elementType": "geometry",
			"stylers": [
				{
					"lightness": 50
				},
				{
					"visibility": "simplified"
				}
			]
		},
		{
			"featureType": "road",
			"elementType": "labels",
			"stylers": [
				{
					"visibility": "off"
				}
			]
		}
	],

	hiding: [
		{
			featureType: 'poi.business',
			stylers: [{ visibility: 'off' }]
		},
		{
			featureType: 'transit',
			elementType: 'labels.icon',
			stylers: [{ visibility: 'off' }]
		}
	]
};


var Ghana = { lat: 7.9465, lng: -1.0232 };


styleRetro = new google.maps.StyledMapType(styles.silver, { name: 'silver' })

var map1 = new google.maps.Map(document.getElementById('map1'), {
	center: Ghana,
	zoom: 6,
	styles: styles.silver,
	streetViewControl: false
});


var map = new google.maps.Map(document.getElementById('map'), {
	center: Ghana,
	zoom: 7,
	styles: styles.javis,
	streetViewControl: false,
	mapTypeControl: false
});


var map2 = new google.maps.Map(document.getElementById('map2'), {
	center: Ghana,
	zoom: 6,
	styles: styles.silver,
	streetViewControl: false
});

var map3 = new google.maps.Map(document.getElementById('map3'), {
	center: Ghana,
	zoom: 6,
	styles: styles.silver,
	streetViewControl: false
});


var map4 = new google.maps.Map(document.getElementById('map4'), {
	center: Ghana,
	zoom: 6,
	styles: styles.silver,
	streetViewControl: false
});


function removeAllFusionTablesFromMap(fusion_tables) {
	if (fusion_tables) {
		for (var i = 0; i <fusion_tables.length; i++) {
			if (fusion_tables[i].length !== 0) {
				fusion_tables[i].setMap(null);
			}
		}
	}
}









function CenterControl1(controlDiv, map) {

	// Set CSS for the control border.
	var controlUI = document.createElement('div');
	controlUI.style.backgroundColor = 'rgb(244, 72, 66)';
	controlUI.style.border = '2px solid #fff';
	controlUI.style.borderRadius = '3px';
	controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
	controlUI.style.cursor = 'pointer';
	controlUI.style.marginBottom = '22px';
	controlUI.style.textAlign = 'center';
	controlUI.title = 'Click to recenter the map';
	controlDiv.appendChild(controlUI);

	// Set CSS for the control interior.
	var controlText = document.createElement('div');
	controlText.style.color = '#fff';
	controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
	controlText.style.fontSize = '16px';
	controlText.style.lineHeight = '38px';
	controlText.style.paddingLeft = '5px';
	controlText.style.paddingRight = '5px';
	controlText.innerHTML = 'Alpha Map';
	controlUI.appendChild(controlText);

	// Setup the click event listeners: simply set the map to Chicago.
	controlUI.addEventListener('click', function () {
		map.setCenter(Ghana,7);
	});

}

function CenterControl2(controlDiv, map) {

	// Set CSS for the control border.
	var controlUI = document.createElement('div');
	controlUI.style.backgroundColor = 'rgb(15, 142, 22)';
	controlUI.style.border = '2px solid #fff';
	controlUI.style.borderRadius = '3px';
	controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
	controlUI.style.cursor = 'pointer';
	controlUI.style.marginBottom = '22px';
	controlUI.style.textAlign = 'center';
	controlUI.title = 'Click to recenter the map';
	controlDiv.appendChild(controlUI);

	// Set CSS for the control interior.
	var controlText = document.createElement('div');
	controlText.style.color = '#fff';
	controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
	controlText.style.fontSize = '16px';
	controlText.style.lineHeight = '38px';
	controlText.style.paddingLeft = '5px';
	controlText.style.paddingRight = '5px';
	controlText.innerHTML = 'Beta Map';
	controlUI.appendChild(controlText);

	// Setup the click event listeners: simply set the map to Chicago.
	controlUI.addEventListener('click', function () {
		map.setCenter(Ghana,7);
	});

}

function CenterControl3(controlDiv, map) {

	// Set CSS for the control border.
	var controlUI = document.createElement('div');
	controlUI.style.backgroundColor = 'rgb(198, 145, 9)';
	controlUI.style.border = '2px solid #fff';
	controlUI.style.borderRadius = '3px';
	controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
	controlUI.style.cursor = 'pointer';
	controlUI.style.marginBottom = '22px';
	controlUI.style.textAlign = 'center';
	controlUI.title = 'Click to recenter the map';
	controlDiv.appendChild(controlUI);

	// Set CSS for the control interior.
	var controlText = document.createElement('div');
	controlText.style.color = '#fff';
	controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
	controlText.style.fontSize = '16px';
	controlText.style.lineHeight = '38px';
	controlText.style.paddingLeft = '5px';
	controlText.style.paddingRight = '5px';
	controlText.innerHTML = 'Delta Map';
	controlUI.appendChild(controlText);

	// Setup the click event listeners: simply set the map to Chicago.
	controlUI.addEventListener('click', function () {
		map.setCenter(Ghana,7);
	});

}

function CenterControl4(controlDiv, map) {

	// Set CSS for the control border.
	var controlUI = document.createElement('div');
	controlUI.style.backgroundColor = 'rgb(13, 188, 219)';
	controlUI.style.border = '2px solid #fff';
	controlUI.style.borderRadius = '3px';
	controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
	controlUI.style.cursor = 'pointer';
	controlUI.style.marginBottom = '22px';
	controlUI.style.textAlign = 'center';
	controlUI.title = 'Click to recenter the map';
	controlDiv.appendChild(controlUI);

	// Set CSS for the control interior.
	var controlText = document.createElement('div');
	controlText.style.color = '#fff';
	controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
	controlText.style.fontSize = '16px';
	controlText.style.lineHeight = '38px';
	controlText.style.paddingLeft = '5px';
	controlText.style.paddingRight = '5px';
	controlText.innerHTML = 'Omega Map';
	controlUI.appendChild(controlText);

	// Setup the click event listeners: simply set the map to Chicago.
	controlUI.addEventListener('click', function () {
		map.setCenter(Ghana,7);
	});

}

// Create the DIV to hold the control and call the CenterControl()
// constructor passing in this DIV.
var centerControlDiv1 = document.createElement('div');
var centerControlDiv2 = document.createElement('div');
var centerControlDiv3 = document.createElement('div');
var centerControlDiv4 = document.createElement('div');
var centerControl1 = new CenterControl1(centerControlDiv1, map1);
var centerControl2 = new CenterControl2(centerControlDiv2, map2);
var centerControl3 = new CenterControl3(centerControlDiv3, map3);
var centerControl4 = new CenterControl4(centerControlDiv4, map4);





centerControlDiv1.index = 1;
centerControlDiv2.index = 1;
centerControlDiv3.index = 1;
centerControlDiv4.index = 1;

map1.controls[google.maps.ControlPosition.TOP_CENTER].push(centerControlDiv1);

map2.controls[google.maps.ControlPosition.TOP_CENTER].push(centerControlDiv2);

map3.controls[google.maps.ControlPosition.TOP_CENTER].push(centerControlDiv3);

map4.controls[google.maps.ControlPosition.TOP_CENTER].push(centerControlDiv4);


clearPolygon = function (currentPolygon) {
	currentPolygon.setMap(null);
	currentPolygon = null;


};



// Create the legend and display on the map

/*




var legend = document.createElement('div');
legend.id = 'legend';
var content = [];
content.push('<h3>Legend*</h3>');
content.push('<p><div class="color red"></div>Battus</p>');
content.push('<p><div class="color yellow"></div>Speyeria</p>');
content.push('<p><div class="color green"></div>Papilio</p>');
content.push('<p><div class="color blue"></div>Limenitis</p>');
content.push('<p><div class="color purple"></div>Myscelia</p>');


legend.innerHTML = content.join('');


legend.index = 1;

*/




//map.controls[google.maps.ControlPosition.LEFT_BOTTOM].push(legend);


var data = [0, 1, 3, 5, 7, 8, 10, 13, 15, 20];
var min = d3.min(data);
var mean = d3.sum(data) / data.length;
var max = d3.max(data);

// quantile scale
var redBlueScale1 = ["rgb(103, 0, 31)", "rgb( 178, 24, 43)", "rgb( 214, 96, 77)", "rgb( 244, 165, 130)", "rgb( 253, 219, 199)", "rgb( 209, 229, 240)", "rgb( 146, 197, 222)", "rgb( 67, 147, 195)", "rgb( 33, 102, 172)", "rgb( 5, 48, 97)"];


var qScale1 = d3.scale.quantile()
	.domain([min, mean, max])
	.range(redBlueScale1);
// console.log(qScale.domain());




//colorlegend("#key", qScale1, "quantile", { title: "NDVI Anomaly", boxHeight: 35, boxWidth: 90 });		  


// Fusion Table






//d3.select('#timeslider').call(d3.slider().scale(d3.time.scale().domain([new Date(2000, 1, 1), new Date(2018, 1, 1)])).axis(d3.svg.axis()).snap(true)
//	.on("slide", function (evt, value) {

//		d3.select('#slidertextmin').text(value[0]);
//		d3.select('#slider3textmax').text(value[1]);

//	})
//);

var start_series_date, end_series_date

var mySlider = new rSlider({
	target: '#timeslider',
	values: [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009, 2010, 2011,2012,2013,2014,2015,2016,2017,2018],
	range: true, // range slider
	set: [2000,2017], // an array of preselected values
	width: null,
	scale: true,
	labels: false,
	tooltip: true,
	step: null, // step size
	disabled: false, // is disabled?
	onChange: function (values) {
		start_series_date = values .slice(0,4)
		end_series_date = values.slice(5,9) 

	
	}// callback
});



function addlayer(name) {


	var layer = new google.maps.FusionTablesLayer({
		query: {
			select: 'geometry',
			from: '1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr',
			where: "name IN ('" + name + "')"


		},
		styles: [{
			polygonOptions: {
				fillColor: '#4408ea',
				fillOpacity: 0.4
			}
		
		}]
	});

	return layer
}


function addpolylayer(name) {


	var layer = new google.maps.FusionTablesLayer({
		query: {
			select: 'geometry',
			from: '1wF4uSA3CSYaCa9g93FRNXcL01-ThklMXRu92h-Vr',
			where: "name IN ('" + name + "')"


		},
		styles: [{
			polygonOptions: {
				fillOpacity: -1,
				strokeColor: '#f90000',
				strokeOpacity: 1,
				strokeWeight: 2
			}

		}]
	});

	return layer
}


var layer;

$('#region1').change(function () {


	var eventTypeName = $("#region1 option:selected").val();

	var storeName = eventTypeName.replace(/'/g, '\\\'');

	if (layer != null) {



		layer.setMap(null);

	}


	layer = addlayer(storeName)


	layer.setMap(map)


})

var layer1;
$('#region2').change(function () {
	var eventTypeName = $("#region2 option:selected").val();

	var storeName = eventTypeName.replace(/'/g, '\\\'');

	if (layer1 != null) {



		layer1.setMap(null);

	}

	 layer1 = addlayer(storeName)

	layer1.setMap(map1)


})

var layer2;
$('#region3').change(function () {
	var eventTypeName = $("#region3 option:selected").val();

	var storeName = eventTypeName.replace(/'/g, '\\\'');

	if (layer2 != null) {



		layer2.setMap(null);

	}

	layer2 = addlayer(storeName)

	layer2.setMap(map2)


})

var layer3;
$('#region4').change(function () {
	var eventTypeName = $("#region4 option:selected").val();

	var storeName = eventTypeName.replace(/'/g, '\\\'');

	if (layer3 != null) {



		layer3.setMap(null);

	}

	layer3 = addlayer(storeName)
	
	layer3.setMap(map3)


})

var layer4
$('#region5').change(function () {
	var eventTypeName = $("#region5 option:selected").val();

	var storeName = eventTypeName.replace(/'/g, '\\\'');

	if (layer4 != null) {



		layer4.setMap(null);

	}

	layer4 = addlayer(storeName)

	layer4.setMap(map4)


})





var twoDimensionalArray;

var shapepoly;


var polyOptions = {
	strokeWeight: 0,
	fillOpacity: 0.45,
	editable: true,
	fillColor: '#FF1493'
}





var drawingManager;

$('#poly_map').click(function () {

	window.drawingManager = new google.maps.drawing.DrawingManager({
		drawingMode: google.maps.drawing.OverlayType.POLYGON,
		drawingControl: true,
		drawingControlOptions: {
			position: google.maps.ControlPosition.RIGHT_BOTTOM,
			drawingModes: ['polygon']
		},
		circleOptions: {
			strokeWeight: 0,
			fillOpacity: 0.45,
			editable: true,
			fillColor: '#FF1493'
		},
		polygonOptions: polyOptions

	});

	//map.overlayMapTypes.clear()

	

		drawingManager.setMap(map);
		

		google.maps.event.addListener(drawingManager, 'polygoncomplete', function (polygon) {
			twoDimensionalArray = null;
			shapepoly = null;
			drawingManager.setDrawingMode(null);
			var arr = [];

			var points = polygon.getPath().getArray();
			shapepoly = polygon;
			twoDimensionalArray = points.map(function (point) {
				return [point.lng(), point.lat()];
			});

			console.log(twoDimensionalArray)


		});

})

function getCoordinates(rect) {
	var bounds = rect.getBounds();

	var g = [
		bounds.getSouthWest().lng(),
		bounds.getSouthWest().lat(),
		bounds.getNorthEast().lng(),
		bounds.getNorthEast().lat(),
	].join(',');

	console.log(g)
	return g
}


var marker_point, marker;

$('#series_marker').click(function (event) {


marker = new google.maps.Marker({
	position: Ghana,
	draggable: true,
	animation: google.maps.Animation.DROP,
	map: map
	});



	marker_point = [parseFloat(marker.getPosition().lng().toFixed(6)), parseFloat(marker.getPosition().lat().toFixed(6))];

	 $('#savedata').val(marker_point);


	 google.maps.event.addListener(marker, "dragend", function () {

		 marker_point = [parseFloat(marker.getPosition().lng().toFixed(6)), parseFloat(marker.getPosition().lat().toFixed(6))];
		 $("#savedata").val(marker_point)

	 });


	var contentString = '<div> <h3>Region Of Interest(ROI)</h3> <br/> <p>Drag the Red Marker To the an area of interest to perform timeseries on</p> <br/> <p> ROI must be within  Ghana</p>   </div>';



	var infowindow = new google.maps.InfoWindow({
		content: contentString
	});
	infowindow.open(map,marker);

})



//console.log(getCoordinates(rectangle))
//google.maps.event.addListener(map1, "center_changed", function (event) {



//	var latlong = map1.getCenter();
//	var lat = map1.getCenter().lat();
//	var lng = map1.getCenter().lng();

//	console.log(lng)
//	latlong = new google.maps.LatLng(parseFloat(lat),parseFloat(lng))
//	console.log(latlong)

//	map2.setCenter(latlong);

//	map3.setCenter(latlong);

//	map4.setCenter(latlong);


//});


//google.maps.event.addListener(map2, "center_changed", function (event) {



//	var latlong = map2.getCenter();
	

//	map1.setCenter(latlong);

//	map3.setCenter(latlong);
	
//	map4.setCenter(latlong);
	

//});



//google.maps.event.addListener(map3, "center_changed", function (event) {



//	var latlong = map3.getCenter();

//	map2.setCenter(latlong);
	
//	map1.setCenter(latlong);
	
//	map4.setCenter(latlong);
	

//});



//google.maps.event.addListener(map4, "center_changed", function (event) {



//	var latlong = map4.getCenter();


//	map2.setCenter(latlong);

//	map3.setCenter(latlong);

//	map1.setCenter(latlong);
	

//});


$('#clear_poly').click(function () {


	if (shapepoly != null) {
		clearPolygon(shapepoly);
	}



})

$('#clear_marker').click(function () {
	console.log("heey")

	marker.setMap(null)


})

// Indices Compute for Map
$(document).on('submit', '#indices_compute_form', function (e) {
	e.preventDefault();
	// document.getElementById("overlay").style.display = "block";

	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' });
	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' }); setTimeout(function () { waitingDialog.hide(); }, 2000);

	waitingDialog.show('This Computation Requires large Computing power and might take some time', {

		// if the option is set to boolean false, it will hide the header and "message" will be set in a paragraph above the progress bar.
		// When headerText is a not-empty string, "message" becomes a content above the progress bar and headerText string will be set as a text inside the H3;
		headerText: 'Computing Data',

		// this will generate a heading corresponding to the size number
		headerSize: 4,

		// extra class(es) for the header tag
		headerClass: '',

		// bootstrap postfix for dialog size, e.g. "sm", "m"
		dialogSize: 'lg',

		// bootstrap postfix for progress bar type, e.g. "success", "warning";
		progressType: 'success',

		// determines the tag of the content element
		contentElement: 'p',

		// extra class(es) for the content tag
		contentClass: 'content'

	});


	$.ajax({
		type: 'POST',
		url: '/indices_compute',
		data: {

			date_year:parseInt($('#year_indices').val()),
			date_month:parseInt($('#month_indices').val()),
			indices: $("#datasource_spi option:selected").val(),
			region_selected: $("#region1 option:selected").val().replace(/'/g, '\\\''),
			satelite: $("#satelite option:selected").val().replace(/'/g, '\\\''),
			region: JSON.stringify(twoDimensionalArray),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
		},
		success: function () {
			map.overlayMapTypes.clear();
	
			$.ajax({
				method: "GET",
				url: '/indices_compute',
				dataType: 'json',
				success: function (data) {
					if (data.mapid!=null) {
						map.controls[google.maps.ControlPosition.LEFT_BOTTOM].clear()
						if (shapepoly != null) {
							clearPolygon(shapepoly);
						}

						twoDimensionalArray = null;
					
						if (layer != null) {



							layer.setMap(null);

						}


						mapType = new google.maps.ImageMapType(updateMapTileOptions(data.mapid, data.token));
						// Add the EE layer to the map.



						map.overlayMapTypes.push(mapType);




						waitingDialog.hide()


						var redBlueScale;

						var qScale;

						if (data.type == 'ndvi_anomaly') {
							redBlueScale = palete.ndvi_anomaly
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'ndwi_anomaly') {
							redBlueScale = palete.ndwi_anomaly
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'precipitation') {

							redBlueScale = palete.precipitation

							qScale = d3.scale.quantile()
								.range(redBlueScale);

						} else if (data.type == 'lst') {
							redBlueScale = palete.lst
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'smi') {
							redBlueScale = palete.smi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'vhi') {
							redBlueScale = palete.vhi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'spi') {
							redBlueScale = palete.spi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						}




						

						var legend = document.createElement('div');
						legend.id = 'legend';
						legend.className = "leg"
						legend.setAttribute("style","	border-radius: 5px;background: white;padding: 5px;margin: 10px;z-index:1;width:220px;height:300px;transition: all 0.5s ease  0.5s !important;")

		

						colorlegend("#legend",legend, qScale, "quantile", data.type, { title: "", boxHeight: 60, boxWidth: 65 });
						legend.index =1;
						map.controls[google.maps.ControlPosition.LEFT_BOTTOM].push(legend);

						var eventType = $("#region1 option:selected").val();

						var layerName = eventType.replace(/'/g, '\\\'');


						layer = addpolylayer(layerName)


						layer.setMap(map)

					} else {
						waitingDialog.hide();
						$("#alBox").al({

							// default, success, warning, error
							context: "default",

							text: {

								// The title bar of your alert
								title: "Error Computing Data",

								// The more verbose description of the alert.
								description: data.error,

								hr: "",
								// The text of the "dismiss" button
								dismiss: "DISMISS"
							},

							classes: {

								// Classes to be added to #alBox
								container: "",

								// Classes to be added to #alBox-panel
								panel: "",

								// Classes to be added to #alBox-title
								title: "",

								// Classes to be added to #alBox-description
								description: "",

								// Classes to be added to the hr element above the dismiss button
								hr: "",

								// Classes to be added to the dismiss button
								dismiss: ""
							},

							// The number of seconds your alert will appear. 
							// Can also define as "infinite" to stay on screen until dismissal.
							seconds: "infinite",

							// URL Location to redirect after the alert is done
							redirect: ""

							});
				
						
					}
		
				},
				error: function () {
					alert("Not Good");
				}


			})

		},
		error: function (data) {

			waitingDialog.hide()


		}

	});

});


// Indices Compute for Map1
$(document).on('submit', '#indices_series_form1', function (e) {
	e.preventDefault();
	// document.getElementById("overlay").style.display = "block";

	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' });
	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' }); setTimeout(function () { waitingDialog.hide(); }, 2000);

	waitingDialog.show('This Computation Requires large Computing power and might take some time', {

		// if the option is set to boolean false, it will hide the header and "message" will be set in a paragraph above the progress bar.
		// When headerText is a not-empty string, "message" becomes a content above the progress bar and headerText string will be set as a text inside the H3;
		headerText: 'Computing Data',

		// this will generate a heading corresponding to the size number
		headerSize: 4,

		// extra class(es) for the header tag
		headerClass: '',

		// bootstrap postfix for dialog size, e.g. "sm", "m"
		dialogSize: 'lg',

		// bootstrap postfix for progress bar type, e.g. "success", "warning";
		progressType: 'success',

		// determines the tag of the content element
		contentElement: 'p',

		// extra class(es) for the content tag
		contentClass: 'content'

	});


	$.ajax({
		type: 'POST',
		url: '/map1',
		data: {


			date_year: parseInt($('#year_indices').val()),
			date_month: parseInt($('#month_indices').val()),
			indices: $("#comp_indices option:selected").val(),
			region_selected: $("#region2 option:selected").val().replace(/'/g, '\\\''),
			satelite: $("#satelite1 option:selected").val().replace(/'/g, '\\\''),
			region: JSON.stringify(twoDimensionalArray),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
		},
		success: function () {
			map1.overlayMapTypes.clear();
			map1.controls[google.maps.ControlPosition.LEFT_BOTTOM].clear()
			$.ajax({
				method: "GET",
				url: '/map1',
				dataType: 'json',
				success: function (data) {

					if (data.mapid != null) {

						if (shapepoly != null) {
							clearPolygon(shapepoly);
						}

						twoDimensionalArray = null;

						if (layer1 != null) {



							layer1.setMap(null);

						}


						mapType = new google.maps.ImageMapType(updateMapTileOptions(data.mapid, data.token));
						// Add the EE layer to the map.



						map1.overlayMapTypes.push(mapType);




						waitingDialog.hide()


						var redBlueScale;

						var qScale;

						if (data.type == 'ndvi_anomaly') {
							redBlueScale = palete.ndvi_anomaly
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'ndwi_anomaly') {
							redBlueScale = palete.ndwi_anomaly
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'precipitation') {

							redBlueScale = palete.precipitation
							qScale = d3.scale.quantile()
								.range(redBlueScale);

						} else if (data.type == 'lst') {
							redBlueScale = palete.lst
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'smi') {
							redBlueScale = palete.smi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'vhi') {
							redBlueScale = palete.vhi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'spi') {
							redBlueScale = palete.spi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						}










						var legend = document.createElement('div');
						legend.id = 'legend';
						legend.className = "leg"
						legend.setAttribute("style", "	border-radius: 5px;background: white;padding: 5px;margin: 10px;z-index:1;width:220px;height:300px;transition: all 0.5s ease  0.5s !important;")



						colorlegend("#legend", legend, qScale, "quantile", data.type, { title: "", boxHeight: 60, boxWidth: 65 });
						legend.index = 1;
			
						map1.controls[google.maps.ControlPosition.LEFT_BOTTOM].push(legend);

						var eventType = $("#region2 option:selected").val();

						var layerName = eventType.replace(/'/g, '\\\'');


						layer = addpolylayer(layerName)


						layer.setMap(map1)

					} else {
						waitingDialog.hide();
						$("#alBox").al({

							// default, success, warning, error
							context: "default",

							text: {

								// The title bar of your alert
								title: "Error Computing Data",

								// The more verbose description of the alert.
								description: data.error,

								hr: "",
								// The text of the "dismiss" button
								dismiss: "DISMISS"
							},

							classes: {

								// Classes to be added to #alBox
								container: "",

								// Classes to be added to #alBox-panel
								panel: "",

								// Classes to be added to #alBox-title
								title: "",

								// Classes to be added to #alBox-description
								description: "",

								// Classes to be added to the hr element above the dismiss button
								hr: "",

								// Classes to be added to the dismiss button
								dismiss: ""
							},

							// The number of seconds your alert will appear. 
							// Can also define as "infinite" to stay on screen until dismissal.
							seconds: "infinite",

							// URL Location to redirect after the alert is done
							redirect: ""

							});


					}

				},
				error: function () {
					alert("Not Good");
				}


			})

		},
		error: function (data) {

			waitingDialog.hide()



		}

	});

});






// Indices Compute for Map2
$(document).on('submit', '#indices_series_form2', function (e) {
	e.preventDefault();
	// document.getElementById("overlay").style.display = "block";

	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' });
	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' }); setTimeout(function () { waitingDialog.hide(); }, 2000);

	waitingDialog.show('This Computation Requires large Computing power and might take some time', {

		// if the option is set to boolean false, it will hide the header and "message" will be set in a paragraph above the progress bar.
		// When headerText is a not-empty string, "message" becomes a content above the progress bar and headerText string will be set as a text inside the H3;
		headerText: 'Computing Data',

		// this will generate a heading corresponding to the size number
		headerSize: 4,

		// extra class(es) for the header tag
		headerClass: '',

		// bootstrap postfix for dialog size, e.g. "sm", "m"
		dialogSize: 'lg',

		// bootstrap postfix for progress bar type, e.g. "success", "warning";
		progressType: 'success',

		// determines the tag of the content element
		contentElement: 'p',

		// extra class(es) for the content tag
		contentClass: 'content'

	});


	$.ajax({
		type: 'POST',
		url: '/map2',
		data: {

			date_year: parseInt($('#year_indices').val()),
			date_month: parseInt($('#month_indices').val()),
			indices: $("#comp_indices1 option:selected").val(),
			region_selected: $("#region3 option:selected").val().replace(/'/g, '\\\''),
			satelite: $("#satelite2 option:selected").val().replace(/'/g, '\\\''),
			region: JSON.stringify(twoDimensionalArray),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
		},
		success: function () {
			map2.overlayMapTypes.clear();
			map2.controls[google.maps.ControlPosition.LEFT_BOTTOM].clear()
			$.ajax({
				method: "GET",
				url: '/map2',
				dataType: 'json',
				success: function (data) {

					if (data.mapid != null) {

						if (shapepoly != null) {
							clearPolygon(shapepoly);
						}

						twoDimensionalArray = null;

						if (layer2 != null) {



							layer2.setMap(null);

						}


						mapType = new google.maps.ImageMapType(updateMapTileOptions(data.mapid, data.token));
						// Add the EE layer to the map.



						map2.overlayMapTypes.push(mapType);




						waitingDialog.hide()


						var redBlueScale;

						var qScale;

						if (data.type == 'ndvi_anomaly') {
							redBlueScale = palete.ndvi_anomaly
							qScale = d3.scale.quantile()
								.domain([Math.ceil(data.min), Math.ceil(data.max)])
								.range(redBlueScale);
						} else if (data.type == 'ndwi_anomaly') {
							redBlueScale = palete.ndwi_anomaly
							qScale = d3.scale.quantile()
								.domain([Math.ceil(data.min), Math.ceil(data.max)])
								.range(redBlueScale);
						} else if (data.type == 'precipitation') {

							redBlueScale = palete.precipitation
							console.log(redBlueScale)
							qScale = d3.scale.quantile()
								.domain([Math.ceil(data.min), Math.ceil(data.max)])
								.range(redBlueScale);

						} else if (data.type == 'lst') {
							redBlueScale = palete.lst
							qScale = d3.scale.quantile()
								.domain([Math.ceil(data.min), Math.ceil(data.max)])
								.range(redBlueScale);
						} else if (data.type == 'smi') {
							redBlueScale = palete.smi
							qScale = d3.scale.quantile()
								.domain([Math.ceil(data.min), Math.ceil(data.max)])
								.range(redBlueScale);
						} else if (data.type == 'vhi') {
							redBlueScale = palete.vhi
							qScale = d3.scale.quantile()
								.domain([Math.ceil(data.min), Math.ceil(data.max)])
								.range(redBlueScale);
						} else if (data.type == 'spi') {
							redBlueScale = palete.spi
							qScale = d3.scale.quantile()
								.domain([Math.ceil(data.min), Math.ceil(data.max)])
								.range(redBlueScale);
						}









						var legend = document.createElement('div');
						legend.id = 'legend';
						legend.className = "leg"
						legend.setAttribute("style", "	border-radius: 5px;background: white;padding: 5px;margin: 10px;z-index:1;width:220px;height:300px;transition: all 0.5s ease  0.5s !important;")



						colorlegend("#legend", legend, qScale, "quantile", data.type, { title: "", boxHeight: 60, boxWidth: 65 });
						legend.index = 1;
						map2.controls[google.maps.ControlPosition.LEFT_BOTTOM].push(legend);


						var eventType = $("#region3 option:selected").val();

						var layerName = eventType.replace(/'/g, '\\\'');


						layer = addpolylayer(layerName)


						layer.setMap(map2)

					} else {
						waitingDialog.hide();
						$("#alBox").al({

							// default, success, warning, error
							context: "default",

							text: {

								// The title bar of your alert
								title: "Error Computing Data",

								// The more verbose description of the alert.
								description: data.error,

								hr: "",
								// The text of the "dismiss" button
								dismiss: "DISMISS"
							},

							classes: {

								// Classes to be added to #alBox
								container: "",

								// Classes to be added to #alBox-panel
								panel: "",

								// Classes to be added to #alBox-title
								title: "",

								// Classes to be added to #alBox-description
								description: "",

								// Classes to be added to the hr element above the dismiss button
								hr: "",

								// Classes to be added to the dismiss button
								dismiss: ""
							},

							// The number of seconds your alert will appear. 
							// Can also define as "infinite" to stay on screen until dismissal.
							seconds: "infinite",

							// URL Location to redirect after the alert is done
							redirect: ""

							});
					}

				},
				error: function () {
					alert("Not Good");
				}


			})

		},
		error: function (data) {

			waitingDialog.hide()

		}

	});

});






// Indices Compute for Map3
$(document).on('submit', '#indices_series_form3', function (e) {
	e.preventDefault();
	// document.getElementById("overlay").style.display = "block";

	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' });
	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' }); setTimeout(function () { waitingDialog.hide(); }, 2000);

	waitingDialog.show('This Computation Requires large Computing power and might take some time', {

		// if the option is set to boolean false, it will hide the header and "message" will be set in a paragraph above the progress bar.
		// When headerText is a not-empty string, "message" becomes a content above the progress bar and headerText string will be set as a text inside the H3;
		headerText: 'Computing Data',

		// this will generate a heading corresponding to the size number
		headerSize: 4,

		// extra class(es) for the header tag
		headerClass: '',

		// bootstrap postfix for dialog size, e.g. "sm", "m"
		dialogSize: 'lg',

		// bootstrap postfix for progress bar type, e.g. "success", "warning";
		progressType: 'success',

		// determines the tag of the content element
		contentElement: 'p',

		// extra class(es) for the content tag
		contentClass: 'content'

	});


	$.ajax({
		type: 'POST',
		url: '/map3',
		data: {


			date_year: parseInt($('#year_indices').val()),
			date_month: parseInt($('#month_indices').val()),
			indices: $("#comp_indices2 option:selected").val(),
			region_selected: $("#region4 option:selected").val().replace(/'/g, '\\\''),
			satelite: $("#satelite3 option:selected").val().replace(/'/g, '\\\''),
			region: JSON.stringify(twoDimensionalArray),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
		},
		success: function () {
			map3.overlayMapTypes.clear();
			map3.controls[google.maps.ControlPosition.LEFT_BOTTOM].clear()
			$.ajax({
				method: "GET",
				url: '/map3',
				dataType: 'json',
				success: function (data) {

					if (data.mapid != null) {

						if (shapepoly != null) {
							clearPolygon(shapepoly);
						}

						twoDimensionalArray = null;

						if (layer3 != null) {



							layer3.setMap(null);

						}


						mapType = new google.maps.ImageMapType(updateMapTileOptions(data.mapid, data.token));
						// Add the EE layer to the map.



						map3.overlayMapTypes.push(mapType);




						waitingDialog.hide()


						var redBlueScale;

						var qScale;

						if (data.type == 'ndvi_anomaly') {
							redBlueScale = palete.ndvi_anomaly
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'ndwi_anomaly') {
							redBlueScale = palete.ndwi_anomaly
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'precipitation') {

							redBlueScale = palete.precipitation
							console.log(redBlueScale)
							qScale = d3.scale.quantile()
								.range(redBlueScale);

						} else if (data.type == 'lst') {
							redBlueScale = palete.lst
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'smi') {
							redBlueScale = palete.smi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'vhi') {
							redBlueScale = palete.vhi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'spi') {
							redBlueScale = palete.spi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						}









						var legend = document.createElement('div');
						legend.id = 'legend';
						legend.className = "leg"
						legend.setAttribute("style", "	border-radius: 5px;background: white;padding: 5px;margin: 10px;z-index:1;width:220px;height:300px;transition: all 0.5s ease  0.5s !important;")



						colorlegend("#legend", legend, qScale, "quantile", data.type, { title: "", boxHeight: 60, boxWidth: 65 });
						legend.index = 1;
						map3.controls[google.maps.ControlPosition.LEFT_BOTTOM].push(legend);

						var eventType = $("#region4 option:selected").val();

						var layerName = eventType.replace(/'/g, '\\\'');


						layer = addpolylayer(layerName)


						layer.setMap(map3)


					} else {
						waitingDialog.hide();
						$("#alBox").al({

							// default, success, warning, error
							context: "default",

							text: {

								// The title bar of your alert
								title: "Error Computing Data",

								// The more verbose description of the alert.
								description: data.error,

								hr: "",
								// The text of the "dismiss" button
								dismiss: "DISMISS"
							},

							classes: {

								// Classes to be added to #alBox
								container: "",

								// Classes to be added to #alBox-panel
								panel: "",

								// Classes to be added to #alBox-title
								title: "",

								// Classes to be added to #alBox-description
								description: "",

								// Classes to be added to the hr element above the dismiss button
								hr: "",

								// Classes to be added to the dismiss button
								dismiss: ""
							},

							// The number of seconds your alert will appear. 
							// Can also define as "infinite" to stay on screen until dismissal.
							seconds: "infinite",

							// URL Location to redirect after the alert is done
							redirect: ""

							});

					}

				},
				error: function () {
					alert("Not Good");
				}


			})

		},
		error: function (data) {

			waitingDialog.hide()


		}

	});

});








// Indices Compute for Map4
$(document).on('submit', '#indices_series_form4', function (e) {
	e.preventDefault();
	// document.getElementById("overlay").style.display = "block";

	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' });
	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' }); setTimeout(function () { waitingDialog.hide(); }, 2000);

	waitingDialog.show('This Computation Requires large Computing power and might take some time', {

		// if the option is set to boolean false, it will hide the header and "message" will be set in a paragraph above the progress bar.
		// When headerText is a not-empty string, "message" becomes a content above the progress bar and headerText string will be set as a text inside the H3;
		headerText: 'Computing Data',

		// this will generate a heading corresponding to the size number
		headerSize: 4,

		// extra class(es) for the header tag
		headerClass: '',

		// bootstrap postfix for dialog size, e.g. "sm", "m"
		dialogSize: 'lg',

		// bootstrap postfix for progress bar type, e.g. "success", "warning";
		progressType: 'success',

		// determines the tag of the content element
		contentElement: 'p',

		// extra class(es) for the content tag
		contentClass: 'content'

	});


	$.ajax({
		type: 'POST',
		url: '/map4',
		data: {


			date_year: parseInt($('#year_indices').val()),
			date_month: parseInt($('#month_indices').val()),
			indices: $("#comp_indices3 option:selected").val(),
			region_selected: $("#region5 option:selected").val().replace(/'/g, '\\\''),
			satelite: $("#satelite4 option:selected").val().replace(/'/g, '\\\''),
			region: JSON.stringify(twoDimensionalArray),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
		},
		success: function () {
			map4.overlayMapTypes.clear();
			map4.controls[google.maps.ControlPosition.LEFT_BOTTOM].clear()
			$.ajax({
				method: "GET",
				url: '/map4',
				dataType: 'json',
				success: function (data) {

					if (data.mapid != null) {

						if (shapepoly != null) {
							clearPolygon(shapepoly);
						}

						twoDimensionalArray = null;

						if (layer4 != null) {



							layer4.setMap(null);

						}


						mapType = new google.maps.ImageMapType(updateMapTileOptions(data.mapid, data.token));
						// Add the EE layer to the map.



						map4.overlayMapTypes.push(mapType);




						waitingDialog.hide()


						var redBlueScale;

						var qScale;

						if (data.type == 'ndvi_anomaly') {
							redBlueScale = palete.ndvi_anomaly
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'ndwi_anomaly') {
							redBlueScale = palete.ndwi_anomaly
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'precipitation') {

							redBlueScale = palete.precipitation
							qScale = d3.scale.quantile()
								.range(redBlueScale);

						} else if (data.type == 'lst') {
							redBlueScale = palete.lst
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'smi') {
							redBlueScale = palete.smi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'vhi') {
							redBlueScale = palete.vhi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						} else if (data.type == 'spi') {
							redBlueScale = palete.spi
							qScale = d3.scale.quantile()
								.range(redBlueScale);
						}









						var legend = document.createElement('div');
						legend.id = 'legend';
						legend.className = "leg"
						legend.setAttribute("style", "	border-radius: 5px;background: white;padding: 5px;margin: 10px;z-index:1;width:220px;height:300px;transition: all 0.5s ease  0.5s !important;")



						colorlegend("#legend", legend, qScale, "quantile", data.type, { title: "", boxHeight: 60, boxWidth: 65 });
						legend.index = 1;
						map4.controls[google.maps.ControlPosition.LEFT_BOTTOM].push(legend);

						var eventType = $("#region5 option:selected").val();

						var layerName = eventType.replace(/'/g, '\\\'');


						layer = addpolylayer(layerName)


						layer.setMap(map4)


					} else {
						waitingDialog.hide();
						$("#alBox").al({

							// default, success, warning, error
							context: "default",

							text: {

								// The title bar of your alert
								title: "Error Computing Data",

								// The more verbose description of the alert.
								description: data.error,

								hr:"" ,
								// The text of the "dismiss" button
								dismiss: "DISMISS"
							},

							classes: {

								// Classes to be added to #alBox
								container: "",

								// Classes to be added to #alBox-panel
								panel: "",

								// Classes to be added to #alBox-title
								title: "",

								// Classes to be added to #alBox-description
								description: "",

								// Classes to be added to the hr element above the dismiss button
								hr: "",

								// Classes to be added to the dismiss button
								dismiss: ""
							},

							// The number of seconds your alert will appear. 
							// Can also define as "infinite" to stay on screen until dismissal.
							seconds: "infinite",

							// URL Location to redirect after the alert is done
							redirect: ""

							});


					}

				},
				error: function () {
					alert("Not Good");
				}


			})

		},
		error: function (data) {

			waitingDialog.hide()

		}

	});

});












// Draggable Element

function dragElement(elmnt) {
	var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
	if (document.getElementById(elmnt.id + "header")) {
		/* if present, the header is where you move the DIV from:*/
		document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
	} else {
		/* otherwise, move the DIV from anywhere inside the DIV:*/
		elmnt.onmousedown = dragMouseDown;
	}

	function dragMouseDown(e) {
		e = e || window.event;
		// get the mouse cursor position at startup:
		pos3 = e.clientX;
		pos4 = e.clientY;
		document.onmouseup = closeDragElement;
		// call a function whenever the cursor moves:
		document.onmousemove = elementDrag;
	}

	function elementDrag(e) {
		e = e || window.event;
		// calculate the new cursor position:
		pos1 = pos3 - e.clientX;
		pos2 = pos4 - e.clientY;
		pos3 = e.clientX;
		pos4 = e.clientY;
		// set the element's new position:
		elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
		elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
	}

	function closeDragElement() {
		/* stop moving when mouse button is released:*/
		document.onmouseup = null;
		document.onmousemove = null;
	}
}



$(document).on('submit', '#series_form', function (e) {
	e.preventDefault();
	waitingDialog.show('This Computation Requires large Computing power and might take some time', {

		// if the option is set to boolean false, it will hide the header and "message" will be set in a paragraph above the progress bar.
		// When headerText is a not-empty string, "message" becomes a content above the progress bar and headerText string will be set as a text inside the H3;
		headerText: 'Computing Data',

		// this will generate a heading corresponding to the size number
		headerSize: 4,

		// extra class(es) for the header tag
		headerClass: '',

		// bootstrap postfix for dialog size, e.g. "sm", "m"
		dialogSize: 'lg',

		// bootstrap postfix for progress bar type, e.g. "success", "warning";
		progressType: 'success',

		// determines the tag of the content element
		contentElement: 'p',

		// extra class(es) for the content tag
		contentClass: 'content'

	});


	


	$.ajax({
		type: 'POST',
		url: '/timeseries',
		data: {

			series_start: parseInt(start_series_date),
			series_end: parseInt(end_series_date),
			indices: $("#datasource_spi option:selected").val(),
			satelite: $("#satelite option:selected").val().replace(/'/g, '\\\''),
			region: JSON.stringify(marker_point),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
		},
		success: function () {

			$.ajax({
				method: "GET",
				url: '/timeseries',
				dataType: 'json',
				success: function (data) {
	
					waitingDialog.hide();
					//Make the DIV element draggagle:

					if(data.error==null){

						dragElement(document.getElementById(("mydiv")));

					$('#mydiv').css('visibility','visible');


					graph = data.timeSeriesData[0]['Data']

					time_d = [];
					data_f = [];
					for (var i = 0; i < graph.length; i++) {

						time_d.push(graph[i][0]);
						data_f.push(graph[i][1])
					}
					// create chart here

					var dataf = [
						{
							x: time_d,
							y: data_f,
							type: 'scatter',
							marker: {
								color: 'rgb(16, 159, 237)'
							}
							,
							name: 'Time Series'

						}
					];
					var layout = {
						title: data.notes_time,
						xaxis: {
							title: 'Date',
							titlefont: {
								family: 'Courier New, monospace',
								size: 18,
								color: '#111111'
							}
						},
						yaxis: {
							title: data.source_time + ' Values',
							titlefont: {
								family: 'Courier New, monospace',
								size: 18,
								color: '#111111'
							}
						}
					};
					Plotly.newPlot('plot', dataf, layout);




					} else {


						$("#alBox").al({

							// default, success, warning, error
							context: "default",

							text: {

								// The title bar of your alert
								title: "Error ",

								// The more verbose description of the alert.
								description: "An Error Occurred while computing time series" + data.error,

								hr: "",
								// The text of the "dismiss" button
								dismiss: "DISMISS"
							},

							classes: {

								// Classes to be added to #alBox
								container: "",

								// Classes to be added to #alBox-panel
								panel: "",

								// Classes to be added to #alBox-title
								title: "",

								// Classes to be added to #alBox-description
								description: "",

								// Classes to be added to the hr element above the dismiss button
								hr: "",

								// Classes to be added to the dismiss button
								dismiss: ""
							},

							// The number of seconds your alert will appear. 
							// Can also define as "infinite" to stay on screen until dismissal.
							seconds: "infinite",

							// URL Location to redirect after the alert is done
							redirect: ""

						});

					}
					



				},
				error: function () {
					$("#alBox").al({

						// default, success, warning, error
						context: "default",

						text: {

							// The title bar of your alert
							title: "Error ",

							// The more verbose description of the alert.
							description: "An Error Occurred while computing time series",

							hr: "",
							// The text of the "dismiss" button
							dismiss: "DISMISS"
						},

						classes: {

							// Classes to be added to #alBox
							container: "",

							// Classes to be added to #alBox-panel
							panel: "",

							// Classes to be added to #alBox-title
							title: "",

							// Classes to be added to #alBox-description
							description: "",

							// Classes to be added to the hr element above the dismiss button
							hr: "",

							// Classes to be added to the dismiss button
							dismiss: ""
						},

						// The number of seconds your alert will appear. 
						// Can also define as "infinite" to stay on screen until dismissal.
						seconds: "infinite",

						// URL Location to redirect after the alert is done
						redirect:"" 

						});
				}


			})

		},
		error: function (data) {
			console.log(data.startdate)
		}

	});

});



//Donwload Indices form
$(document).on('submit', '#download', function (e) {
	e.preventDefault();
	// document.getElementById("overlay").style.display = "block";

	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' });
	// waitingDialog.show('Processing Request', 'Computing  may take a few minutes.', { dialogSize: 'sm', progressType: 'warning' }); setTimeout(function () { waitingDialog.hide(); }, 2000);

	waitingDialog.show('This Computation Requires large Computing power and might take some time', {

		// if the option is set to boolean false, it will hide the header and "message" will be set in a paragraph above the progress bar.
		// When headerText is a not-empty string, "message" becomes a content above the progress bar and headerText string will be set as a text inside the H3;
		headerText: 'Downloading Data',

		// this will generate a heading corresponding to the size number
		headerSize: 4,

		// extra class(es) for the header tag
		headerClass: '',

		// bootstrap postfix for dialog size, e.g. "sm", "m"
		dialogSize: 'lg',

		// bootstrap postfix for progress bar type, e.g. "success", "warning";
		progressType: 'success',

		// determines the tag of the content element
		contentElement: 'p',

		// extra class(es) for the content tag
		contentClass: 'content'

	});


	$.ajax({
		type: 'POST',
		url: '/indices_download',
		data: {

			date_year: parseInt($('#year_indices').val()),
			date_month: parseInt($('#month_indices').val()),
			indices: $("#datasource_spi option:selected").val(),
			region_selected: $("#region1 option:selected").val().replace(/'/g, '\\\''),
			satelite: $("#satelite option:selected").val().replace(/'/g, '\\\''),
			region: JSON.stringify(twoDimensionalArray),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
		},
		success: function () {
			$.ajax({
				method: "GET",
				url: '/indices_download',
				dataType: 'json',
				success: function (data) {
					
					if (data.download_data != null) {

					if (shapepoly != null) {
							clearPolygon(shapepoly);
						}

						twoDimensionalArray = null;
						if (layer != null) {



							layer.setMap(null);

						}
						waitingDialog.hide()
						var url = data.download_data;
						
						$("#alBox").aldownload({

							// default, success, warning, error
							context: "default",

							text: {

								// The title bar of your alert
								title: "Donwload",

								// The more verbose description of the alert.
								description: 'CLICK THE BUTTON BELLOW TO DONWLOAD',

								hr: '',
								download: "DOWNLOAD DATA",
								// The text of the "dismiss" button
								dismiss: "DISMISS",
								url:url
							},

							classes: {

								// Classes to be added to #alBox
								container: "",

								// Classes to be added to #alBox-panel
								panel: "",

								// Classes to be added to #alBox-title
								title: "",

								// Classes to be added to #alBox-description
								description: "",
								download:"",

								// Classes to be added to the hr element above the dismiss button
								hr: "",

								// Classes to be added to the dismiss button
								dismiss: ""
							},

							// The number of seconds your alert will appear. 
							// Can also define as "infinite" to stay on screen until dismissal.
							seconds: "infinite",

							// URL Location to redirect after the alert is done
							redirect:''

						});


					} else {
						waitingDialog.hide();
			
						$("#alBox").al({

							// default, success, warning, error
							context: "default",

							text: {

								// The title bar of your alert
								title: "Error Computing Data",

								// The more verbose description of the alert.
								description: data.error,

								hr:"",
								// The text of the "dismiss" button
								dismiss: "DISMISS"
							},

							classes: {

								// Classes to be added to #alBox
								container: "",

								// Classes to be added to #alBox-panel
								panel: "",

								// Classes to be added to #alBox-title
								title: "",

								// Classes to be added to #alBox-description
								description: "",

								// Classes to be added to the hr element above the dismiss button
								hr: "",

								// Classes to be added to the dismiss button
								dismiss: ""
							},

							// The number of seconds your alert will appear. 
							// Can also define as "infinite" to stay on screen until dismissal.
							seconds: "infinite",

							// URL Location to redirect after the alert is done
							redirect: ""

						});

					}

				},
				error: function () {
					alert("Not Good");
				}


			})

		},
		error: function (data) {

			waitingDialog.hide()


		}

	});

});









function updateMapTileOptions(MAPID, TOKEN) {

	var eeMapOptions = {
		getTileUrl: function (tile, zoom) {
			//cross origin is for putting in to get the save pdf map working
			//var url = ['https://crossorigin.me/https://earthengine.googleapis.com/map',
			var url = ['https://earthengine.googleapis.com/map',
				MAPID, zoom, tile.x, tile.y
			].join("/");
			url += '?token=' + TOKEN;
			return url;
		},
		tileSize: new google.maps.Size(256, 256)
	};
	return eeMapOptions;
};


