const server = "http://0.0.0.0";
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

}

function showPopup(lat, lon) {
  weather = $.ajax({
                  url: server + "/get-weather",
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
