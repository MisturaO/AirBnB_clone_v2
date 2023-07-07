#!/usr/bin/python3
"""A fabfile to zip web_static folder"""
import os
import datetime
from fabric.api import *

def do_pack():
    """pack the files"""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    if !os.path.isdir('versions'):
        parent_dir = os.cwd()
        full_path = os.path.join(parent_dir, 'versions')
        os.mkdir(path)
    local('tar -cvfz versions/web_static_{}.tgz web_static'.format(full_path))

