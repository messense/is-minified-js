import os.path

from ._native import lib, ffi

__all__ = ['is_likely_minified', ]


def is_likely_minified(path):
    if not os.path.exists(path):
        return False
    return bool(lib.is_likely_minified(path.encode('utf-8')))
