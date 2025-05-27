#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy:
"""

from fabric.api import local, run, put, env
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
        run(f'tar -xvzf /tmp/{file_name} -C /data/web_static/releases/')
        run(f'rm /tmp/{file_name}')
        run(f'ln -sfn /data/web_static/releases/{file_name} \
                /data/web_static/current')
        return True
    except:
        return False
