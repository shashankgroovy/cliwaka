from setuptools import setup, find_packages
from codecs import open
from os import path

current_dir = path.abspath(path.dirname(__file__))
with open(path.join(current_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cliwaka',
    version='0.1.1',
    description='Cliwaka is an interactive command line utility for wakatime.com',
    long_description=long_description,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],

    author='Shashank Srivastav',
    author_email='shashankgrovy@gmail.com',

    license='GPLv3',
    keywords='wakatime cli tool',
    url='https://github.com/shashankgroovy/cliwaka',
    download_url='https://github.com/shashankgroovy/cliwaka/archive/master.zip',

    packages=find_packages(),
    install_requires=[
        'requests',
        'argparse'
    ],

    entry_points={
        'console_scripts': [
            'cliwaka=cliwaka.__main__:main',
        ],
    },
)
