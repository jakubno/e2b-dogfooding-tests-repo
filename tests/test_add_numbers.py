from calc import add_numbers, multiply_numbers


def test_add_numbers():
    assert add_numbers(1, 2) == 3, "Should be 3"


def test_multiply_numbers():
    assert multiply_numbers(13, 7) == 91, "Should be 91"
