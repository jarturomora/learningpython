try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project Skeleton',
    'author': 'Jose Arturo Mora Soto',
    'url': 'www.jams.name',
    'download_url': 'www.jams.name/projects',
    'author_email': 'emailme@jams.name',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME']
    'scripts': [],
    'name': 'projectname'
}

setup(**config)