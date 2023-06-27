# UNIT TEST DEMO

Run the following command to run test cases
```shell
pytest
# or
pytest -v
# -v means verbose
```

## Changing standard (Python) test discovery
Changing naming conventions
```ini
# content of pytest.ini
# Example 1: have pytest look for "check" instead of "test"
[pytest]
python_files = check_*.py
python_classes = Check
python_functions = *_check
```

## Marking test functions and selecting them for run
You can mark a test function with custom metadata
```python
from pytest import mark

@mark.webtest
def test_send_http():
    pass
```

You can then restrict a test run to only run tests marked with `webtest`:
```shell
pytest -m webtest
# -m means mark
# or
pytest -m "not webtest" # all tests except webtest ones
```
You can register custom marks in `pytest.ini` file like this:
```ini
[pytest]
markers = 
    slow: marks tests as slow
    serial
```

To see available markers type: `pytest --markers`

## Pytest Fixtures