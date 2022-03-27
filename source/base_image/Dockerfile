# CANNR TM analytics container building tool base container.
# Copyright 2020 Pat Tendick ptendick@gmail.com
# All rights reserved
# Maintainer Pat Tendick ptendick@gmail.com

# Use Rocker image
#FROM r-base:4.1.3
FROM rocker/tidyverse:4.1.3

# Install required libraries
RUN apt-get -y update --fix-missing
RUN apt-get -y install libssl-dev
RUN apt-get -y install libxml2-dev
RUN apt-get -y install libcurl4-openssl-dev
RUN apt-get -y install libsodium-dev
RUN apt-get -y install libsodium23
RUN apt-get -y install libgmp3-dev
RUN apt-get -y install libglpk-dev

# Install VIM
RUN apt-get -y install vim

# Install Python 3.9
RUN apt -y update --fix-missing
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt -y install python3.9
RUN apt-get -y install python3-pip

# Create symlink and modify path
RUN ln -s /usr/bin/python3.9 python
ENV PATH=$PATH:/

# Copy the requirements file, install Python packages, and set PYTHONPATH
COPY requirements.txt .
ENV PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.9/dist-packages/
RUN python3.9 -m pip install -r requirements.txt

# Install NGINX community edition and create log directories
RUN apt install -y nginx
RUN mkdir -p /etc/nginx/logs
RUN mkdir -p /usr/share/nginx/logs/

# Install R packages
RUN install2.r plumber
RUN install2.r urltools

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
