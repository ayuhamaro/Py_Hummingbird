# encoding=utf-8

import pymysql
from vendor.hummingbird import hb_config

db = pymysql.connect(host=hb_config.get('mysql', 'host'),
                     port=3306,
                     user=hb_config.get('mysql', 'user'),
                     passwd=hb_config.get('mysql', 'password'),
                     db=hb_config.get('mysql', 'database'),
                     charset='utf8')

cursor = db.cursor()


def select(sql):
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def update(sql):
    cursor.execute(sql)
    db.commit()


def close():
    db.close()