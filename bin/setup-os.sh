#!/bin/sh

if [ "`whoami`" != "root" ]; then
    echo "Require root privilege"
    exit 1
fi

apt update -y
apt install python3-venv -y
