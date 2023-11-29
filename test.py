import unittest
import pytest
import race_results


def code_that_raises_file_not_found_error():
    # Some code that should raise FileNotFoundError
    raise FileNotFoundError("File not found")


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        code_that_raises_file_not_found_error()



if __name__ == '__main__':
    unittest.main()
