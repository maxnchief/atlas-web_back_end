BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """Basic caching system with no limit."""

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value for the key key."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data:
            return None  
        return self.cache_data[key]
        