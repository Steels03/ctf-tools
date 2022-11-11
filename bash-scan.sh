#!/bin/bash

if [[ "$1" == "-r" ]]
then
    net=$(echo $2 | cut -d . -f1-3)
    for i in {1..255}; do (ping -c 1 "$net".${i} | grep "bytes from" &); done
elif [[ "$1" == "-p" ]]
then
    for i in {1..65535}; do (echo > /dev/tcp/$2) >/dev/null 2>&1 && echo $i is open; done
else
    echo "Network scan : ./bash-scan.sh -r 192.168.1.0/24"
    echo "Port scan : ./bash-scan.sh -p 192.168."
fi
    