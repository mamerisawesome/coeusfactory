function runCoverage () {
    coverage run --source coeusfactory/ -m pytest tests &&
    coverage html &&
    open htmlcov/index.html
    coverage-badge -o assets/coverage.svg
}

runCoverage
