#!/usr/bin/env bash
# bash script that facilitate deployment of webstatic

if ! command -v <the_command> &> /dev/null
then
    apt-get upgrade
    apt-get install nginx 
fi
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

touch /data/web_static/releases/test/index.html
echo "Test for index" >> index.html

ln -sf /data/web_static/current /data/web_static/releases/test/
chown -hR ubuntu:ubuntu /data/
new_loc="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sed -i "38i\ $new_loc" /etc/nginx/sites-available/default
service restart nginx
