import pytest
from Code_Base import runners_data, read_integer_between_numbers


def code_that_raises_file_not_found_error():
    # Some code that should raise FileNotFoundError
    runners_data()
    raise FileNotFoundError("File not found")


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        code_that_raises_file_not_found_error()


def code_that_raises_Index_Error():
    read_integer_between_numbers("Input:", 1, 12)
    raise IndexError("Index Out of Bounds")

def test_List_out_Of_bounds():
    with pytest.raises(IndexError)
        code_that_raises_Index_Error()