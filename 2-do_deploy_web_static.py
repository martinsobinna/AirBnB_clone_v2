#!/usr/bin/python3
"""
Wrote a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy:
"""

import os

from fabric.api import env

from fabric.api import put, run

env.hosts = ['52.91.137.7', '100.25.33.74']


def do_deploy(archive_path):
    """
    It help distributes an archive just to your weeb servers
    """
    if os.path.exists(archive_path) is False:
        return(False)
    try:
        put(archive_path, '/tmp/')
        _file_name = archive_path.split("/")[-1]
        file_name = _file_name.split(".")[0]

        run('mkdir -p /data/web_static/releases/{}'.format(file_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format
            (_file_name, file_name))
        run('rm /tmp/{}'.format(_file_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(file_name, file_name))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(file_name))
        return(True)
    except:
        return(False)
