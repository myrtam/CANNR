# CANNR TM analytics container building tool Dockerfile template.
# Copyright 2020 Pat Tendick ptendick@gmail.com
# All rights reserved
# Maintainer Pat Tendick ptendick@gmail.com

FROM <base image>
#<maintainer>

# Copy specific NGINX configuration
COPY conf.d/http /etc/nginx/http

# Install R packages
#<R Packages>

# Copy project contents
COPY . .

# Install Python packages
RUN pip3 install -r requirements.txt

# Copy static content
#<Static Content>

# Change permissions and run main script to start services
RUN chmod a+x main.sh
CMD ./main.sh
