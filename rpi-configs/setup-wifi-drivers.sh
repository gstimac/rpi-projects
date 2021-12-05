#!/bin/bash

mkdir ~/wifi-drivers; cd ~/wifi-drivers;
wget http://downloads.fars-robotics.net/wifi-drivers/8188eu-drivers/8188eu-5.10.63-1459.tar.gz
tar -xzf 8188eu-5.10.63-1459.tar.gz
./install.sh
#reboot
