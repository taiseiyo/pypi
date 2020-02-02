#!/usr/bin/env python3
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='package-name',
    version='1.0.0',
    description='explain package',
    long_description=long_description,
    url='https://github.com/takezyou/pydata',
    author='full name',
    author_email='kaitokun07@icloud.com',
    license='MIT',
    # 実際に動かす時に依存関係にあるライブラリをinstallしてくれる
    install_requires=['beautifulsoup4', 'lxml'],
    keywords='keyword',
    packages=find_packages(exclude=('tests')),
    # 今回コマンドを作ったのでconsole_scriptsを記述している
    entry_points={
        "console_scripts": [
            "pydata=pydata.__init__:main",
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
