import os
from calc import add_numbers


def test_add_numbers():
    assert add_numbers(1, 2) == 3, "Should be 3"
