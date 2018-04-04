


$('#datasource_spi').change(function () {
	var eventTypeName = $("#datasource_spi option:selected");

	if (eventTypeName.is('[name="precipitation"]')) {
		$('#indices_discription').text("is any form of water - liquid or solid - falling from the sky. It includes rain, sleet, snow, hail and drizzle plus a few less common occurrences such as ice pellets, diamond dust and freezing rain");

		$("#satelite").hide('slow');
		$("#stext").hide('slow');
	}

	if (eventTypeName.is('[name="precipitation anom"]')) {
		$('#indices_discription').text("This shows the deviation from the monthly total precipitation relative to historical average");

		$("#satelite").hide('slow');
		$("#stext").hide('slow');
	}

	if (eventTypeName.is('[name="ndvi anomaly"]')) {

		$('#indices_discription').text("NDVI anomaly is the difference between the average NDVI for a particular month of a given year and the average NDVI for the same month over a specified number of years. This approach can be used to characterize the health of vegetation for a particular month and year relative to what is considered normal, which is a good indicator of drought or declining vegetation health");

		$("#satelite").show('slow');
		$("#stext").show('slow');


	}

	if (eventTypeName.is('[name="ndwi anomaly"]')) {
		$('#indices_discription').text("NDWI anomaly is the difference between the average NDVI for a particular month of a given year and the average NDWI for the same month over a specified number of years");

		$("#satelite").show('slow');
		$("#stext").show('slow');
		//$("#satelite option[value='avhrr']").remove();

	}

	if (eventTypeName.is('[name="spi"]')) {
		$('#indices_discription').text("The index is a standardized measure for precipitation in different climatic regions and for seasonal differences.  It allows an analyst to determine the rarity of a drought at a given time scale (temporal resolution) of interest for any rainfall station with historic data");

		$("#satelite").hide('slow');
		$("#stext").hide('slow');
	}

	if (eventTypeName.is('[name="lst"]')) {
		$('#indices_discription').text(" It is the radiative skin temperature of the land derived from solar radiation");

		$("#satelite").show('slow');
		$("#stext").show('slow');
		//$("#satelite option[value='avhrr']").remove();

	}

	if (eventTypeName.is('[name="vhi"]')) {
		$('#indices_discription').text("is a spectral transformation of two or more bands designed to enhance the contribution of vegetation properties and allow reliable spatial and temporal inter-comparisons of terrestrial photosynthetic activity and canopy structural variations");

		$("#satelite").show('slow');
		$("#stext").show('slow');
		//$("#satelite option[value='modis']").remove();

	}
	if (eventTypeName.is('[name="smi"]')) {
		$('#indices_discription').text("Soil moisture is a key variable in controlling the exchange of water and heat energy between the land surface and the atmosphere through evaporation and plant transpiration. As a result,soil moisture plays an important role in the development of weather patterns and the production of precipitation");

		$("#satelite").show('slow');
		$("#stext").show('slow');
	}
});











$('#comp_indices').change(function () {
	var eventTypeName = $("#comp_indices option:selected");

	if (eventTypeName.is('[name="precipitation"]')) {
		$("#satelite1").hide('slow');
		$("#stext1").hide('slow');
	}
	if (eventTypeName.is('[name="precipitation anom"]')) {
		$("#satelite1").hide('slow');
		$("#stext1").hide('slow');
	}

	if (eventTypeName.is('[name="ndvi anomaly"]')) {


		$("#satelite1").show('slow');
		$("#stext1").show('slow');
	}

	if (eventTypeName.is('[name="ndwi anomaly"]')) {
		$("#satelite1").show('slow');
		$("#stext1").show('slow');
	}

	if (eventTypeName.is('[name="spi"]')) {

		$("#satelite1").hide('slow');
		$("#stext1").hide('slow');
	}

	if (eventTypeName.is('[name="lst"]')) {

		$("#satelite1").show('slow');
		$("#stext1").show('slow');
	}

	if (eventTypeName.is('[name="vhi"]')) {

		$("#satelite1").show('slow');
		$("#stext1").show('slow');
	}
	if (eventTypeName.is('[name="smi"]')) {

		$("#satelite1").show('slow');
		$("#stext1").show('slow');
	}
});


$('#comp_indices1').change(function () {
	var eventTypeName = $("#comp_indices1 option:selected");

	if (eventTypeName.is('[name="precipitation"]')) {

		$("#satelite2").hide('slow');
		$("#stext2").hide('slow');
	}
	if (eventTypeName.is('[name="precipitation anom"]')) {

		$("#satelite2").hide('slow');
		$("#stext2").hide('slow');
	}

	if (eventTypeName.is('[name="ndvi anomaly"]')) {


		$("#satelite2").show('slow');
		$("#stext2").show('slow');
	}

	if (eventTypeName.is('[name="ndwi anomaly"]')) {

		$("#satelite2").show('slow');
		$("#stext2").show('slow');
	}

	if (eventTypeName.is('[name="spi"]')) {

		$("#satelite2").hide('slow');
		$("#stext2").hide('slow');
	}

	if (eventTypeName.is('[name="lst"]')) {

		$("#satelite2").show('slow');
		$("#stext2").show('slow');
	}

	if (eventTypeName.is('[name="vhi"]')) {

		$("#satelite2").show('slow');
		$("#stext2").show('slow');
	}
	if (eventTypeName.is('[name="smi"]')) {

		$("#satelite2").show('slow');
		$("#stext2").show('slow');
	}
});

$('#comp_indices2').change(function () {
	var eventTypeName = $("#comp_indices2 option:selected");

	if (eventTypeName.is('[name="precipitation"]')) {

		$("#satelite3").hide('slow');
		$("#stext3").hide('slow');
	}

	if (eventTypeName.is('[name="precipitation anom"]')) {

		$("#satelite3").hide('slow');
		$("#stext3").hide('slow');
	}

	if (eventTypeName.is('[name="ndvi anomaly"]')) {


		$("#satelite3").show('slow');
		$("#stext3").show('slow');
	}

	if (eventTypeName.is('[name="ndwi anomaly"]')) {


		$("#satelite3").show('slow');
		$("#stext3").show('slow');
	}

	if (eventTypeName.is('[name="spi"]')) {


		$("#satelite3").hide('slow');
		$("#stext3").hide('slow');
	}

	if (eventTypeName.is('[name="lst"]')) {

		$("#satelite3").show('slow');
		$("#stext3").show('slow');
	}

	if (eventTypeName.is('[name="vhi"]')) {


		$("#satelite3").show('slow');
		$("#stext3").show('slow');
	}
	if (eventTypeName.is('[name="smi"]')) {

		$("#satelite3").show('slow');
		$("#stext3").show('slow');
	}
});

$('#comp_indices3').change(function () {
	var eventTypeName = $("#comp_indices3 option:selected");

	if (eventTypeName.is('[name="precipitation"]')) {


		$("#satelite4").hide('slow');
		$("#stext4").hide('slow');
	}

	if (eventTypeName.is('[name="precipitation anom"]')) {


		$("#satelite4").hide('slow');
		$("#stext4").hide('slow');
	}

	if (eventTypeName.is('[name="ndvi anomaly"]')) {


		$("#satelite4").show('slow');
		$("#stext4").show('slow');
	}

	if (eventTypeName.is('[name="ndwi anomaly"]')) {
		$("#satelite4").show('slow');
		$("#stext4").show('slow');
	}

	if (eventTypeName.is('[name="spi"]')) {
		$("#satelite4").hide('slow');
		$("#stext4").hide('slow');
	}

	if (eventTypeName.is('[name="lst"]')) {

		$("#satelite4").show('slow');
		$("#stext4").show('slow');
	}

	if (eventTypeName.is('[name="vhi"]')) {

		$("#satelite4").show('slow');
		$("#stext4").show('slow');
	}
	if (eventTypeName.is('[name="smi"]')) {

		$("#satelite4").show('slow');
		$("#stext4").show('slow');
	}
});


$("#md1").click(function () {
	$("#comparemap").hide(500);
	$("#indicesmap").show();


});

$("#md2").click(function () {
	$("#indicesmap").hide(500);
	$("#comparemap").css("visibility", "visible");
	$("#comparemap").show();
});
















