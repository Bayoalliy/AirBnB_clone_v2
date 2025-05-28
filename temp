#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy:
"""

from fabric.api import *
from datetime import datetime
import os


env.hosts = ['3.82.128.8', '3.83.155.83']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """deploys a .tzg file from web_static to remote server"""

    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        f = file_name.split('.')[0]
        f_path = "/data/web_static/releases/{}".format(f)
        run('mkdir {}'.format(f_path))
        run('tar -xvzf /tmp/{} -C {}'.format(file_name, f_path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}'.format(f_path, f_path))
        run('rm -r {}/web_static'.format(f_path))
        run('rm -r /data/web_static/current')
        run('ln -sf {} /data/web_static/current'.format(f_path))
        return True
    except:
        return False
