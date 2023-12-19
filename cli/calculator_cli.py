import argparse
import calc


def main():
    parser = argparse.ArgumentParser(description='CLI Calculator')
    parser.add_argument('operation', choices=['add', 'multiply', 'average'],
                        help='Operation to perform: add, multiply, or average')
    parser.add_argument('values', type=float, nargs='+',
                        help='Numbers for the operation, separated by space.')

    args = parser.parse_args()

    if args.operation == 'add':
        result = calc.add_numbers(args.values[0], args.values[1])
    elif args.operation == 'multiply':
        result = calc.multiply_numbers(args.values[0], args.values[1])
    elif args.operation == 'average':
        if len(args.values) % 2 != 0:
            raise ValueError('The number of values for average must be even.')
        mid = len(args.values) // 2
        result = calc.calculate_average_of_two_lists(args.values[:mid], args.values[mid:])

    print(f'Result: {result}')


if __name__ == '__main__':
    main()
