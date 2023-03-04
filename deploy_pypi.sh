#!/usr/local/bin/bash

python3 setup.py bdist_wheel sdist
pip install .
python3 run.py
twine check dist/* 
twine upload dist/*
