#!/usr/bin/env bash
# This script sets up your web servers for the deployment of 'web_static'
# This script is to be executed in my ALX servers web-01 and web-02
apt-get -y update
apt-get -y install nginx

# Creates files and folders if they don't already exists
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "ALX Software Engineering " > /data/web_static/releases/test/index.html

# Creates a symbolic link from 'link_path' to 'target_path' and delete symb link
# if it already exist, then recreate it everytime the script is run
link_path="/data/web_static/current"
target_path="/data/web_static/releases/test/"
if [ -L "$link_path" ]; then
    rm "$link_path"
fi
# Below creates the symbolic link
ln -s "$target_path" "$link_path"

# Gives ownership of the file to the 'ubuntu' user
chown -R ubuntu /data/
chgrp -R ubuntu /data/


# Update the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static using alias directive
location_block='\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}'
sed -i "/server_name _;/a$location_block" /etc/nginx/sites-available/default

# You need to start nginx every time the server config file is updated 
service nginx start
