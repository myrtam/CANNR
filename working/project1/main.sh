# Startup script

# Start workers
python /folders/pyfolder/pyfolder.py 5001 &
Rscript --vanilla /usr/local/cannr/runApp.R /folders/rfolder/iris.R 5002 1 &
Rscript --vanilla /usr/local/cannr/runApp.R /folders/rfolder/sum.R 5003 1 &

# Start NGINX
nginx -g 'daemon off;'
