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
        f = file_name[:-4]
        f_path = f"/data/web_static/releases/{f}"
        run(f'mkdir {f_path}')
        run(f'tar -xvzf /tmp/{file_name} -C {f_path}')
        run(f'rm /tmp/{file_name}')
        run(f'mv {f_path}/web_static/* {f_path}')
        run('rm -r /data/web_static/current')
        run(f'ln -sf {f_path} /data/web_static/current')
        return True
    except:
        return False
