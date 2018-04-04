var colorlegend = function (target,act ,scale, type,indices, options) {
	var scaleTypes = ['linear', 'quantile', 'ordinal']
		, found = false
		, opts = options || {}
		, boxWidth = opts.boxWidth || 20        // width of each box (int)
		, boxHeight = opts.boxHeight || 20      // height of each box (int)
		, title = opts.title || null            // draw title (string)
		, fill = opts.fill || false             // fill the element (boolean)
		, linearBoxes = opts.linearBoxes || 9   // number of boxes for linear scales (int)
		, htmlElement = act
		console.log(htmlElement)// target container element - strip the prefix #

		, w = 220          // width of container element
		console.log(w)
		, h =300       // height of container element
		, colors = []
		, padding = [2, 4, 10, 4]               // top, right, bottom, left
		, boxSpacing = type === 'ordinal' ? 3 : 3 // spacing between boxes
		, titlePadding = title ? 11 : 1
		, domain = (indices === "lst") ? ['Very Low', 'Low', 'Moderate', 'Hot', 'Very Hot'] : (indices === "vhi") ? ['Wet', 'No Drought/Normal', 'Moderate Drought', 'Severe Drought', 'Extreme Drought'] : (indices === "precipitation") ? ['Exceptional Less', 'Extremely Less', 'Severely Less', 'Moderately Less', 'Abnormally Less', 'Neutral', 'Abnormally Rainy', 'Moderately Rainy', 'Severely Rainy', 'Extremely Rainy', 'Exceptionally Rainy'] : (indices === "ndwi_anomaly") ? ['Extremely Dry', 'Severely Dry', 'Moderately Dry', 'Near Normal', 'Normal', 'Moderately Wet', 'Very Wet', 'Extremely Wet'] : (indices === "ndvi_anomaly") ? ['Extremely Dry', 'Severely Dry', 'Moderately Dry', 'Near Normal', 'Moderately Wet', 'Very Wet', 'Extremely Wet'] : (indices === "spi") ? ['Exceptional Dry', 'Extremely Dry', 'Severely Dry', 'Moderately Dry', 'Abnormally Dry', 'Neutral', 'Abnormally Wet', 'Moderately Wet', 'Severely Wet', 'Extremely Wet', 'Exceptionally Wet'] : (indices === "smi") ? ['Exceptional Dry', 'Extremely Dry', 'Severely Dry', 'Moderately Dry', 'Abnormally Dry', 'Neutral', 'Abnormally Wet', 'Moderately Wet', 'Severely Wet', 'Extremely Wet', 'Exceptionally Wet'] : (indices === "NDVI") ? ["Extremely Low", "Very Low", "Low", "Near Normal", "Normal", "High", "Very High", "Extremely High"] : (indices === "NDWI") ? ['Extremely Low', 'Severely Low', 'Moderately Low', 'Near Normal', 'Normal', 'Moderately High', 'Very High', 'Extremely High'] : (indices === "EVI") ? ["Extremely Low", "Very Low", "Low", "Near Normal", "Normal", "High", "Very High", "Extremely High"] : [""]
		
		, range = scale.range()
		, i = 0
		, isVertical = opts.vertical || true;

	
	// check for valid input - 'quantize' not included
	for (i = 0; i < scaleTypes.length; i++) {
		if (scaleTypes[i] === type) {
			found = true;
			break;
		}
	}
	if (!found)
		throw new Error('Scale type, ' + type + ', is not suported.');


	// setup the colors to use
	if (type === 'quantile') {
		colors = range;
	}
	else if (type === 'ordinal') {
		for (i = 0; i < domain.length; i++) {
			colors[i] = range[i];
		}
	}
	else if (type === 'linear') {
		var min = domain[0];
		var max = domain[domain.length - 1];
		for (i = 0; i < linearBoxes; i++) {
			colors[i] = scale(min + i * ((max - min) / linearBoxes));
		}
	}

	// check the width and height and adjust if necessary to fit in the element use the range if quantile
	if (!isVertical) {
		if (fill || w < (boxWidth + boxSpacing) * colors.length + padding[1] + padding[3]) {
			boxWidth = (w - padding[1] - padding[3] - (boxSpacing * colors.length)) / colors.length;
		}
		if (fill || h < boxHeight + padding[0] + padding[2] + titlePadding) {
			boxHeight = h - padding[0] - padding[2] - titlePadding;
		}

	} else {
		if (fill || h < (boxHeight + boxSpacing) * colors.length + padding[0] + padding[2]) {
			boxHeight = (h - padding[0] - padding[2] - (boxSpacing * colors.length)) / colors.length;
		}
		if (fill || w < boxWidth + padding[1] + padding[3] + titlePadding) {
			boxWidth = w - padding[1] - padding[3] - titlePadding;
		}
	}





	// set up the legend graphics context
	var legend = d3.select(htmlElement)
		
		.append('svg')
		.attr('width', w)
		.attr('height', h)
		.append('g')
		.attr('class', 'colorlegend')
		.attr('transform', 'translate(' + padding[3] + ',' + padding[0] + ')')
		.style('font-size', '14px')
		.style('fill', '#000');

	var legendBoxes = legend.selectAll('g.legend')
		.data(colors)
		.enter().append('g');
	console.log(legend)
	// value labels
	var valueLabels;
	if (!isVertical) {
		valueLabels = legendBoxes.append('text')
			.attr('class', 'colorlegend-labels')
			.attr('dy', '.81em')
			.attr('x', function (d, i) {
				return i * (boxWidth + boxSpacing) + (type !== 'ordinal' ? (boxWidth / 2) : 0);
			})
			.attr('y', function () {
				return boxHeight + 2;
			});
	} else {
		valueLabels = legendBoxes.append('text')
			.attr('class', 'colorlegend-labels')
			.attr('dy', padding[0])
			.attr('x', function () {
				// return boxWidth + titlePadding;
				return titlePadding;
			})
			.attr('y', function (d, i) {
				return i * (boxHeight + boxSpacing) + boxHeight / 2;
			});
	}
	valueLabels
		.style('text-anchor', function () {
			return type === 'ordinal' ? 'start' : 'start';
		})
		.style('pointer-events', 'none')
		.text(function (d, i) {

			// show label for all ordinal values
			if (type === 'ordinal') {
				return domain[i];
			}
			// show only the first and last for others
			else {
				return domain[i];

				//if (i === 0)
				//	return domain[0];
				//if (i === colors.length - 1)
				//	return domain[domain.length - 1];
			}
		});


	// the colors, each color is drawn as a rectangle
	if (!isVertical) {
		legendBoxes.append('rect')
			.attr('x', function (d, i) {
				return i * (boxWidth + boxSpacing);
			})
			.attr('width', boxWidth)
			.attr('height', boxHeight)
			.style('fill', function (d, i) { return colors[i]; });

	} else {
		legendBoxes.append('rect')
			.attr('y', function (d, i) {
				return i * (boxHeight + boxSpacing);
			})
			.attr('x', function () {
				return w - boxWidth - padding[1] - padding[3];
			})
			.attr('width', boxWidth)
			.attr('height', boxHeight)
			.style('fill', function (d, i) { return colors[i]; });
	}

	// show a title in center of legend (bottom)
	if (title) {
		var legendText = legend.append('text')
			.attr('class', 'colorlegend-title')
			.style('text-anchor', 'middle')
			.style('pointer-events', 'none')
			.text(title);

		if (!isVertical) {
			legendText
				.attr('dy', '.71em')
				.attr('x', (colors.length * (boxWidth / 2)))
				.attr('y', boxHeight + titlePadding);

		} else {
			legendText
				.attr('dy', '.51em')
				.attr('y', (colors.length * (boxHeight / 2)))
				.attr('transform', 'rotate(90, 5,' + (colors.length * (boxHeight / 2)) + ')');
		}
	}

	return this;
}