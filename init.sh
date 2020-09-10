# initialize environment

sudo cp ./nginx.conf /etc/nginx/nginx.conf
cd ./web
gunicorn -c ./../etc/gunicorn.py hello:application &> ./gunicorn.access.log &
sudo nginx
