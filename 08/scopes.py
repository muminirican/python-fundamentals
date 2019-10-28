"""Demonstrate Scoping"""

count = 0


def show_count():
    print("count = ", count)


def set_count(c):
    global count
    count = c
    print("count in function", id(count), count)


# sys.path.extend(['D:\\Pluralsight\\python-fundamentals\\08'])

# sys.path.extend([r'D:\Pluralsight\python-fundamentals\04\demos\demos\after'])

