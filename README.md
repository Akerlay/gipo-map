# GIPO-maps

GIPO-maps is a service that connects the Leaflet.js maps and openweathemap api.
![Example](https://pp.userapi.com/c849336/v849336332/192b05/mk2girpOulg.jpg)

## Deploying on your server

### Building
Before launch commands below, cd into cloned repo and configure api tokens by
```bash
python3 configure.py
```
![Config](https://pp.userapi.com/c849336/v849336332/192ae8/fEA4GgPFieM.jpg)

Then build
```bash
docker-compose build
```

### Running
```bash
docker-compose up
```
## Built With

* [Leaflet](https://github.com/Leaflet/Leaflet) - JS maps framework
* [Flask](http://flask.pocoo.org/) - python3 web framework
