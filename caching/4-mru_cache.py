#!/usr/bin/env python3
"""
MRUCache module
---------------
Implements a MRU caching system using BaseCaching.
"""

BaseCaching = __import__('base_caching').BaseCaching

class MRUCache(BaseCaching):
    """MRU caching system with a limit defined by BaseCaching.MAX_ITEMS."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item in the cache using MRU algorithm.
        If the cache exceeds MAX_ITEMS, discard the most recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update usage order: move key to end (most recently used)
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove most recently used key
            mru_key = self.usage_order.pop()
            print("DISCARD:", mru_key)
            del self.cache_data[mru_key]

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """
        Get an item by key.
        Return None if key is None or not found.
        """
        if key is None or key not in self.cache_data:
            return None
        # Update usage order: move key to end (most recently used)
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]