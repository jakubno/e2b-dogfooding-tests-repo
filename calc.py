def add_two_numbers(a, b):
    return a + b

# Example usage
if __name__ == '__main__':
    number1 = float(input('Enter first number: '))
    number2 = float(input('Enter second number: '))
    result = add_two_numbers(number1, number2)
    print(f'The sum of {number1} and {number2} is {result}')
