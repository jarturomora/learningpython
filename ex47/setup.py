try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project Exercise 47',
    'author': 'Jose Arturo Mora Soto',
    'url': 'www.jams.name',
    'download_url': 'https://github.com/jarturomora/learningpython',
    'author_email': 'emailme@jams.name',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47']
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
