from setuptools import setup

setup(
    name='lrank',
    version='1.0',
    packages=['lrank'],
    entry_points={
        'console_scripts': [
            'lrank = lrank.__main__:main'
        ]
    }, install_requires=['docopt'])
