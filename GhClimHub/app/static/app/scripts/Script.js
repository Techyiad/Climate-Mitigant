
var Ghana = { lat: 7.9465, lng: -1.0232 };


var styles = {
	default: null,
	silver: [
		{
			elementType: 'geometry',
			stylers: [{ color: '#f5f5f5' }]
		},
		{
			elementType: 'labels.icon',
			stylers: [{ visibility: 'off' }]
		},
		{
			elementType: 'labels.text.fill',
			stylers: [{ color: '#616161' }]
		},
		{
			elementType: 'labels.text.stroke',
			stylers: [{ color: '#f5f5f5' }]
		},
		{
			featureType: 'administrative.land_parcel',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#bdbdbd' }]
		},
		{
			featureType: 'poi',
			elementType: 'geometry',
			stylers: [{ color: '#eeeeee' }]
		},
		{
			featureType: 'poi',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#757575' }]
		},
		{
			featureType: 'poi.park',
			elementType: 'geometry',
			stylers: [{ color: '#e5e5e5' }]
		},
		{
			featureType: 'poi.park',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#9e9e9e' }]
		},
		{
			featureType: 'road',
			elementType: 'geometry',
			stylers: [{ color: '#ffffff' }]
		},
		{
			featureType: 'road.arterial',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#757575' }]
		},
		{
			featureType: 'road.highway',
			elementType: 'geometry',
			stylers: [{ color: '#dadada' }]
		},
		{
			featureType: 'road.highway',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#616161' }]
		},
		{
			featureType: 'road.local',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#9e9e9e' }]
		},
		{
			featureType: 'transit.line',
			elementType: 'geometry',
			stylers: [{ color: '#e5e5e5' }]
		},
		{
			featureType: 'transit.station',
			elementType: 'geometry',
			stylers: [{ color: '#eeeeee' }]
		},
		{
			featureType: 'water',
			elementType: 'geometry',
			stylers: [{ color: '#c9c9c9' }]
		},
		{
			featureType: 'water',
			elementType: 'labels.text.fill',
			stylers: [{ color: '#9e9e9e' }]
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

var palete = {
	'ndvi': ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00'], 'ndwi': ["#e20000 ", "32cd32", "ffff00", "ff8c00", "#00f9f9", "#3570dd", "0000ff"], 'evi': ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf']
}



function CenterControl(controlDiv, map, center) {
	// We set up a variable for this since we're adding event listeners
	// later.
	var control = this;

	// Set the center property upon construction
	control.center_ = center;
	controlDiv.style.clear = 'both';

	// Set CSS for the control border
	var goCenterUI = document.createElement('div');
	goCenterUI.id = 'goCenterUI';
	goCenterUI.title = 'Click to recenter the map';
	controlDiv.appendChild(goCenterUI);

	// Set CSS for the control interior
	var goCenterText = document.createElement('div');
	goCenterText.id = 'goCenterText';
	goCenterText.innerHTML = 'Center Map';
	goCenterUI.appendChild(goCenterText);

	// Set CSS for the setCenter control border
	var setCenterUI = document.createElement('div');
	setCenterUI.id = 'setCenterUI';
	setCenterUI.title = 'Click to change the center of the map';
	controlDiv.appendChild(setCenterUI);

	// Set CSS for the control interior
	var setCenterText = document.createElement('div');
	setCenterText.id = 'setCenterText';
	setCenterText.innerHTML = 'Set Center';
	setCenterUI.appendChild(setCenterText);

	// Set up the click event listener for 'Center Map': Set the center of
	// the map
	// to the current center of the control.
	goCenterUI.addEventListener('click', function () {
		var currentCenter = control.getCenter();
		map.setCenter(currentCenter);
	});

	// Set up the click event listener for 'Set Center': Set the center of
	// the control to the current center of the map.
	setCenterUI.addEventListener('click', function () {
		var newCenter = map.getCenter();
		control.setCenter(newCenter);
	});
}

/**
 * Define a property to hold the center state.
 * @private
 */
CenterControl.prototype.center_ = null;

/**
 * Gets the map center.
 * @return {?google.maps.LatLng}
 */
CenterControl.prototype.getCenter = function () {
	return this.center_;
};

/**
 * Sets the map center.
 * @param {?google.maps.LatLng} center
 */
CenterControl.prototype.setCenter = function (center) {
	this.center_ = center;
};





styleRetro = new google.maps.StyledMapType(styles.retro, { name: 'Retro' })
styleSilver = new google.maps.StyledMapType(styles.silver, { name: 'Silver' })
styleNight = new google.maps.StyledMapType(styles.night, { name: 'Darknight' })


var polyOptions = {
	strokeWeight: 0,
	fillOpacity: 0.45,
	editable: true,
	fillColor: '#FF1493'
};
var mapOptions = {
	center: Ghana,
	zoom: 7,
	maxZoom: 20,
	streetViewControl: false,
	mapTypeControl: true,
	navigationControl: true,
	mapTypeId: google.maps.MapTypeId.TERRAIN,
	mapTypeControlOptions: {
		style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
		position: google.maps.ControlPosition.TOP_RIGHT,
		mapTypeIds: [
			google.maps.MapTypeId.HYBRID,
			google.maps.MapTypeId.ROADMAP,
			google.maps.MapTypeId.SATELLITE,
			google.maps.MapTypeId.TERRAIN,
			'Retro',
			'Silver',
			'Darknight',
			'simpleAtlasStyle',
			'whiteWaterStyle',
		]
	},
	clickable: true,
	backgroundColor: '#FFFFFF',
	disableDefaultUI: false,
	zoomControl: true,
	zoomControlOptions: {
		style: google.maps.ZoomControlStyle.LARGE,
		position: google.maps.ControlPosition.TOP_RIGHT
	},
	panControl: false,
	panControlOptions: {
		position: google.maps.ControlPosition.TOP_RIGHT
	},
};


var map = new google.maps.Map(document.getElementById('map'), mapOptions);




var poly = null;

var rectangle = null;


getPolygonCoordinates = function () {
	if (this.currentPolygon) {
		var points = this.currentPolygon.getPath().getArray();
		var twoDimensionalArray = points.map(function (point) {
			return [point.lng(), point.lat()];
		});
		return twoDimensionalArray;
	} else {
		return null;
	}
};

var twoDimensionalArray;

var shapepoly;
//google.maps.event.addListener(drawingManager, 'polygoncomplete', function (polygon) {
//	twoDimensionalArray = null;
//	shapepoly = null;
//	var arr = [];

//	var points = polygon.getPath().getArray();
//	shapepoly = polygon;
//	twoDimensionalArray = points.map(function (point) {
//		return [point.lng(), point.lat()];
//	});

//	document.getElementById("rectangle").innerHTML = JSON.stringify(twoDimensionalArray);
//	poly = twoDimensionalArray;
//	getpoly = twoDimensionalArray;

//	document.getElementById("poly").innerHTML = points;


//});

var shapecircle;


function getCoordinates(rect) {
	var bounds = rect.getBounds();
	return [
		bounds.getSouthWest().lng(),
		bounds.getSouthWest().lat(),
		bounds.getNorthEast().lng(),
		bounds.getNorthEast().lat(),
	].join(',');
}



clearPolygon = function (currentPolygon) {
	currentPolygon.setMap(null);
	currentPolygon = null;


};



clearCircle = function (currentCircle) {
	currentCircle.setMap(null);
	currentCircle = null;


};


map.mapTypes.set('Retro', styleRetro);
map.mapTypes.set('Silver', styleSilver);
map.mapTypes.set('Darknight', styleNight);

// Create the DIV to hold the control and call the CenterControl()
// constructor
// passing in this DIV.
var centerControlDiv = document.createElement('div');
var centerControl = new CenterControl(centerControlDiv, map, Ghana);

centerControlDiv.index = 1;
centerControlDiv.style['padding-top'] = '10px';
map.controls[google.maps.ControlPosition.BOTTOM_LEFT].push(centerControlDiv);









//Adding event listener to from element


// Returns a string of the bounds of the given rectangle
// (xMin,yMin,xMax,yMax).
function getCoordinates(rect) {
	var bounds = rect.getBounds();
	return [
		bounds.getSouthWest().lng(),
		bounds.getSouthWest().lat(),
		bounds.getNorthEast().lng(),
		bounds.getNorthEast().lat(),
	].join(',');
}

function buildGetTileUrl(mapid, token) {
	return function (tile, zoom) {
		var baseUrl = 'https://earthengine.googleapis.com/map';
		var url = [baseUrl, mapid, zoom, tile.x, tile.y].join('/');
		url += '?token=' + token;
		return url;
	};
}



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



function getCoordinates(rect) {
	var bounds = rect.getBounds();
	return [
		bounds.getSouthWest().lng(),
		bounds.getSouthWest().lat(),
		bounds.getNorthEast().lng(),
		bounds.getNorthEast().lat(),
	].join(',');
}




/*********************************
*    OPACITY SLIDER BUTTON            *
*********************************/
//set style of tooltip window for opacity slider
var opacity_tooltip = $('<div id="tooltip" />').css({
	position: 'relative',
	top: 0,
	left: -70,
	color: 'white',
	background: 'black',
	display: 'block',
	padding: '10',
	opacity: 1,
	width: '60',
	range: true,
	fontSize: '11px',

}).hide();

//set initial tooltip
opacity_tooltip.text(Math.round($('#opacity').val() * 100) + "% Opacity");

var mapType;

function put_sliderOnMap() {
	//needs to be done after window.mapType is definitely not undefined
	$("#slider").slider({
		orientation: "vertical",
		range: false,
		max: 1.00,
		min: 0.00,
		step: .05,
		animate: true,
		value: $('#opacity').val(),
		slide: function (event, ui) {
			set_opacity(ui.value);
		},
		change: function (event, ui) { }
	}).find(".ui-slider-handle").append(opacity_tooltip).hover(function () {
		opacity_tooltip.show()
	}, function () {
		opacity_tooltip.hide()
	});
	set_opacity(parseFloat($('#opacity').val()));
};


function set_opacity(opacity) {
	opacity_tooltip.text(Math.round(opacity * 100) + "% Opacity");
	mapType.setOpacity(opacity);
	if (opacity === 1) {
		opacity = 1.0;
		$('#opacity').val("1.0");
	} else if (opacity === 0) {
		opacity = 0.0;
		$('#opacity').val("0.0");
	} else {
		$('#opacity').val(opacity);
	};
};




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
	console.log(eventTypeName)
	var storeName = eventTypeName.replace(/'/g, '\\\'');

	if (layer != null) {



		layer.setMap(null);

	}


	layer = addlayer(storeName)


	layer.setMap(map)


})




var marker_point,marker;

$('#marker_decide').click(function (event) {

	$('#chart_submit').prop('disabled', false);
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
	infowindow.open(map, marker);

})





var drawingManager;

$('#poly_map').click(function () {

	window.drawingManager = new google.maps.drawing.DrawingManager({
		drawingMode: google.maps.drawing.OverlayType.POLYGON,
		drawingControl: true,
		drawingControlOptions: {
			position: google.maps.ControlPosition.LEFT_TOP,
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


	});

})






$('#clear_poly').click(function () {


	if (shapepoly != null) {
		clearPolygon(shapepoly);
	}



})


$('#clear_marker').click(function () {
	console.log("heey")

marker.setMap(null)


})


$(document).on('submit', '#user_download', function (e) {
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
		url: '/download_data',
		data: {
			dataset: $('#dataset').val(),
			datasource: $('#datasource').val(),
			start: $('#start').val().replace(/\s+/g, ''),
			end: $('#end').val().trim(),
			cloudscore: $("#cloudscore").val(),
			region: JSON.stringify(twoDimensionalArray),
			region_selected: $("#region1 option:selected").val().replace(/'/g, '\\\''),
			scale: document.getElementById('scale').value,
			name: document.getElementById('downloadFilename').value,
			download: document.getElementById("rectangle").innerHTML,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

		},
		success: function () {

			marker.setMap(null);
			$.ajax({
				method: "GET",
				url: '/download_data',
				dataType: 'json',
				success: function (data) {

					map.overlayMapTypes.clear();
					if (data.error == null) {


						waitingDialog.hide();


						if (layer != null) {



							layer.setMap(null);

						}


						if (shapepoly != null) {
							clearPolygon(shapepoly);
						}

						twoDimensionalArray = null;

						//set url
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
								url: url
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
								download: "",

								// Classes to be added to the hr element above the dismiss button
								hr: "",

								// Classes to be added to the dismiss button
								dismiss: ""
							},

							// The number of seconds your alert will appear. 
							// Can also define as "infinite" to stay on screen until dismissal.
							seconds: "infinite",

							// URL Location to redirect after the alert is done
							redirect: ''

						});





					} else {


						if (layer != null) {



							layer.setMap(null);

						}


						if (shapepoly != null) {
							clearPolygon(shapepoly);
						}

						twoDimensionalArray = null;
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
					waitingDialog.hide();
					$("#alBox").al({

						// default, success, warning, error
						context: "default",

						text: {

							// The title bar of your alert
							title: "Error Computing Data",

							// The more verbose description of the alert.
							description: "Could Not COmpute Data",

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


			})

		},
		error: function (data) {
			waitingDialog.hide();
			$("#alBox").al({

				// default, success, warning, error
				context: "default",

				text: {

					// The title bar of your alert
					title: "Error Computing Data",

					// The more verbose description of the alert.
					description: "Could Not COmpute Data",

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

	});

});






$(document).on('submit', '#user_form', function (e) {
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
		url: '/calc_data',
		data: {
			dataset: $('#dataset').val(),
			datasource: $('#datasource').val(),
			start: $('#start').val().replace(/\s+/g, ''),
			end: $('#end').val().trim(),
			cloudscore: $("#cloudscore").val(),
			region: JSON.stringify(twoDimensionalArray),
			region_selected: $("#region1 option:selected").val().replace(/'/g, '\\\''),
			scale: null,
			name: 'something',
			download: document.getElementById("rectangle").innerHTML,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

		},
		success: function () {
			map.overlayMapTypes.clear();

			$.ajax({
				method: "GET",
				url: '/calc_data',
				dataType: 'json',
				success: function (data) {
					map.controls[google.maps.ControlPosition.LEFT_BOTTOM].clear()
					if (data.error == null) {


						if (layer != null) {



							layer.setMap(null);

						}
	

						if (shapepoly != null) {
							clearPolygon(shapepoly);
						}

						
						mapType = new google.maps.ImageMapType(updateMapTileOptions(data.mapid, data.token));
						twoDimensionalArray = null;



						// Add the EE layer to the map.

						map.overlayMapTypes.push(mapType);
						document.getElementById("date_info").innerHTML = data.collection_info + "  " + data.date_info
						document.getElementById("notes").innerHTML = data.notes




						//adjust transparency to that set (EE gives 100% back)
						// mapType.setOpacity(parseFloat($('#opacity').val()));

						//replace map layer of layer=0, else they could accumulate
						map.overlayMapTypes.setAt(0, mapType);

						//Add opacity slider on map
						put_sliderOnMap();
						map.controls[google.maps.ControlPosition.RIGHT_TOP].push(opacity_slider);

						var eventTypeName = $("#dataset option:selected").val();
						var storeName = eventTypeName.replace(/'/g, '\\\'');
					

						var redBlueScale;

						var qScale;

						if (storeName == "NDVI") {
							redBlueScale = palete.ndvi
							qScale = d3.scale.quantile()
								.range(redBlueScale);

						} else if (storeName == "NDWI") {
							redBlueScale = palete.ndwi
							qScale = d3.scale.quantile()
								.range(redBlueScale);

						} else if (storeName == "EVI") {

							redBlueScale = palete.evi
							qScale = d3.scale.quantile()
								.range(redBlueScale);


						}

						var legend = document.createElement('div');
						legend.id = 'legend';
						legend.className = "leg"
						legend.setAttribute("style", "	border-radius: 5px;background: white;padding: 5px;margin: 10px;z-index:1;width:220px;height:300px;transition: all 0.5s ease  0.5s !important;")



						colorlegend("#legend", legend, qScale, "quantile", storeName, { title: "", boxHeight: 60, boxWidth: 65 });
						legend.index = 1;
						map.controls[google.maps.ControlPosition.LEFT_BOTTOM].push(legend);

						
						var eventType = $("#region1 option:selected").val();
						
						var layerName = eventType.replace(/'/g, '\\\'');


						layer = addpolylayer(layerName)


						layer.setMap(map)



						waitingDialog.hide();


					} else {
						map.overlayMapTypes.clear();
						waitingDialog.hide();
						$("#alBox").al({

							// default, success, warning, error
							context: "default",

							text: {

								// The title bar of your alert
								title: "Error Computing Data" ,

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
					waitingDialog.hide();
					$("#alBox").al({

						// default, success, warning, error
						context: "default",

						text: {

							// The title bar of your alert
							title: "Error Computing Data",

							// The more verbose description of the alert.
							description: "Could Not Compute Data. An Error Occured",

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


			})

		},
		error: function (data) {
			waitingDialog.hide();
			$("#alBox").al({

				// default, success, warning, error
				context: "default",

				text: {

					// The title bar of your alert
					title: "Error Computing Data",

					// The more verbose description of the alert.
					description: "Could Not Compute Data. An Error Occured",

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

	});

});

var myLatlng = { lat: 6.678162, lng: -1.571227 };




//var marker_point;

//google.maps.event.addListener(marker, 'dragend', function (evt) {

//	marker_point = [parseFloat(evt.latLng.lng().toFixed(6)), parseFloat(evt.latLng.lat().toFixed(6))];
//	console.log(marker_point);
//});



//chart

$(document).on('submit', '#chart_form', function (e) {
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

	setTimeout(function () {
		waitingDialog.hide();
	}, 8000);
	$.ajax({
		type: 'POST',
		url: '/chart_data',
		data: {
			dataset: $('#dataset').val(),
			datasource: $('#datasource').val(),
			start: $('#start').val().replace(/\s+/g, ''),
			end: $('#end').val().trim(),
			cloudscore: $("#cloudscore").val(),
			region: JSON.stringify(twoDimensionalArray),
			region_selected: $("#region1 option:selected").val().replace(/'/g, '\\\''),
			palette: JSON.stringify(document.getElementById('palette').innerHTML),
			chart_point: JSON.stringify(marker_point),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

		},
		success: function () {		
			$.ajax({
				method: "GET",
				url: '/chart_data',
				dataType: 'json',
				success: function (data) {
				
					if (data.error == null) {
						$('#graphDropdown').click();


						if (layer != null) {



							layer.setMap(null);

						}




						marker.setMap(null)
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
									color: 'rgb(255, 0, 0)'
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
									color: '#7f7f7f'
								}
							},
							yaxis: {
								title: data.product_time + ' Values',
								titlefont: {
									family: 'Courier New, monospace',
									size: 18,
									color: '#7f7f7f'
								}
							}
						};
						Plotly.newPlot('myDiv', dataf, layout);
						waitingDialog.hide();
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
					waitingDialog.hide();
					$("#alBox").al({

						// default, success, warning, error
						context: "default",

						text: {

							// The title bar of your alert
							title: "Error Computing Data",

							// The more verbose description of the alert.
							description: "Cloud Not Compute Data",

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


			})

		},
		error: function (data) {
			waitingDialog.hide();
			$("#alBox").al({

				// default, success, warning, error
				context: "default",

				text: {

					// The title bar of your alert
					title: "Error Computing Data",

					// The more verbose description of the alert.
					description: "Cloud Not Compute Data",

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

	});

});
































if (typeof jQuery == 'undefined') {
	console.log("jQuery library is not found.");
} else {

	// TODO: Add general library information/comments
	// TODO: Add grunt/gulp to the project
	(function ($) {

		var timer = null;

		$.fn.aldownload = function (options) {

			// Define defaults
			var defaults = {
				context: "default",
				text: {
					title: "TITLE",
					description: "DESCRIPTION",
					dismiss: "DISMISS",
					download: "DOWNLOAD DATA",
					url: ""
				},
				classes: {
					container: "",
					panel: "",
					title: "",
					description: "",
					download: "",
					hr: "",
					dismiss: ""
				},
				seconds: "infinite",
				redirect: ""
			};

			// Build settings, merging defaults and options
			var settings = $.extend(true, {}, defaults, options);

			// Build the alBoxPanel
			var html = '<div id="alBox-panel" class="alBox-panel-' + settings.context + ' ' + settings.classes.panel + '">';
			html += '<span id="alBox-title" class="' + settings.classes.title + '">' + settings.text.title + '</span>';
			html += '<span id="alBox-description"  class="' + settings.classes.description + '">' + settings.text.description + '</span>';
			html += '<hr class="' + settings.classes.hr + '"/>';
			html += '<button id="alBox-download" class="' + settings.classes.download + '">' + settings.text.download + '</button>';
			html += '<button id="alBox-dismiss" class="' + settings.classes.dismiss + '">' + settings.text.dismiss + '</button>';
			html += '</div>';

			// Place into DOM
			this.html(html);

			if (settings.classes.container != "") {
				$("#alBox").addClass(settings.classes.container);
			}

			// Add the click handler for the dismiss button
			$("#alBox-dismiss").click(clearAl);
			$("#alBox-download").click(openurl)
			// Click handler for clicking outside the prompt box
			$("#alBox").click(dismiss);

			// Fade in the alert box
			this.fadeIn();
			function openurl() {
				window.open(settings.text.url);

			}
			// If seconds isn't "infinite" set a timer to clear the box
			if (settings.seconds !== "infinite") {
				timer = setInterval(function () {
					clearTimeout(timer);
					clearAl();
					timer = null;
				}, settings.seconds * 1000);
			}

			// Preserve chaining
			return this;
		};

		/**
		 * Dismiss only if the panel, title, description not part of the click event
		 * @param e: event
		 */
		function dismiss(e) {
			e.preventDefault();
			if (!$(e.target).is('#alBox-panel')
				&& !$(e.target).is('#alBox-title')
				&& !$(e.target).is('#alBox-description')) {

				// Clear the alert box
				// clearAl();
			}
		}

		/**
		 * Function that will clear the interval, fade the alert out
		 * and remove the HTML structure from the container
		 */
		function clearAl() {
			clearInterval(timer);
			$("#alBox").fadeOut();
			$("#alBox").html('');

		}





	}(jQuery));
}































if (typeof jQuery == 'undefined') {
	console.log("jQuery library is not found.");
} else {

	// TODO: Add general library information/comments
	// TODO: Add grunt/gulp to the project
	(function ($) {

		var timer = null;

		$.fn.al = function (options) {

			// Define defaults
			var defaults = {
				context: "default",
				text: {
					title: "TITLE",
					description: "DESCRIPTION",
					dismiss: "DISMISS"
				},
				classes: {
					container: "",
					panel: "",
					title: "",
					description: "",
					hr: "",
					dismiss: ""
				},
				seconds: "infinite",
				redirect: ""
			};

			// Build settings, merging defaults and options
			var settings = $.extend(true, {}, defaults, options);

			// Build the alBoxPanel
			var html = '<div id="alBox-panel" class="alBox-panel-' + settings.context + ' ' + settings.classes.panel + '">';
			html += '<span id="alBox-title" class="' + settings.classes.title + '">' + settings.text.title + '</span>';
			html += '<span id="alBox-description" class="' + settings.classes.description + '">' + settings.text.description + '</span>';
			html += '<hr class="' + settings.classes.hr + '"/>';
			html += '<button id="alBox-dismiss" class="' + settings.classes.dismiss + '">' + settings.text.dismiss + '</button>';
			html += '</div>';

			// Place into DOM
			this.html(html);

			if (settings.classes.container != "") {
				$("#alBox").addClass(settings.classes.container);
			}

			// Add the click handler for the dismiss button
			$("#alBox-dismiss").click(clearAl);

			// Click handler for clicking outside the prompt box
			$("#alBox").click(dismiss);

			// Fade in the alert box
			this.fadeIn();

			// If seconds isn't "infinite" set a timer to clear the box
			if (settings.seconds !== "infinite") {
				timer = setInterval(function () {
					clearTimeout(timer);
					clearAl();
					timer = null;
				}, settings.seconds * 1000);
			}

			// Preserve chaining
			return this;
		};

		/**
		 * Dismiss only if the panel, title, description not part of the click event
		 * @param e: event
		 */
		function dismiss(e) {
			e.preventDefault();
			if (!$(e.target).is('#alBox-panel')
				&& !$(e.target).is('#alBox-title')
				&& !$(e.target).is('#alBox-description')) {

				// Clear the alert box
				clearAl();
			}
		}

		/**
		 * Function that will clear the interval, fade the alert out
		 * and remove the HTML structure from the container
		 */
		function clearAl() {
			clearInterval(timer);
			$("#alBox").fadeOut();
			$("#alBox").html('');

		}

	}(jQuery));
}







/**
 * Module for displaying "Waiting for..." dialog using Bootstrap
 *
 * @author Eugene Maslovich <ehpc@em42.ru>
 */

var waitingDialog = waitingDialog || (function ($) {
	'use strict';

	// Creating modal dialog's DOM
	var $dialog = $(
		'<div class="modal fade" data-backdrop="static" data-keyboard="false" tabindex="-1" role="dialog" aria-hidden="true" style="padding-top:15%; overflow-y:visible;">' +
		'<div class="modal-dialog modal-m">' +
		'<div class="modal-content">' +
			'<div class="modal-header"><h3 style="margin:0;"></h3></div>' +
			'<div class="modal-body">' +
				'<div class="progress progress-striped active" style="margin-bottom:0;"><div class="progress-bar" style="width: 100%"></div></div>' +
			'</div>' +
		'</div></div></div>');

	return {
		/**
		 * Opens our dialog
		 * @param message Custom message
		 * @param options Custom options:
		 * 				  options.dialogSize - bootstrap postfix for dialog size, e.g. "sm", "m";
		 * 				  options.progressType - bootstrap postfix for progress bar type, e.g. "success", "warning".
		 */
		show: function (message, options) {
			// Assigning defaults
			if (typeof options === 'undefined') {
				options = {};
			}
			if (typeof message === 'undefined') {
				message = 'Loading';
			}
			var settings = $.extend({
				dialogSize: 'm',
				progressType: '',
				onHide: null // This callback runs after the dialog was hidden
			}, options);

			// Configuring dialog
			$dialog.find('.modal-dialog').attr('class', 'modal-dialog').addClass('modal-' + settings.dialogSize);
			$dialog.find('.progress-bar').attr('class', 'progress-bar');
			if (settings.progressType) {
				$dialog.find('.progress-bar').addClass('progress-bar-' + settings.progressType);
			}
			$dialog.find('h3').text(message);
			// Adding callbacks
			if (typeof settings.onHide === 'function') {
				$dialog.off('hidden.bs.modal').on('hidden.bs.modal', function (e) {
					settings.onHide.call($dialog);
				});
			}
			// Opening dialog
			$dialog.modal();
		},
		/**
		 * Closes dialog
		 */
		hide: function () {
			$dialog.modal('hide');
		}
	};

})(jQuery);
