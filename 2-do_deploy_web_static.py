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
        Returns True if all operations have been done
        correctly, otherwise returns False

    """
    if os.path.isfile(archive_path) is False:
        return False

    """ Archive path without the .tgz extension. Ready to be added to 'path'"""
    file = archive_path.split('/')[-1]
    name = file.split('.')[0]
    """full path of the uncompressed archive_path"""

    try:
        """uploads the archive_path to the /tmp/ dir in the remote server"""
        put(archive_path, '/tmp/')

        """Creates the dir structure we will send the uncompressed archived file into"""
        run('mkdir -p /data/web_static/releases/{}'.format(name))
        
        """ uncompresses the archive from the folder "//tmp/data/web_static/releases/
        to the file path /tmp/data/web_static/releases/name"""
        run('tar -xzf /tmp/data/web_static/releases/ -C /data/web_static/releases/{}'.format(name))
    
        """Deletes the archive from the web server in the /tmp/ directory."""
        run('rm /tmp/{}'.format(archive_path))
    
        """Deletes the symbolic link '/data/web_static/current' from the web server"""
        run('rm -rf /data/web_static/current')

        """Creates a new the symbolic link '/data/web_static/current' on the web server,
        linked to new uncompressed archive file path /data/web_static/releases/name (i.e <file
        name without extension>)"""
        run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(name))
        return True
    except Exception: 
        return False