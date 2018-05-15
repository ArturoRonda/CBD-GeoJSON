var geojson = new XMLHttpRequest();
geojson.open("GET", document.currentScript.getAttribute("map"),true);

geojson.addEventListener("load",  geojsonLoaded);
geojson.myParam1 = document.currentScript.getAttribute("longitud");
geojson.myParam2 = document.currentScript.getAttribute("latitud");
geojson.send() 

function geojsonLoaded() {
	featuresObject = JSON.parse(geojson.response)
	
	var geojsonMarkerOptions = {
		radius: 8,
		fillColor: "#ff5000",
		color: "#ffffff",
		weight: 1,
		opacity: 1,
		fillOpacity: 0.75
	};
	function pointToLayer(feature, latlng) {
		geojsonMarkerOptions.fillColor = feature.properties["marker-color"]
		return L.circleMarker(latlng, geojsonMarkerOptions);
	}
	
	function onEachFeature(feature, layer) {
		layer.bindPopup(feature.properties.title + "</br>" + 
			feature.properties.description + "</br>" +
			feature.properties.type);
	}

	var mymap = L.map('mapid').setView([parseFloat(geojson.myParam2),  parseFloat(geojson.myParam1)], 13);
	//L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	L.tileLayer('https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors | ' + featuresObject.features.length + ' caches found'
	}).addTo(mymap);
	L.geoJSON(featuresObject, {
		pointToLayer: pointToLayer,
		onEachFeature: onEachFeature
	}).addTo(mymap)
}
