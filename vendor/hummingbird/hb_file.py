# encoding=utf-8

def file_get_contents(path):
    return open(path, 'r', encoding='utf-8').read()