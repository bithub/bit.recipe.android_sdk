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
        for dk in ['sdk', 'ndk']:
            install = pkg_resources.resource_filename(__name__, 'install_android_%s' %dk)
            path = os.getcwd()
            if 'install_android_%s' %dk in os.listdir('bin'):
                os.unlink('bin/install_android_%s' %dk)
            target_install = os.path.join('bin','install_android_%s' %dk)
            open(target_install,'w').write('#/bin/bash\nDK=%s\nAPIS=%s\n' %(self.options[dk],tuple(apis))+open(install).read())
            commands.getoutput('chmod +x %s' %target_install)
        open(os.path.join('bin', 'android_sdk'),'w').write('BUILDOUT=`pwd`\nexport ANDROIDAPI=8\nexport ANDROIDSDK=$BUILDOUT/parts/android-sdk\nexport PATH=$ANDROIDSDK:$PATH') 
        open(os.path.join('bin', 'android_ndk'),'w').write('BUILDOUT=`pwd`\nexport ANDROIDNDKVER=r7\nexport ANDROIDNDK=$BUILDOUT/parts/android-ndk\nexport PATH=$ANDROIDNDK:$PATH') 

    def install(self):
        install_android_sdk = pkg_resources.resource_filename(__name__, 'install_android_sdk')
        self.logger.info("Setting up %s" % install_android_sdk)
        self._update()
        return ['bin/install_android_sdk', 'bin/install_android_ndk']

    def update(self):
        self._update()
