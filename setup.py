import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()


setup(
    name='spaegg',
    version='0.1.0',
    description='HTTP Server to serve Simple Page Application',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Hiroki KIYOHARA',
    author_email='hirokiky@gmail.com',
    url='https://github.com/hirokiky/spaegg',
    license='MIT',
    packages=['spaegg'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'spaegg = spaegg.commands:run',
        ]
    }
)
