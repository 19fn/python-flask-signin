#!/bin/bash

if [ $(id -u) -ne 0 ]; then
	echo;echo "[!] You should run this script as root (sudo $0).";echo
else
	sudo docker build . --tag "signin:v2.0" && \
		sudo docker-compose up --detach && \
    		echo;echo "[+] "$0" has terminated successfully.";echo
fi

