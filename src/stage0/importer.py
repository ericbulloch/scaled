import json
import os
import sqlite3
from time import time


def map_order(order):
    return tuple([
        order['tenant_uuid'],
        order['tenant_name'],
        order['postal'],
        order['state'],
        order['timestamp'],
        json.dumps(order['items']),
    ])


def main():
    database = 'database.db'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tenant_uuid TEXT,
            tenant_name TEXT,
            postal TEXT,
            state TEXT,
            timestamp TEXT,
            items TEXT
        )
    ''')
    connection.commit()
    for root, dirs, files in os.walk('orders'):
        if not files:
            continue
        for file in files:
            full_path = os.path.join(root, file)
            start = time()
            print(f'starting to import {full_path}')
            with open(full_path, 'r') as fp:
                orders = json.load(fp)
            sql = 'INSERT INTO orders (tenant_uuid, tenant_name, postal, state, timestamp, items) VALUES (?, ?, ?, ?, ?, ?)'
            cursor.executemany(sql, [map_order(order) for order in orders])
            connection.commit()
            print(f'{time() - start} seconds to import {full_path}')


if __name__ == '__main__':
    main()
