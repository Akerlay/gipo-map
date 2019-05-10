let myMap;
let canvas;
const server = "http://127.0.0.1:5000";
const mappa = new Mappa('Leaflet');
let placesToRender;

var imgs = new Map();

const options = {
  lat: 56,
  lng: 56,
  zoom: 4,
  style: "http://{s}.tile.osm.org/{z}/{x}/{y}.png"
};

function setup(){
  placesToRender = $.ajax({
    url: server + "/get-weather",
    method: 'POST',
    async: false,
    dataType: 'json'
  }).responseJSON;

  canvas = createCanvas(windowWidth,windowHeight);
  myMap = mappa.tileMap(options);
  myMap.overlay(canvas);

  textStyle(BOLD);

  fill(200, 100, 100);
}

function draw(){
  clear();
  for (let i = 0; i < placesToRender.length; i++) {
    let place = placesToRender[i];
    let pos = myMap.latLngToPixel(place["lat"], place["lon"]);
    // fill(200, 100, 100);
    // ellipse(pos.x, pos.y, 20, 20);
    let s;
    if (!imgs.has(place['icon'])) {
      s = loadImage('https://crossorigin.me/https://yastatic.net/weather/i/icons/blueye/color/svg/' + place['icon']);
      imgs[place['icon']] = s;
    } else {
      s = imgs[place['icon']];
    }
    s.crossOrigin = "";
    image(s, pos.x, pos.y, 10000, 10000);

    fill(100, 100, 100);
    text(place['temp'] + "°", pos.x, pos.y - 12)
  }
}