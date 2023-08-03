#!/usr/bin/env python3
""" Basic caching system """
from base_caching import BasseCaching


class BasicCache(BaseCaching):
    """Dict caching system"""
    def put(self, key, item):
        """Puts item in cache"""
        if key is not None and item is not None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Gets item by key"""
        return self.cache_data.get(key)
