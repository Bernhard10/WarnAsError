from setuptools import setup, find_packages


setup(
    name='warnaserror',
    author='Bernhard Thiel',
    license="MIT",
    py_modules = ['warnaserror'],
    entry_points = {
        'nose.plugins.0.10': [
            'warnaserror = warnaserror:WarnAsError'
            ]
        },
    )
