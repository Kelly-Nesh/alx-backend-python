#!/usr/bin/env python3
"""duck type an iterable object"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    type-annotated function that takes an iterable of sequences
    and returns a list of tuples of the sequence and its length"""
    return [(i, len(i)) for i in lst]
