#!/bin/sh

autopep8 -i -r -v fpl
autoflake -i -r -v fpl
isort -v fpl
mypy fpl
pylint fpl

autopep8 -i -r -v tests
autoflake -i -r -v tests
isort -v tests
mypy tests
pylint tests
