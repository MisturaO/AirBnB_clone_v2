#!/usr/bin/env bash
# script that sets up my web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
if [[ !-d '/data' ]]; then
	mkdir '/data'
if [[ !-d '/data/web_static' ]]; then
	mkdir '/data/web-static'
if [[ !-d '/data/web_static/releases' ]]
	mkdir 'data/web_static/releases'
if [[ !-d 'data/web_static/shared' ]]
	mkdir 'data/web_static/shared'
if [[ !-d 'data/web_static/'  ]]
