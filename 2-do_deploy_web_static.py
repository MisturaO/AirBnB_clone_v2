#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo, using the function do_pack
from fabric.api import run
import os.path
from fabric.api import put
from fabric.api import env

env.hosts = ["3.90.81.72", "3.85.148.246"]


def do_deploy(archive_path):
    """
    Write a Fabric script (based on the file 1-pack_web_static.py) that
    distributes an archive to your web servers, using the function do_deploy:

    Args:
        archive_path(str): The path of the archive to distribute to web servers
    Returns:

    """
    if os.path.isfile(archive_path) is False:
        return False
    
    """Path to uncompress archive_path to """
    path = '/data/web_static/releases/'
    """ Archive path without the .tgz extension. Ready to be added to 'path'"""
    file = archive_path.split('/')[-1]
    name = file.split('.')[0]

    """Checks archive_path is inside the /temp/ dir"""
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    """Deletes the archive file from web server otherwise return False"""
    if run("rm rf {}+{}".format(path, name)).failed is True:
        return False
    if run("mkdir -p {}{}/".format(path, name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C {}{}/".format(file, path, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv {}/{}/web_static/*{}{}/".format(path, name, path, name)).failed is True:
        return False
    if run("rm -rf {}{}/web_static".format(path, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s {}{}/ /data/web_static/current".format(path, name)).failed is True:
        return False
    return True