# set base image (host OS)
FROM python:3.8-slim

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt
# RUN pip install "celery[redis]"

# copy the content of the local app directory to the working directory
COPY app/ .

EXPOSE 3000
