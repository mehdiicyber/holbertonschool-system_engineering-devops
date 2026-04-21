#!/usr/bin/python3
from add_0 import add
from add_0 import sub
from add_0 import mul
from add_0 import div
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} - {} = {}".format(a, b, sub(a, b)))

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} * {} = {}".format(a, b, mul(a, b)))

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} / {} = {}".format(a, b, div(a, b)))
