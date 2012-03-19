import logging
import os
import shutil
import pkg_resources
import commands

class Recipe:
    def __init__(self, buildout, name, options):
        self.options = options
        self.logger = logging.getLogger(name)
        self.name = name

    def _update(self):
        install = pkg_resources.resource_filename(__name__, 'install_android_sdk')
        path = os.getcwd()
        target_install = os.path.join(path,'bin','install_android_sdk')
        part = os.path.join(path,'parts',self.name)
        if os.path.exists(target_install)
            os.unlink(target_install)
        open(target_install,'w').write('#/bin/bash\nSDK=%s\nAPIS=%s\n' %(self.options['sdk'],tuple(apis))+open(install).read())
        commands.getoutput('chmod +x %s' %target_install)
        open(os.path.join('bin', 'android_sdk'),'w').write('BUILDOUT=%s\nexport ANDROIDAPI=%s\nexport ANDROIDSDK=%s\nexport PATH=$ANDROIDSDK:$PATH'%(path,apis[0],part) 

    def install(self):
        self._update()
        return ['bin/%s'self.name,]

    def update(self):
        self._update()
