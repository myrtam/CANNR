# Startup script

# Start workers
python /folders/pyFolder/pyFolder.py 5000 &
Rscript --vanilla /usr/local/cannr/runApp.R /folders/rFolder/iris.R 5001 1 &
Rscript --vanilla /usr/local/cannr/runApp.R /folders/rFolder/sum.R 5002 1 &

# Start NGINX
nginx -g 'daemon off;'
