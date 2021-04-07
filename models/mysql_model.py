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
    args = ['Maro', 2]
    data = mysql.update(sql, args)
    mysql.close()
    return data


def insert_data():
    sql = 'INSERT INTO TAG_SWAMP (word) VALUES (%s)'
    args = [('Maro11'), ('Maro12'), ('Maro13')]
    data = mysql.insert(sql, args)
    mysql.close()
    return data


def delete_data():
    sql = 'DELETE FROM TAG_SWAMP WHERE id = %s'
    args = [5]
    data = mysql.delete(sql, args)
    mysql.close()
    return data

