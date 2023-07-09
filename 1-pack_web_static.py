#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo, using the function do_pack
from fabric.api import local
import os.path
from datetime import datetime


def do_pack():
    """Creates a tar gzipped file archive of directory web_static
    to be transfered to the server as a compressed file"""
    file = 'web_static_'
    dt_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = file + dt_time + ".tgz"

    if os.path.isdir('versions') is False:
        if local('mkdir -p versions').failed is True:
            return None
    if local('tar -cvzf versions/{} web_static'
             .format(file_name)).failed is True:
        return None
    return "versions/" + file_name
