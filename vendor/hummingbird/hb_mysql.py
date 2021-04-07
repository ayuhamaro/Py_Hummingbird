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


def select(query, args=[]):
    cursor.execute(query, args)
    data = cursor.fetchall()
    return data


def update(query, args=[]):
    cursor.execute(query, args)
    db.commit()


def insert(query, args=[]):
    if len(args) > 1:
        cursor.executemany(query, args)
    else:
        cursor.execute(query, args)
    db.commit()


def delete(query, args=[]):
    cursor.execute(query, args)
    db.commit()


def execute(query, args=[]):
    cursor.execute(query, args)


def close():
    db.close()

