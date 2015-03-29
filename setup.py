from setuptools import setup

__author__ = 'Masashi Shibata <contact@c-bata.link>'
__version__ = '0.0.0'

requires = []

setup(
    name='django-label-tag-attr',
    version=__version__,
    author=__author__,
    author_email='contact@c-bata.link',
    url='https://github.com/c-bata/django-label-tag-attr',
    description='Django library to alter css classes and html attributes.',
    packages=['label_tag_attr'],
    install_requires=['Django'],
)