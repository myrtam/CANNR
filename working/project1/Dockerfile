# CANNR TM analytics container building tool Dockerfile template.
# Copyright 2020 Pat Tendick ptendick@gmail.com
# All rights reserved
# Maintainer Pat Tendick ptendick@gmail.com

FROM cannr-base
LABEL maintainer="someone@somewhere.com"

# Copy specific NGINX configuration
COPY conf.d/http /etc/nginx/http

# Install R packages
# No R packages to install

# Copy project contents
COPY . .

# Install Python packages
RUN python3.9 -m pip install -r requirements.txt

# Copy static content
COPY ./content/web/static /content


# Change permissions and run main script to start services
RUN chmod a+x main.sh
CMD ./main.sh
