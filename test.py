import pytest

def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        # Code that should raise FileNotFoundError
        print("FileNotFoundError detected")
