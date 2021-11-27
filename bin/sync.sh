#!/bin/bash

REMOTE_TARGET=$1

rsync -av --delete \
    --exclude=__pycache__ \
    --exclude=README.md \
    --exclude=develop-requirements.txt \
    --exclude=bin \
    --exclude=tests \
    --exclude=venv \
    --exclude=tmp \
    --exclude=.* \
    --exclude=*.egg-info \
    --exclude=*.pyc \
    ./ $REMOTE_TARGET
