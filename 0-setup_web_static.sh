#!/usr/bin/env bash
# script that sets up my web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
if [[ ! -d /data ]]; then
        mkdir /data
fi
if [[ ! -d /data/web_static ]]; then
        mkdir /data/web_static
fi
if [[ ! -d /data/web_static/releases ]]; then
        mkdir /data/web_static/releases
fi
if [[ ! -d /data/web_static/shared ]]; then
        mkdir /data/web_static/shared
fi
if [[ ! -d /data/web_static/current  ]]; then
        mkdir /data/web_static/current
        ln -fs /data/web_static/current /data/web_static/releases/test
        echo 'Hello World!' > /data/web_static/current/index.html
fi
if [[ -d /data/web_static/current ]]; then
        ln -fs /data/web_static/current /data/web_static/releases/test
fi
chown -RL ubuntu:ubuntu /data
ADD='\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}'
sed -i "/server_name _;/a $ADD" /etc/nginx/sites-available/default
service nginx restart
