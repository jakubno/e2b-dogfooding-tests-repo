def add_numbers(a: float, b: float) -> float:
    return a + b


def calculate_average_of_two_lists(numbers: list[float], numbers2: list[float]) -> float:
    if len(numbers) == 0:
        first_average = 0
    else:
        total = sum(numbers)
        first_average = total / len(numbers)

    if len(numbers2) == 0:
        second_average = 0
    else:
        total = sum(numbers2)
        second_average = total / len(numbers2)

    return (first_average + second_average) / 2


def multiply_numbers(a: float, b: float) -> float:
    return a * b
