# encoding=utf-8

def get(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except IOError as e:
        print(e)


def put(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            return f.write(content)
    except IOError as e:
        print(e)


def put_print(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            print(content, file=f)
    except IOError as e:
        print(e)

