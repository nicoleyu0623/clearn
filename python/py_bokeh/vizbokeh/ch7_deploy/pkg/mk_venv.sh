#!/bin/sh

mkdir -p /var/log/nginx/flask
mkdir -p /opt/webapps/bokehflask

mkdir /opt/envs

#virtualenv /opt/envs/virtual #for python2
python3 -m venv /opt/envs/virtual


