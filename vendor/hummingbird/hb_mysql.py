# encoding=utf-8

import pymysql
from vendor.hummingbird import hb_config


connection = pymysql.connect(host=hb_config.get('mysql', 'host'),
                             port=hb_config.get('mysql', 'port'),
                             user=hb_config.get('mysql', 'user'),
                             passwd=hb_config.get('mysql', 'password'),
                             db=hb_config.get('mysql', 'database'),
                             charset='utf8mb4')


def select(query, args=[]):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            data = cursor.fetchall()
            return data
    except pymysql.Error as e:
        print(e)


def update(query, args=[]):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            connection.commit()
            return cursor.rowcount
    except pymysql.Error as e:
        print(e)


def insert(query, args=[]):
    try:
        with connection.cursor() as cursor:
            if len(args) > 1:
                cursor.executemany(query, args)
            else:
                cursor.execute(query, args)
            connection.commit()
            return cursor.lastrowid
    except pymysql.Error as e:
        print(e)


def delete(query, args=[]):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            connection.commit()
            return cursor.rowcount
    except pymysql.Error as e:
        print(e)


def execute(query, args=[]):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, args)
    except pymysql.Error as e:
        print(e)


def close():
    try:
        connection.close()
    except pymysql.Error as e:
        print(e)

