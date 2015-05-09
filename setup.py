import os
from setuptools import setup

__author__ = 'Masashi Shibata <contact@c-bata.link>'
__version__ = '1.0.2'

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(BASE_PATH, 'README.rst')).read()
CHANGES = open(os.path.join(BASE_PATH, 'CHANGES.rst')).read()

requires = []

setup(
    name='django-label-tag-attr',
    version=__version__,
    author=__author__,
    author_email='contact@c-bata.link',
    url='https://github.com/c-bata/django-label-tag-attr',
    description="Add css classes and html tag attributes "
                "to django form's label.",
    long_description=README + '\n\n' + CHANGES,
    packages=['label_tag_attr'],
    install_requires=['Django'],
    keywords=['django', 'form', 'label', 'label_tag_attr'],
    license='MIT License',
    include_package_data=True,
)
