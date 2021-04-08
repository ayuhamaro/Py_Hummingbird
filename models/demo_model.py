# encoding=utf-8

import vendor.hummingbird.hb_mysql as mysql


def get_data():
    sql = 'SELECT * FROM FOO WHERE id = %s;'
    args = [1]
    data = mysql.select(sql, args)
    mysql.close()
    return data


def update_data():
    sql = 'UPDATE FOO SET foo = %s WHERE id = %s;'
    args = ['Foo', 2]
    data = mysql.update(sql, args)
    mysql.close()
    return data


def insert_data():
    sql = 'INSERT INTO FOO (foo) VALUES (%s)'
    args = [('Foo1'), ('Foo2'), ('Foo3')]
    data = mysql.insert(sql, args)
    mysql.close()
    return data


def delete_data():
    sql = 'DELETE FROM FOO WHERE id = %s'
    args = [1]
    data = mysql.delete(sql, args)
    mysql.close()
    return data

