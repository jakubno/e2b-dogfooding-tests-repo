from calc import calculate_average_of_two_lists


def test_calculate_average_of_two_lists():
    avg = calculate_average_of_two_lists([1, 2, 3], [])
    assert avg == 2, f"Expected 2, got {avg}"

    avg = calculate_average_of_two_lists([1, 2, 3], [4, 5, 6])
    assert avg == 3.5, f"Expected 3.5, got {avg}"
