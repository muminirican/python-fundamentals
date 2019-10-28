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

# a, b = b, a is the idiomatic Python swap

# "".join(["high", "way", "man"]) will produce "highwayman", another cool python property

# "yaşım {kek[0]}, adım {kek[1]} , arkadaşımın adı {kek[2][0]}, yaşı {kek[2][1]}".format(kek = kek)
# 'yaşım 123, adım ksdk , arkadaşımın adı hj, yaşı 23'