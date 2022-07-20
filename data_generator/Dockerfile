FROM python:3.8.12-slim

# set work directory
WORKDIR /usr/src/app/project
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update -y
RUN apt-get install libgomp1 -y

RUN pip install --upgrade pip
COPY project/ /usr/src/app/project/

RUN pip install -r requirements.txt

# copy project
COPY project /usr/src/app/project/
