#!/usr/bin/env python3
""" Caching system """
from base_caching import baseCaching


class LIFOCache(BaseCaching):
    """LIFOcaching system"""
    def _init_(self):
        """Initializer"""
        super()._init_()

    def put(self, key, item):
        """Adds an item in cache"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print('DISCARD:'.self.last_item)
        if key:
            self.last_item = key

        def get(self, key):
            """Gets an item by key"""
            return self.cache_data.get(key)
