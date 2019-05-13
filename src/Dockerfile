FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /src
COPY requirements.txt requirements.txt
#RUN  apt-get update && apt-get install -y uwsgi
RUN pip3 install uwsgi
RUN pwd && ls && pip3 install -r ./requirements.txt
COPY ./ /src
RUN ls
RUN chmod +x /src/inception.sh
ENTRYPOINT ["./inception.sh"]
EXPOSE 8080/tcp
EXPOSE 8081/tcp