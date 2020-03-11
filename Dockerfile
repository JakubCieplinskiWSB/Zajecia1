FROM alpine:latest

USER root

ENV FLASK_APP /home/app/application.py
ENV AP /home/app

RUN apk add --update-cache \
    python \
    python-dev \
    py-pip \
    build-base \
    bash \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

RUN mkdir /home/app
RUN mkdir /home/app/templates

ADD *.txt* $AP/
ADD templates/*.html* $AP/templates
ADD *.py* $AP/

RUN pip install -r ${AP}/requirements.txt
EXPOSE 5000/tcp


CMD [ "flask", "run", "--host", "0.0.0.0"]