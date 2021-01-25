#! /bin/bash

pkill zoom &
python3 spam.py &
zoom-client &

echo "exit"