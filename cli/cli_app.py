import sys
from calc import add_numbers, multiply_numbers

def main():
    operation = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    if operation == 'add':
        result = add_numbers(a, b)
    elif operation == 'multiply':
        result = multiply_numbers(a, b)
    else:
        print('Unsupported operation.')
        sys.exit(1)

    print(f'Result: {result}')

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python cli_app.py {add | multiply} <num1> <num2>')
        sys.exit(1)
    main()
