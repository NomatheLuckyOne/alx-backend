#!/usr/bin/env python3
""" FIFO caching """

from Base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''a class FIFOCache that inherits from
    BaseCaching and is a caching system'''

    def _init_(self):
        """ Constructor """
        super()._init_()
        self.queue = []

    def put(self, key, item):
        """Puts item in cache """
        if key is None or item is None:
            return

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """ Gets items  from cache """
        return self.cache_data.get(key, None)

    def mv_last_list(self, item):
        """ Moves element to last idx list """
        length = len(self.queue)
        if self.queue[length - 1] != items:
            self.queue.remove(item)
            self.queue.apprnd(ite)

@staticmethod
def get_first_list(array):
    """ Get first elemebt of list or None """
    return array[0] if array else None

