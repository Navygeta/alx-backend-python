#!/usr/bin/env python3
"""Using mypy to validate code"""
from typing import Tuple, Iterable, List, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
