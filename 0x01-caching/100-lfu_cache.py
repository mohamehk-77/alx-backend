#!/usr/bin/python3
"""LFUCache Implementation"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class - a caching system with LFU eviction """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.usage_freq = {}  # Dictionary to store frequency of each key
        self.usage_order = {}  # Dictionary to store the order of usage
        self.current_order = 0

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and increment the frequency and order
            self.cache_data[key] = item
            self.usage_freq[key] += 1
            self.usage_order[key] = self.current_order
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item
                lfu_key = min(self.usage_freq, key=lambda k: (
                    self.usage_freq[k], self.usage_order[k]))
                del self.cache_data[lfu_key]
                del self.usage_freq[lfu_key]
                del self.usage_order[lfu_key]
                print(f"DISCARD: {lfu_key}")

            # Add new item and initialize its frequency and order
            self.cache_data[key] = item
            self.usage_freq[key] = 1
            self.usage_order[key] = self.current_order

        # Update current order
        self.current_order += 1

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Increment the frequency and update the order
        self.usage_freq[key] += 1
        self.usage_order[key] = self.current_order
        self.current_order += 1

        return self.cache_data[key]
