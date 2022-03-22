#!/bin/sh

__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Running unit tests ..."

. ${__dir}/run-unittests.sh
. ${__dir}/run-pytest.sh
. ${__dir}/run-nutter.sh

