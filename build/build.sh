#!/bin/sh

echo "Running unit tests ..."
./run-unittests.sh
./run-pytest.sh
./run-nutter.sh