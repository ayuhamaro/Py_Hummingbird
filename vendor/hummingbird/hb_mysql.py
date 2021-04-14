# encoding=utf-8

import pymysql
from vendor.hummingbird import hb_config


connection = pymysql.connect(host=hb_config.get('mysql', 'host'),
                             port=hb_config.get('mysql', 'port'),
                             user=hb_config.get('mysql', 'user'),
                             passwd=hb_config.get('mysql', 'password'),
                             db=hb_config.get('mysql', 'database'),
                             charset='utf8mb4',)


def select(query, args=[]):
    try:
        with connection.cursor() as cursor:
            if len(args) == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, args)

            data = cursor.fetchall()
            return data

    except pymysql.Error as e:
        print(e)


def update(query, args=[]):
    try:
        with connection.cursor() as cursor:
            if len(args) == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, args)

            connection.commit()
            return cursor.rowcount

    except pymysql.Error as e:
        print(e)


def insert(query, args=[]):
    batch_row = 100

    try:
        with connection.cursor() as cursor:
            if isinstance(args, list):
                if len(args) > batch_row:
                    data_list = []
                    for row in args:
                        data_list.append(row)
                        if len(data_list) == batch_row:
                            cursor.executemany(query, data_list)
                            connection.commit()
                            data_list = []

                    cursor.executemany(query, data_list)
                    connection.commit()

                elif len(args) > 0:
                    cursor.executemany(query, args)
                    connection.commit()

                else:
                    cursor.execute(query)
                    connection.commit()

            elif isinstance(args, tuple):
                if len(tuple) == 0:
                    cursor.execute(query)
                else:
                    cursor.execute(query, args)
                connection.commit()

            return cursor.lastrowid

    except pymysql.Error as e:
        print(e)


def delete(query, args=[]):
    try:
        with connection.cursor() as cursor:
            if len(args) == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, args)

            connection.commit()
            return cursor.rowcount

    except pymysql.Error as e:
        print(e)


def execute(query, args=[]):
    try:
        with connection.cursor() as cursor:
            if len(args) == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, args)

    except pymysql.Error as e:
        print(e)


def close():
    try:
        connection.close()

    except pymysql.Error as e:
        print(e)
