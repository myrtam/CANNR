# CANNR TM analytics container building tool base container.
# Copyright 2020 Pat Tendick ptendick@gmail.com
# All rights reserved
# Maintainer Pat Tendick ptendick@gmail.com

# Use Rocker image
FROM r-base

# Install required libraries
RUN apt-get update --fix-missing
RUN apt-get -y install libcurl4-openssl-dev
RUN apt-get -y install libsodium-dev
RUN apt-get -y install libsodium23

# Install Python 3.9
RUN apt update --fix-missing
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.9

# Create symlink and modify path
RUN ln -s /usr/bin/python3.9 python
ENV PATH=$PATH:/

# Install pip3
RUN apt-get -y install python3-pip

# Install Python packages and set PYTHONPATH
RUN pip3 install docker
RUN pip3 install stdlib_list
RUN pip3 install flask
RUN pip3 install pandas
RUN pip3 install numpyencoder
ENV PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.9/dist-packages/

# Install NGINX community edition and create log directories
RUN apt install -y nginx
RUN mkdir -p /etc/nginx/logs
RUN mkdir -p /usr/share/nginx/logs/

# Install R packages
RUN install2.r plumber
RUN install2.r urltools
RUN install2.r stringr
#RUN install2.r objectstore

# Create the event calendar directory
RUN mkdir -p /eventCalendar

# Add the /web directory, which is exposed through NGINX
RUN mkdir -p /content
RUN mkdir -p /content/web
RUN mkdir -p /content/temp

# Copy base NGINX configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy project contents and set PYTHONPATH
COPY cannr /usr/local/cannr
ENV PYTHONPATH=$PYTHONPATH:/usr/local/cannr/lib

# Install local R packages
RUN cd /usr/local/cannr/packages && Rscript installpack.R

# Set DOCKER_HOST so tool can access Docker on the host machine
#ENV DOCKER_HOST=host.docker.internal
