template = '''version: '3'
services:
  flask:
    build: ./src
    command: /src/inception.sh
    stdin_open: true
    tty: true
    volumes:
      - ./src:/app
    environment:
      YANDEX_GEOCODER_KEY: "%s"
      OWM_KEY: "%s"


  nginx:
    build: ./nginx
    depends_on:
      - flask
    ports:
      - 80:80
'''
if __name__ == '__main__':
    print('Configuring docker-compose')
    geocoder = input('YANDEX_GEOCODER_KEY: ')
    owm = input('OWM_KEY: ')
    print('"docker-compose.yml generated!"')

    with open('docker-compose.yml', 'w') as f:
        f.write(template % (geocoder, owm))
