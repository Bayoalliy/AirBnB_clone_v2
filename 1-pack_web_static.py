#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    if not os.path.exists('versions'):
        local('mkdir -p versions')
    d = datetime.now()
    arch_path = f'versions/web_static_{d.strftime("%Y%m%d%H%M%S")}.tgz'
    res = local(f'tar -czvf {arch_path} web_static', capture=True)
    if res.succeeded:
        return arch_path
    else:
        return None
