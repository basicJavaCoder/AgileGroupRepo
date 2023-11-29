import unittest
import pytest


def code_that_raises_file_not_found_error():
    # Some code that should raise FileNotFoundError
    raise FileNotFoundError("File not found")


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        code_that_raises_file_not_found_error()
