#!/usr/bin/python3
"""cache base"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class - a simple caching system with no limit """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
