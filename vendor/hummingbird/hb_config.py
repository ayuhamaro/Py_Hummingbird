# encoding=utf-8

from config import *


def get(module='', key=''):
    return eval(f'{module}.{module}[key]')
