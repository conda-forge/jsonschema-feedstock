from pathlib import Path
import os
import sys

import pytest
import jsonschema

HERE = Path(__file__).parent
TESTS = Path(jsonschema.__file__).parent / "tests"

os.environ.update(JSON_SCHEMA_TEST_SUITE=str(HERE / "json"))

PYTEST_ARGS = [
    "-vv",
    "--cov=jsonschema",
    "--cov-report=term-missing:skip-covered",
    "--no-cov-on-fail",
    *sys.argv[1:],
    *TESTS.rglob("test_*.py")
]

print("PYTEST_ARGS", *PYTEST_ARGS)

sys.exit(pytest.main(PYTEST_ARGS))
