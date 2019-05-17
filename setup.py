# coding:utf-8
from setuptools import (setup, find_packages)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="shadowsocksr-tools",
    version="1.3.0",
    packages=find_packages(),

    # metadata for upload to PyPI
    author="Vision Network",
    author_email="michael@vision.network",
    description="Python Shadowsocksr tools.",
    keywords='Proxy, Shadowsocks, Shadowsocksr, IP, GEO_IP',

    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/voken100g/python-shadowsocksr-tools.git",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests-cache',
        'ip-query',
        'qwert',
        'cli-print',
        'proxy-fn',
        'common-patterns',
    ],
)
