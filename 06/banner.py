#!/usr/bin/env python3
"""Create a banner for any string.

Usage:

    python3 banner.py string
"""

import sys


def banner(message, border='-'):
    """Print a banner.

    Args:
        message: Input from the user as string to be displayed.
        border: Input form the user, border char, default -

    Returns:
        None, but prints the string.
    """
    line = border * len(message)
    print(line)
    print(message)
    print(line)


print(__name__)


def main(message, border='-'):
    banner(message, border)


if __name__ == '__main__':
    main(sys.argv[1])
# todo: modify code to accept two parameteres from the command line