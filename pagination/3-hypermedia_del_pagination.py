#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion-resilient hypermedia pagination.
        Returns a dictionary with index, next_index, page_size, and data.
        """
        assert index is None or (
            isinstance(index, int) and 0 <= index < len(self.dataset())
        )
        indexed_data = self.indexed_dataset()
        data = []
        current = index if index is not None else 0
        collected = 0
        max_index = max(indexed_data.keys())
        # Collect page_size items, skipping missing indices
        while collected < page_size and current <= max_index:
            if current in indexed_data:
                data.append(indexed_data[current])
                collected += 1
            current += 1
        next_index = current
        return {
            "index": index if index is not None else 0,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
