#!/usr/bin/python3
"""
 a Fabric script (based on the filee 2-do_deploy_web_static.py)
 that creates and distributes an archive to your web
 servers, using the function deploy:
"""

import os

from fabric.api import *

from datetime import datetime

env.hosts = ['52.91.137.7', '100.25.33.74']

def do_pack():
    """Creating the archive from the web_static's directory"""
    local("mkdir -p versions")
    filee = 'versions/web_static_{}.tgz'\
        .format(datetime.strftime(datetime.now(), "%Y%m%d%I%M%S"))
    compr = 'tar -cvzf {} web_static'.format(filee)
    tarr_filee = local(compr)
    if tarr_filee.failed:
        return None
    else:
        return filee


def do_deploy(archive_path):
    """Deploys an archive"""
    if not os.path.exists(archive_path):
        return False
    archv = archive_path.split('/')[1]
    namee = archv.split('.')[0]
    tarr_filee = put(archive_path, '/tmp/{}'.format(archv))
    if tarr_filee.failed:
        return False
    tarr_filee = run('mkdir -p /data/web_static/releases/{}'.format(namee))
    if tarr_filee.failed:
        return False
    tarr_filee = run(
        'tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        .format(archv, namee))
    if tarr_filee.failed:
        return False
    tarr_filee = run('rm /tmp/{}'.format(archv))
    if tarr_filee.failed:
        return False
    compr = 'mv /data/web_static/releases/{0}/web_static/*'
    compr += ' /data/web_static/releases/{0}/'
    tarr_filee = run(compr.format(namee))
    if tarr_filee.failed:
        return False
    tarr_filee = run(
                'rm -rf /data/web_static/releases/{}/web_static'
                .format(namee))
    if tarr_filee.failed:
        return False
    tarr_filee = run('rm -rf /data/web_static/current')
    if tarr_filee.failed:
        return False
    tarr_filee = run(
            'ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(namee))
    if tarr_filee.failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    """ Based on 2-do_deploy_web_static.py it creates and then
    distributes an archive just to your own web servers,
    using this function called deploy"""
    archive = do_pack()
    if archive is None:
        return False
    tarr_filee = do_deploy(archive)
    return tarr_filee
