# encoding=utf-8

import sys


def get(index):
    if index > len(sys.argv) - 1:
        return False
    else:
        return sys.argv[index]


