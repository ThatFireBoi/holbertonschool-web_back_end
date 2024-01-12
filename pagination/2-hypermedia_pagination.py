#!/usr/bin/env python3
"""Implement a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10."""

import csv
from typing import List


def index_range(page, page_size):
    """Return a tuple of size two containing a start
    index and an end index corresponding to the range
    of indexes to return in a list for those particular
    pagination parameters."""
    if page and page_size:
        start_index = (page - 1) * page_size
        end_index = page * page_size
        return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a list of lists containing the data for the requested page."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return a dictionary containing the following key-value pairs"""
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) / page_size
        if len(self.dataset()) % page_size != 0:
            total_pages += 1
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': int(total_pages)
        }
