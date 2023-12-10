#!/usr/bin/python3
"""
Fabric script to distribute an archive to servers
"""

from fabric.api import put, run, env
from os.path import exists
import os 

env.hosts = ['100.26.163.17', '54.237.61.242']

def do_deploy(archive_path):
    """
    Deploy the archive of static files to the webservers.

    Arguments:
        archive_path: The path to the archive to distribute.

    Returns:
        True if all is okay, else False.
    """
    if exists(archive_path) is False:
        print(f"Archive not found: {archive_path}")
        return False

    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}/web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception as e:
        print(f"Deployment failed: {e}")
        success = False
    return success
