try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

package_data = {
        'status_cats': [ 'templates/status_cats/*.html' ],
}

setup(
  name = 'django-status-cats',
  packages = ['status_cats'],
  version = '0.1',
  package_data = package_data,
  description = 'Django middleware for adding HTTP status cats to your responses ',
  author = 'Andromeda Yelton',
  author_email = 'andromeda.yelton@gmail.com',
  url = 'https://github.com/thatandromeda/django-status-cats',
  download_url = 'https://github.com/thatandromeda/django-status-cats/tarball/0.1',
  license = 'CC0',
  classifiers = [
    'Framework :: Django',
    'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    'Intended Audience :: Developers',
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Programming Language :: Python',
    ],
)
