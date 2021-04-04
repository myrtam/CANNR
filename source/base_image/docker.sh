
# Before executing this, log into Docker Hub:
# docker login -u cannr

# Build the image and tag it.
docker build -t cannr/cannr-base:latest -t cannr/cannr-base:0.1.0 .

# Push the image with all tags.
docker push cannr/cannr-base --all-tags