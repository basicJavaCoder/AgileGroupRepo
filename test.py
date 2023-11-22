import pytest

with self.assertRaises(FileNotFoundError):
    print("FileNotFoundError detected")
