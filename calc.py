def add_numbers(a: float, b: float) -> float:
    return a + b


def calculate_average_of_two_lists(numbers: list[float], numbers2: list[float]) -> float:
    if len(numbers) == 0 and len(numbers2) == 0:
        return 0
    elif len(numbers) == 0:
        return sum(numbers2) / len(numbers2)
    elif len(numbers2) == 0:
        return sum(numbers) / len(numbers)
    else:
        total = sum(numbers)
        first_average = total / len(numbers)

        total = sum(numbers2)
        second_average = total / len(numbers2)

        return (first_average + second_average) / 2
