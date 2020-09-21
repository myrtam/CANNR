# Startup script

# Start workers
python /folders/pyFolder1/pyFolder1.py 5000 &
Rscript --vanilla /usr/local/cannr/runApp.R /folders/folder2/iris.R /folders/folder2/folder2 5001 1 &
Rscript --vanilla /usr/local/cannr/runApp.R /folders/folder2/sum.R /folders/folder2/folder2 5002 1 &

# Start NGINX
nginx -g 'daemon off;'
