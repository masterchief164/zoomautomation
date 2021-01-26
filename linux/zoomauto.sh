#! /bin/bash

pkill zoom &
b='/linu.py'
k="${PWD}${b}"
python3 $k &
zoom-client &

echo "exit"
