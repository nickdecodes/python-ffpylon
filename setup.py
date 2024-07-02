#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : nickdecodes
@Email   : nickdecodes@163.com
@Usage   :
@FileName: setup.py
@DateTime: 2024/1/28 18:50
@SoftWare: 
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='mediakit',
    version='0.1',
    keywords=['mediakit', 'ffmpeg'],
    packages=find_packages(),
    package_data={"": ["LICENSE", "NOTICE"]},
    include_package_data=True,
    author="nickdecodes",
    author_email="nickdecodes@163.com",
    description="Media Kit Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    install_requires=[
    ],
    project_urls={
        "Documentation": "http://python-mediakit.readthedocs.io",
        "Source": "https://github.com/nickdecodes/python-mediakit",
    },
)
