# Startup script

# Start workers
python /folders/pyFolder/pyFolder.py 4000 &
Rscript --vanilla /usr/local/cannr/runApp.R /folders/rFolder/iris.R 4001 1 &
Rscript --vanilla /usr/local/cannr/runApp.R /folders/rFolder/sum.R 4002 1 &

# Start NGINX
nginx -g 'daemon off;'
