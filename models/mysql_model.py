# encoding=utf-8

import vendor.hummingbird.hb_mysql as mysql


def get_data():
    sql = 'SELECT * FROM TAG_POOL WHERE id = %s;'
    args = [7010]
    data = mysql.select(sql, args)
    mysql.close()
    return data


def update_data():
    sql = 'UPDATE TAG_SWAMP SET word = %s WHERE id = %s;'
    args = ['Maro', 1]
    mysql.update(sql, args)
    mysql.close()


def insert_data():
    sql = 'INSERT INTO TAG_SWAMP (word) VALUES (%s)'
    args = [('Maro1'), ('Maro2'), ('Maro3')]
    mysql.insert(sql, args)
    mysql.close()


def delete_data():
    sql = 'DELETE FROM TAG_SWAMP WHERE id = %s'
    args = [1]
    mysql.delete(sql, args)
    mysql.close()