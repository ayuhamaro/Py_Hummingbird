# encoding=utf-8

import vendor.hummingbird.hb_mysql as mysql


def get_data():
    data = mysql.select('SELECT * FROM TAG_POOL')
    mysql.close()
    return data
