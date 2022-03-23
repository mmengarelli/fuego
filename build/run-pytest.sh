echo "Running pytest tests ..."

py.test --junitxml $DIST/pytest-results.xml  $TEST/pytest
