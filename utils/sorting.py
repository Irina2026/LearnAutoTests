from itertools import pairwise


def is_sorted_ascending(prices):
    return all(a <= b for a, b in pairwise(prices))


def is_sorted_descending(prices):
    return all(a >= b for a, b in pairwise(prices))
