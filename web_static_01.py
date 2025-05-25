#!/usr/bin/python3
"""
Function that compresses the web_static folder
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Compress web_static folder into .tgz archive"""
    try:
        if not os.path.exists("versions"):
            local("mkdir -p versions")
        t = datetime.now()
        archive_name = "web_static_{}.tgz".format(t.strftime("%Y%m%d%H%M%S"))
        archive_path = "versions/{}".format(archive_name)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None
