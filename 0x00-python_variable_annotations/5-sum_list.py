#!/usr/bin/env python3
"""Complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """type-annotated function that takes a list of floats
    returns their sum as a float."""
    return sum(input_list)
