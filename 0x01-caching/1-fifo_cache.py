#!/usr/bin/env python3
""" FIFO caching system """
from Base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching class """
    def _init_(self):
        """ Constructor """
        super()._init_()

    def put(self, key, item):
        """ Assigns the item value of the key """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = sorted(self.cache_data[0]
                    self.cache_data.pop(discarded_key)
                    print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """ Puts an item by key """
        return self.cache_data.get(key)
