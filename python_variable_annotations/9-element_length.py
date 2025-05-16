#!/usr/bin/env python3


from typing import Iterable, Sequence, List, Tuple


def element_length(Lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing the elements of the input list and their respective lengths."""
    return [(i, len(i)) for i in Lst]
