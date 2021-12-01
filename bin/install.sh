#!/bin/sh
APP_DIR=`pwd`

if [ "`whoami`" != "root" ]; then
    echo "Require root privilege"
    exit 1
fi


cat <<EOF > /etc/systemd/system/fullpower-led.service
[Unit]
Description = Full Power LED

[Service]
WorkingDirectory = $APP_DIR
ExecStart = $APP_DIR/venv/bin/python app.py
User = $SUDO_USER
Type = simple

[Install]
WantedBy = multi-user.target
EOF
