echo "Running unittest tests ..."

py.test --junitxml $DIST/results.xml  $TEST//unittest
