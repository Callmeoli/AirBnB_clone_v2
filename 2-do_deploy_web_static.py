#!/usr/bin/python3
""" Function that compress a folder """
from fabric.api import env, run, put
import os

def do_deploy(archive_path):
    """ a function that deploy our web static"""
    env.hosts = ['34.232.69.130', '100.26.216.95']
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            os.path.basename(archive_path)
            file = os.path.basename(archive_path)
            filename = file.split(".")[0]
            run("tar –xvzf /tmp/{} –C /data/web_static/releases/{}".format(file, filename))
            run("rm -rf /tmp/{}".format(archive_path))
            run("unlink /data/web_static/current")
            run("ln -s /data/web_static/current /data/web_static/releases/{}".format(filename))
        except Exception:
            return False
    else:
        return False
