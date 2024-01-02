#!/usr/bin/env python3
"""Annotate the below function’s parameters and return values with the
appropriate types"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing elements and their lengths"""
    return [(i, len(i)) for i in lst]
