#!/bin/bash

echo "Running the python script for setup."
python3 setup.py

echo "Running the deploy script to enable passwordless SSH on the remote servers."
bash deploy.sh
