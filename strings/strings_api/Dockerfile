FROM python:3
MAINTAINER Gustavo Correia Gonzalez

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /usr/src/app

ENTRYPOINT ["hug"]

CMD ["-f", "strings_apis/app.py"]
