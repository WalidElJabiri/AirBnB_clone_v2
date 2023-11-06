#!/usr/bin/python3
"""
Fscript that generates a .tgz
"""
from os import makedirs
from datetime import datetime
from fabric.api import local


def do_pack():
    """ generates the archive. """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(timestamp)

    try:
        makedirs("./versions", exist_ok=True)
        local('tar -cvzf {} web_static'.format(file_path))
        return file_path

    except:
        return None
