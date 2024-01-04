#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
    a = 10
    b = 5
    adding = add(a, b)
    print("{} + {} = {}".format(a, b , adding))
    subtraction = subtract(a, b)
    print("{} - {} = {}".format(a, b, subtraction))
    multipictation = multiply(a, b)
    print("{} * {} = {}".format(a, b, multiplication))
    division = divide(a, b)
    print("{} / {} = {}".format(a, b, division))
