# Startup script

# Start workers
python /folders/tool/tool.py 5001 &

# Start NGINX
nginx -g 'daemon off;'
