#!/usr/bin/python3
"""
Write a Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean:
"""

from fabric.api import *
from datetime import datetime
import os


env.hosts = ['3.82.128.8', '3.83.155.83']
env.user = 'ubuntu'


def local_clean(n):
    res = local('ls versions/', capture=True)
    if res.succeeded:
        lst = sorted(res.splitlines())
        lst = lst[::-1]
        if not int(n):
            lst = lst[1:]
        else:
            lst = lst[int(n):]

    for file in lst:
        local('rm versions/{}'.format(file))


def remote_clean(n):
    res = run('ls /data/web_static/releases')
    if res.succeeded:
        lst = sorted(res.splitlines())
        lst = lst[::-1]
        if not int(n):
            lst = lst[1:]
        else:
            lst = lst[int(n):]

    for file in lst:
        sudo('rm -r versions/{}'.format(file))


def do_clean(number=0):
    """removes outdated archives"""
    local_clean(number)
    remote_clean(number)
