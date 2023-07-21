#!/usr/bin/env python 3
"""Implement a method named get_page that takes two integer
arguments page with default value 1 and page_size with defaul value 10
"""
import csv
from typing import List, Tuple


def index_range(page: int page_size: int) -> Tuple[int, int]:
    '''Retrieves the index range from a given page size
    '''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    '''Server class to paginate a database of popular baby names
    '''
    DATA_FILE = "Popular_Baby_Name.csv"


def _init_(self):
    '''Initializes a new Server instance
    '''
    self._dataset = None


def dataset(self) -> List[List]:
    '''Cached dataset
    '''
    if self.dataset is None:
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            dataset = [row for row in reader]
        self._dataset = dataset[1:]

    return self._dataset


def get_page(self, page: int = 1, page_size: int = 10) -> List[list]:
    '''Retrieves a page of data
    '''
    assert type(page) == int and type(page_size) == int
    assert page > 0 and page_size > 0
    start, end = index_range(page, page_size)
    data = self.dataset()
    if start > len(data):
        return []
    return data[start:end]
