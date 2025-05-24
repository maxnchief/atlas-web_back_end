#!/usr/bin/env python3
"""
FIFOCache module
----------------
Implements a FIFO caching system using BaseCaching.
"""

BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """FIFO caching system with a limit defined by BaseCaching.MAX_ITEMS."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache using FIFO algorithm.
        If the cache exceeds MAX_ITEMS, discard the first item added.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # FIFO: remove the first inserted key
            first_key = next(iter(self.cache_data))
            print("DISCARD:", first_key)
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        Return None if key is None or not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]