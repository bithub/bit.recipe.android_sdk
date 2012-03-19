import logging
import os
import shutil
import pkg_resources
import commands

class Recipe:
    def __init__(self, buildout, name, options):
        self.options = options
        self.logger = logging.getLogger(name)

    def _update(self):
        apis = self.options['apis'].split('\n')        
        install = pkg_resources.resource_filename(__name__, 'install_android_sdk')
        path = os.getcwd()
        target_install = os.path.join(path,'bin','install_android_sdk')
        if os.path.exists(target_install)
            os.unlink(target_install)
        open(target_install,'w').write('#/bin/bash\nDK=%s\nAPIS=%s\n' %(self.options[dk],tuple(apis))+open(install).read())
        commands.getoutput('chmod +x %s' %target_install)
        open(os.path.join('bin', 'android_sdk'),'w').write('BUILDOUT=`pwd`\nexport ANDROIDAPI=8\nexport ANDROIDSDK=$BUILDOUT/parts/android-sdk\nexport PATH=$ANDROIDSDK:$PATH') 

    def install(self):
        self._update()
        return ['bin/install_android_sdk',]

    def update(self):
        self._update()
