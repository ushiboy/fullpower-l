#!/bin/sh

if [ "`whoami`" != "root" ]; then
    echo "Require root privilege"
    exit 1
fi

systemctl enable fullpower-led.service
raspi-config nonint do_overlayfs 0
