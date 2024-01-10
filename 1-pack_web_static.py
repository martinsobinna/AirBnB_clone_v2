#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB
Clone repo, using the function do_pack
"""

from fabric.api import local

from datetime import datetime

def do_pack():
    """Creating the archive from the web_static directory"""
    local("mkdir -p versions")
    filee = 'versions/web_static_{}.tgz'\
        .format(datetime.strftime(datetime.now(), "%Y%m%d%I%M%S"))
    compr = 'tar -cvzf {} web_static'.format(filee)
    tarr_filee = local(compr)
    if tarr_filee.failed:
        return None
    return filee
