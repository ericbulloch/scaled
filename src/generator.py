from datetime import datetime, timedelta
import json
import os
import random

from source import get_items, get_tenants, read_postal_csv

def generate_date():
    hour = str(random.randint(0, 23))
    minute = str(random.randint(0, 59))
    second = str(random.randint(0, 59))
    return f'{hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}'

def generate_dates(days_ago):
    now = datetime.now()
    dates = []
    for i in range(days_ago + 1):
        date = now - timedelta(days=i)
        dates.append(date.strftime('%Y-%m-%d'))
    return dates[::-1]

def generate_orders(date, amount):
    parent_dir = 'orders'
    file_name = f'{os.path.join(parent_dir, date)}.json'
    if os.path.exists(file_name):
        with open(file_name, 'r') as fp:
            return json.load(fp)
    tenants = get_tenants()
    items = get_items()
    postal = read_postal_csv('postal.csv')
    orders = []
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    tenant_weights = [0.49] + [0.075] * 4 + [0.04] * 5 + [0.0005] * 20
    for i in range(amount):
        tenant = random.choices(tenants, weights=tenant_weights)[0]
        print(tenant)
        postal_data = random.choice(postal)
        timestamp = f'{date}T{generate_date()}Z'
        number_of_items = random.randint(1, 15)
        order_items = []
        for j in range(number_of_items):
            item = random.choice(items)
            quantity = random.randint(1, 30)
            order_items.append({
                "id": item['id'],
                "name": item['name'],
                "quantity": quantity,
                "price": item['price'],
                "cost": item['cost'],
            })
        order = {
            "postal": postal_data['postal'],
            "state": postal_data['state'],
            "timestamp": timestamp,
            "tenant_uuid": tenant["id"],
            "tenant_name": tenant['name'],
            "items": order_items,
        }
        orders.append(order)
    with open(file_name, 'w') as fp:
        json.dump(orders, fp, indent=4)
    return orders


if __name__ == '__main__':
    try:
        with open('config.json', 'r') as fp:
            config = json.load(fp)
    except FileNotFoundError:
        print('The config.json was not found. Please provide one to run this command.')
        exit(1)
    days_ago = config.get('days_ago', 30)
    customer_types = config.get('customer_types', [])
    if not customer_types:
        print('The config.json is missing customer_types. Please provide customer types.')
        exit(1)
    dates = generate_dates(days_ago=days_ago)
    for d in dates:
        current = datetime.strptime(d, '%Y-%m-%d')
        number_of_orders = 10 if current.weekday() > 4 else 30
        orders = generate_orders(d, number_of_orders)
        print(json.dumps(orders, indent=4))
        print(f"{number_of_orders} orders generated for {d}")
