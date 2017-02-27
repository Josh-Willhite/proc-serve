#!/bin/bash

#Update package repos and install dependencies
apt-get update
dependencies=(git python3 python3-dev python3-setuptools)
for dep in "${dependencies[@]}"
do
    apt-get install -y $dep
done
