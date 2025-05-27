#!/usr/bin/env bash
#Write a Bash script that sets up your web servers for the deployment of web_static.
mkdir -p /data/web_static/releases/test/
echo "<html><body><h1>Heloo worlddd!</h1></body></html>" > /data/web_static/releases/test/index.html
mkdir -p /data/web_static/shared/
ln -sfn /data/web_static/releases/test/ /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sed '/location/i \\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}' /etc/nginx/sites-available/default
