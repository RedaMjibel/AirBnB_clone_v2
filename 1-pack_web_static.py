#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder.
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import task, local

@task
def do_pack():
    """
    making an archive and storing it in the folder versions
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create.failed:
        return None
    else:
        return archive
