#!/usr/bin/env python3
def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of (start_index, end_index) for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
