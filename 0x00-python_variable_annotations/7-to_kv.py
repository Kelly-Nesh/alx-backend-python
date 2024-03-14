#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """type-annotated function that takes a string and an int/float
    returns a tuple of the string and the int/float."""
    return (k, v**2)
