#!/usr/bin/python3
"""LRUCache Implementation"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class - a caching system with LRU eviction """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]
