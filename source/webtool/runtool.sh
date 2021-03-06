
# Run the tool for the first time with 
docker run -d -p 80:80 --name cannr-web -v /projects --mount type=bind,source=/Users/ptendick/Documents/GitHub/CANNR/external,target=/external cannr-web
