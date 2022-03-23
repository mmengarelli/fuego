#!/bin/sh

__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export DIST=../dist
export TEST=../test

echo "Running unit tests ..."

. ${__dir}/run-pytest.sh
. ${__dir}/run-nutter.sh