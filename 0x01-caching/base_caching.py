#!/usr/bin/python3
"""class base"""


class BaseCaching:
    """BaseCaching defines:
      - self.cache_data, a dictionary to store the cache data
    """

    def __init__(self):
        """Initialize the cache data"""
        self.cache_data = {}

    def print_cache(self):
        """Print the cache data"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")
