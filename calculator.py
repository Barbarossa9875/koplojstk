#!/usr/bin/env python3

"""Simple command-line calculator"""

import sys

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else float('inf'),
}

def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("Usage: calculator.py <number1> <operator> <number2>")
        print("Operators: +, -, *, /")
        return 1

    _, num1_str, operator, num2_str = argv
    if operator not in OPERATORS:
        print(f"Unsupported operator: {operator}")
        return 1

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("Both operands must be numbers.")
        return 1

    result = OPERATORS[operator](num1, num2)
    if result == float('inf'):
        print("Error: Division by zero")
        return 1

    if result.is_integer():
        result = int(result)
    print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

