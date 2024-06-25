#!/usr/bin/env python3
"""simpil pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """function that returns a tuple of size two"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
