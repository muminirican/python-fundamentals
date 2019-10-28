#!/usr/bin/env python3
"""Learn how to use tuples

Usage:

    python3 tuples.py
"""
# tuples are defined with (), are immutable
# t is the global scoped object for this module
t = ("Norway", 4.953, 3)


def loop(tpl):
    for item in tpl:
        print(item)
    print("length of the tuple is ", len(tpl))


print(__name__)


def main():
    loop(t)


if __name__ == "__main__":
    main()
elif __name__ == "tuples":
    pass
else:
    print("not called properly")

