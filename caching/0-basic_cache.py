#!/usr/bin/env python3

"""
BasicCache module
-----------------
Implements a basic caching system with no limit using BaseCaching.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic caching system with no limit."""

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key.
        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or not found, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
