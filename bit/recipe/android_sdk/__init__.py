import logging
import os
import pkg_resources
import commands


class Recipe:

    def __init__(self, buildout, name, options):
        self.options = options
        self.logger = logging.getLogger(name)
        self.name = name

    def _update(self):
        install = pkg_resources.resource_filename(
            __name__, 'install_android_sdk')
        path = os.getcwd()
        target_install = os.path.join(path, 'bin', self.name)
        part = os.path.join(path, 'parts', self.name)
        apis = self.options['apis']
        if os.path.exists(target_install):
            os.unlink(target_install)
        env_vars = {'BUILDOUT': path,
                    'SDK': self.options['sdk'],
                    'APIS': '( %s )' % ' '.join(apis),
                    'SDKDIR': part,
                    'PARTNAME': self.name,
                    }
        bash = '#!/bin/bash\n'
        bash += '\n'.join(['%s=%s' % (k, v)
                          for k, v in env_vars.items()])
        open(target_install, 'w').write(bash + open(install).read())
        commands.getoutput('chmod +x %s' % target_install)

    def _install(self):
        print commands.getoutput('./bin/%s install' % self.name)

    def install(self):
        self._update()
        self._install()
        return ['bin/%s' % self.name]

    def update(self):
        self._install()
        self._update()
