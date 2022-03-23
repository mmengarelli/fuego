#!/bin/sh

__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export DIST=../dist
export TEST=../test

echo "Clean up ..."

rm -rf $DIST

echo "Prepare environment ..."
# pip install --upgrade nutter
# pip install --upgrade pytest

echo "Running unit tests ..."
. ${__dir}/run-pytest.sh
. ${__dir}/run-nutter.sh


echo "Running integration tests ..."
. ${__dir}/run-integration-tests.sh

