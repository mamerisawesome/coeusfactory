function runCoverage () {
    coverage run --source coeusfactory/ -m pytest tests &&
    coverage html &&
    open htmlcov/index.html &&

    rm assets/coverage.svg >/dev/null &&
    coverage-badge -o assets/coverage.svg
}

runCoverage
