#!/usr/bin/env python3
import argparse
import sys
from calc import add_numbers, multiply_numbers


def main():
    parser = argparse.ArgumentParser(description='Calculator CLI app utilizing calc.py functions.')
    parser.add_argument('operation', choices=['add', 'multiply'], help='The operation to perform')
    parser.add_argument('a', type=float, help='First operand')
    parser.add_argument('b', type=float, help='Second operand')

    args = parser.parse_args()

    if args.operation == 'add':
        result = add_numbers(args.a, args.b)
    elif args.operation == 'multiply':
        result = multiply_numbers(args.a, args.b)

    print(f'Result: {result}')

if __name__ == '__main__':
    sys.exit(main())
