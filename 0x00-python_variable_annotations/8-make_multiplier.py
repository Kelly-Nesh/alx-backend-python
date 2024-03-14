#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type-annotated function that takes a float multiplier as argument
    and returns a function that multiplies a float by the multiplier"""
    def callable(arg: float):
        return arg * multiplier
    return callable
