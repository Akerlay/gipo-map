let mymap;


function setup(){
  mymap = L.map('mapid').setView([50, 40], 7);
  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiYWtlcmxheSIsImEiOiJjanZqampjejAwaGMwNDZrM3RvMnFxdTF0In0.wpnO6xhUSOC6m0HK3MHkfQ'
  }).addTo(mymap);

  L.tileLayer("https://tile.openweathermap.org/map/temp_new/{z}/{x}/{y}.png?appid={appid}", {
    maxZoom: 18,
    appid: '64ed697ea8b17ac57034a397407b4116'
  }).addTo(mymap);

  mymap.addEventListener('click', function(ev) {
    lat = ev.latlng.lat;
    lon = ev.latlng.lng;
    showPopup(lat, lon)
  });

  document.getElementById('sr-button').addEventListener('click', findCity);
  $('#sr-input').keypress(function(event){
	var keycode = (event.keyCode ? event.keyCode : event.which);
	if(keycode == '13'){
		findCity()
	}

  });
}

function findCity() {
    city = document.getElementById('sr-input').value;
    resp = $.ajax({
      url: '/find-city',
      method: 'POST',
      data: {'city': city},
      async: false,
      dataType: 'json'
    }).responseJSON;
    mymap.panTo(new L.LatLng(resp['lat'], resp['lon']));
    showPopup(resp['lat'], resp['lon'])

}

function showPopup(lat, lon) {
  weather = $.ajax({
                  url: "/get-weather",
                  method: 'POST',
                  data: {'lat': lat, 'lon': lon},
                  async: false,
                  dataType: 'json'
                  }).responseJSON;

  let popup_content = _.template(document.getElementById('popup-template').innerHTML);

  let popup = L.popup()
               .setLatLng([weather['lat'], weather['lon']])
               .setContent(popup_content(weather))
               .openOn(mymap);
}

function draw(){

}
