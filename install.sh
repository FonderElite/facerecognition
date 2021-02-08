#!/bin/bash

if [ `whoami` != 'root' ]
  then
    echo "You must be root to do this."
    exit
fi
else
sudo apt-get install python3-pip
pip3 install requirements.txt
