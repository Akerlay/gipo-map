FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /maps
COPY ./maps /maps
RUN pip3 --no-cache-dir install -r requirements.txt

ENTRYPOINT  ["python3", "run.py"]
