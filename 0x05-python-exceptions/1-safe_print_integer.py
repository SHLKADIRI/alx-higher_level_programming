#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integ
    Args:
        value (int): The int
    Returns:
        If a TypeError o
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
