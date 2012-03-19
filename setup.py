from setuptools import setup, find_packages

name = "bit.recipe.android_sdk"
version = '0.0.2'
setup(
    name=name,
    version=version,
    author="Ryan Northey",
    author_email="ryan@3ca.org.uk",
    description="bit foundation android_sdk zc.buildout recipe",
    license="GPL",
    keywords="buildout",
    url='http://www.python.org/pypi/' + name,
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['bit', 'bit.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['zc.buildout', 'setuptools'],
    entry_points={'zc.buildout':
                    ['default=%s:Recipe' % name]},
    )
