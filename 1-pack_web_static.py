#!/usr/bin/python3
"""A fabfile to zip web_static folder"""
import os
from datetime import datetime
from fabric.api import *


def do_pack():
    """pack the files"""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    if not os.path.isdir('versions'):
        parent_dir = os.getcwd()
        full_path = os.path.join(parent_dir, 'versions')
        os.makedirs(full_path)
    cmd = 'tar -cvfz /versions/web_static_{}.tgz web_static'.format(date)
    if local('{}'.format(cmd)).failed:
        return None
