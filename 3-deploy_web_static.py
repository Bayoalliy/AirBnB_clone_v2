#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import *
from datetime import datetime
import os


env.hosts = ['3.82.128.8', '3.83.155.83']
env.user = 'ubuntu'


def do_pack():
    """creates a .tzg file from web_static"""
    if not os.path.exists('versions'):
        local('mkdir -p versions')
    d = datetime.now()
    arch_path = f'versions/web_static_{d.strftime("%Y%m%d%H%M%S")}.tgz'
    res = local(f'tar -czvf {arch_path} web_static', capture=True)
    if res.succeeded:
        return arch_path
    else:
        return None




def do_deploy(archive_path):                                              """deploys a .tzg file from web_static to remote server"""

    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')                                            file_name = archive_path.split('/')[-1]
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


def deploy():
    """creates and distributes an archive to your web servers"""
    res = do_pack()
    if not res:
        return False

    do_deploy(res)
