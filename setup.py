from setuptools import setup


setup(
    name='warnaserror',
    author='Bernhard Thiel',
    license="MIT",
    py_modules = ['warnaserror'],
    version = '0.01',
    entry_points = {
        'nose.plugins.0.10': [
            'warnaserror = warnaserror:WarnAsError'
            ]
        },
    )
