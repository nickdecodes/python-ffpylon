#!/bin/bash

# python setup.py sdist bdist_wheel && echo "build package"

python -m build && echo "build package"

#python -m installer dist/*.whl

twine upload dist/* && echo "upload package"