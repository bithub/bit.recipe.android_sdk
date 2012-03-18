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
        sdk = pkg_resources.resource_filename(__name__, 'install_android_sdk')
        path = os.getcwd()
        if 'install_android_sdk' in os.listdir('bin'):
            os.unlink('bin/install_android_sdk')
        target_install_android_sdk = os.path.join('bin','install_android_sdk')
        open(target_install_android_sdk,'w').write('#/bin/bash\nAPIS=%s\n' %(apis)+open(install_android_sdk).read())
        commands.getoutput('chmod +x %s' %target_install_android_sdk)

    def install(self):
        self.logger.info("Setting up %s install_android_sdk" % install_android_sdk_type)
        self._update()
        commands.getoutput('./bin/install_android_sdk')
        return ['bin/install_android_sdk']

    def update(self):
        command = self.options.get('update-command')
        self._update()
        if command is not None:
            self.logger.info("Running %s" % command)

