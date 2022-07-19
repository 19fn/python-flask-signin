#!/bin/bash

if [ $(id -u) -ne 0 ]; then
	echo;echo "[!] You must run this script as root (sudo $0).";echo
else
	sudo docker build . --tag "signin:v1.0" && \
	sudo docker-compose up --detach
	echo
	echo -ne "[!] 'Initialize.sh' is still finishing wait...  (10%)\r"
    sleep 1
    echo -ne "[!] 'Initialize.sh' is still finishing wait...  (28%)\r"
    sleep 1
	echo -ne "[!] 'Initialize.sh' is still finishing wait...  (45%)\r"
	sleep 1
	echo -ne "[!] 'Initialize.sh' is still finishing wait...  (78%)\r"
	sleep 1
	echo -ne "[!] 'Initialize.sh' is still finishing wait...  (100%)\r"
	echo -n ""
    echo;echo;echo "[+] "$0" has terminated successfully.";echo
fi