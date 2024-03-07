#!/usr/bin/python3
""" generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo,
 using the function do_pack"""


from fabric.api import *
from datetime import datetime


def do_pack():
    """ Fabric script that generates a .tgz archive from contents of
    web_static folder """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None