import sqlite3 as sq


class Database(object):

    def __init__(self, path):
        self.connection = sq.connect(path)
        self.connection.execute('pragma foreign_keys = on')
        self.connection.commit()
        self.cur = self.connection.cursor()

    def create_tables(self):
        self.query(
            'CREATE TABLE IF NOT EXISTS products (idx text, title text, body text, photo blob, price int, tag text)')
        self.query('CREATE TABLE IF NOT EXISTS orders (cid int, usr_name text, usr_address text, phone_number text,'
                   ' products text)')
        self.query('CREATE TABLE IF NOT EXISTS categories (idx text, title text)')
        self.query('CREATE TABLE IF NOT EXISTS cart (cid int, idx text, quantity int, comment text, garnish text, sauce text, degree text, spice text, amount int)')
        self.query('CREATE TABLE IF NOT EXISTS questions (cid int, question text)')
        self.query('CREATE TABLE IF NOT EXISTS regime (bron int, delivery int)')
        self.query('CREATE TABLE IF NOT EXISTS status (idx text, status text)')
        self.query('CREATE TABLE IF NOT EXISTS users (id int, name text, lastname text, birthday date, phone_number text, entry_number text, balance float)')

    def query(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.connection.commit()

    def fetchone(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()

    def __del__(self):
        self.connection.close()