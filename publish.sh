#!/bin/bash

python setup.py sdist bdist_wheel && echo "build package"

twine upload dist/* && echo "upload package"