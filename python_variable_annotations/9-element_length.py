#!/usr/bin/env python3
"""
A type-annotated function that takes input lst and returns
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing a string and an int
    """
    return [(i, len(i)) for i in lst]
