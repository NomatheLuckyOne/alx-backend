#!/usr/bin/env python3

""" Basic dictionary """

from  base_caching import  BasseCaching


class BasicCache(BaseCaching):
    '''a class BasicCache that inherits from 
    BaseCaching and is a caching syatem'''

    def put(self, key, item):
        """Puts item in cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get (self, key):
        """Gets item from cache"""
        return self.cache_data.get(key, None)
