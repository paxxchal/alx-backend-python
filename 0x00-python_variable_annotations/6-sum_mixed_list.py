#!/usr/bin/env python3
"""
This module contains a type-annotated function
for summing a list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats.

    :param mxd_lst: List of integers and floats
    :return: The sum of the list as a float
    """
    return sum(mxd_lst)
