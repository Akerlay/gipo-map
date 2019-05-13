# GIPO-maps

GIPO project wich connects Leaflet.js maps and openweathemap api.
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
* [Flask](http://flask.pocoo.org/) - The web framework used

## Authors

* **Kirill Mineev** - *python/js/docker* - [Akerlay](https://github.com/Akerlay)
* **Mikhail Selyankin** - *python* - [selyankin](https://github.com/selyankin)
* **Davyd Norin** - *html/css*
