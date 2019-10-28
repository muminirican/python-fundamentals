"""Demonstrate Scoping"""

count = 0


def show_count():
    print("count = ", count)


def set_count(c):
    global count
    count = c
    print("count in function", id(count), count)


