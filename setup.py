from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'VERSION')) as f:
    VERSION = f.read().strip()


setup(
    name='py3-wkhtmltopdf',
    version=VERSION,
    description='Simple Python 3 wrapper for wkhtmltopdf',
    long_description="%s\n\n%s" % (open('README.md', 'r').read(), open('AUTHORS.md', 'r').read()),
    author='Jonathan Tsai',
    author_email='hello@jontsai.com',
    license='BSD',
    url='http://github.com/jontsai/python3-wkhtmltopdf',
    packages=find_packages(),
    dependency_links=[],
    install_requires=[],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
