#!/usr/bin/python3
""" distribute deployed """

from fabric.api import env, run, put
import os
env.hosts = ['34.232.69.130', '100.26.216.95']

def do_deploy(archive_path):
    """ a function that deploy our web static"""

    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            os.path.basename(archive_path)
            file = os.path.basename(archive_path)
            filename = file.split(".")[0]
            run("mkdir -p /data/web_static/releases/{}/".format(filename))
            run("tar -xzf /tmp/{0} -C\
                 /data/web_static/releases/{1}/".format(file, filename))
            run("rm -rf /tmp/{}".format(archive_path))
            run('mv /data/web_static/releases/{0}/web_static/*\
                 /data/web_static/releases/{1}/'.format(filename, filename))
            run('rm -rf\
                 /data/web_static/releases/{0}/web_static/'.format(filename))
            run('rm -rf /data/web_static/current')
            run("ln -s /data/web_static/releases/{}\
                 /data/web_static/current".format(filename))
            return True
        except Exception:
            return False
    else:
        return False

def do_pack():
    """ Function that compress a folder """
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except Exception:
        return None

def deploy():
    """ a function that deploy """

    try:
        pack = do_pack()
        if pack is None:
            return False
        dep = do_deploy(pack)
        return dep
    except Exception:
        return False
