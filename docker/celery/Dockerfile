FROM python:3.12-slim
WORKDIR /opt/app

COPY docker/backend/requirements.txt /opt/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt -y update \
    && pip3 install --upgrade pip \
    && pip3 install -r  requirements.txt --no-cache-dir 

COPY src/ /opt/app
