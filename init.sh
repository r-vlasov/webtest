# initialize environment

sudo cp ./nginx.conf /etc/nginx/nginx.conf
gunicorn -c ./etc/gunicorn.py hello:application &> ./gunicorn.access.log &
sudo nginx
