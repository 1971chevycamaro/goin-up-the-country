#!/bin/bash
sudo pigpiod
echo "updating..."
cd data/updater
python2 updater.py
cd ../../
echo "loading..."
python3 data/control.py
