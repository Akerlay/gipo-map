let myMap;
let canvas;
const server = "http://127.0.0.1:5000";
let placesToRender;
let mymap;




function setup(){
  mymap = L.map('mapid').setView([50, 40], 7);
  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiYWtlcmxheSIsImEiOiJjanZqampjejAwaGMwNDZrM3RvMnFxdTF0In0.wpnO6xhUSOC6m0HK3MHkfQ'
}).addTo(mymap);
  L.tileLayer("https://tile.openweathermap.org/map/temp_new/{z}/{x}/{y}.png?appid={appid}", {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    appid: '64ed697ea8b17ac57034a397407b4116'
}).addTo(mymap);


  //"https://tile.openweathermap.org/map/temp_new/{z}/{x}/{y}.png?appid=64ed697ea8b17ac57034a397407b4116",

  placesToRender = $.ajax({
    url: server + "/get-weather",
    method: 'POST',
    async: false,
    dataType: 'json'
  }).responseJSON;



  textStyle(BOLD);
  fill(200, 100, 100);


  for (let i = 0; i < placesToRender.length; i++) {
      let place = placesToRender[i];
      let circle = L.circle([place['lat'], place['lon']], {
        color: [0, 255, 0],
        fillColor: calc_color(place['temp']),
        fillOpacity: 0.9,
        radius: 30000
      }
      ).addTo(mymap);
      circle.bindPopup(place['title'] + ': ' + place['temp'] + '°');
  }
}

function rgbToHex(value) {
  let hex = Number(value).toString(16);
  if (hex.length < 2) {
       hex = "0" + hex;
  }
  return hex;
}

function hexify(r, g, b) {
  let red = rgbToHex(r);
  let green = rgbToHex(g);
  let blue = rgbToHex(b);
  return '#'+red+green+blue;
}

function draw(){

  // eskere;
  // clear();
  // for (let i = 0; i < placesToRender.length; i++) {
  //   let place = placesToRender[i];
  //   let pos = myMap.latLngToPixel(place["lat"], place["lon"]);
  //
  //   let col = calc_color(place['temp']);
  //   fill(col);
  //   ellipse(pos.x, pos.y, 20, 20);
  //
  //   fill(100, 100, 100);
  //   text(place['temp'] + "°", pos.x, pos.y - 12)


  // }
}

function calc_color(temp) {
  let num_temp = parseFloat(temp);
  let k = 3;
  let r = Math.round(150 + k * num_temp);
  if (r > 255)
    r = 255;
  let g = 0;
  let b = Math.round(150 - k * num_temp);
  if (b < 0)
    b = 0;
  let result = hexify(r, g, b);
  console.log(result);
  return result;
}