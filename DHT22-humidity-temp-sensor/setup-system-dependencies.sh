#!/bin/bash
sudo apt update -y 
sudo apt upgrade -y
sudo apt install python3-dev python3-pip -y
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install pigpio
