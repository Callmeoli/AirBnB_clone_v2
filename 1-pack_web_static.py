#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
import fabric
import os


def do_pack():
    try:
        if not os.path.exists("versions"):
            fabric.local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        fabric.local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except:
        return None