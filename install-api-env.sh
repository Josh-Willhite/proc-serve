#!/bin/bash
dependencies=(git python3 python3-dev python3-setuptools)
proc_serve_user="procserve"
install_dir="/opt"

#Update package repos and install dependencies
apt-get update
for dep in "${dependencies[@]}"
do
    apt-get install -y $dep
done

#Add procserve system user
useradd -r $proc_serve_user

#clone repo to opt
cd ${install_dir}
git clone https://github.com/Josh-Willhite/proc-serve.git

#install proc-serve
cd ${install_dir}/proc-serve
python3 setup.py install
chmod 755 src/proc_serve.py

#add link to executable
ln -sf /opt/proc-serve/src/proc_serve.py /usr/local/bin/procserve
