# encoding=utf-8

from vendor.hummingbird import *
import models.demo_model as demo_model


def main():
    if isinstance(hb_argv[1], str):
        file_path = hb_argv[1]
        data = hb_file.get(file_path)
        hb_file.put('foo.txt', data)

        demo_model.insert_data()
        demo_model.update_data()
        demo_model.delete_data()
        data = demo_model.get_data()


if __name__ == '__main__':
    main()
