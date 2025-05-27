#!/usr/bin/env bash
#Write a Bash script that sets up your web servers for the deployment of web_static.
apt update
apt install -y nginx
mkdir -p /data/web_static/releases/test/
echo "Hello world!" > /data/web_static/releases/test/index.html
mkdir -p /data/web_static/shared/
ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/pass PHP/i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
