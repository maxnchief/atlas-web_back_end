#!/usr/bin/env python3
"""
LRUCache module
---------------
Implements a LRU caching system using BaseCaching.
"""

BaseCaching = __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    """LRU caching system with a limit defined by BaseCaching.MAX_ITEMS."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item in the cache using LRU algorithm.
        If the cache exceeds MAX_ITEMS, discard the least recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update usage order: move key to end (most recently used)
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove least recently used key
            lru_key = self.usage_order.pop(0)
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]

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
