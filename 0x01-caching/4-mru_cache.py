#!/usr/bin/python3
"""MRUCache Implementation"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class - a caching system with MRU eviction """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.mru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.mru_order.pop(-1)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.mru_order.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]
