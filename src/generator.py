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

def generate_orders(date, customer_types):
    current = datetime.strptime(date, '%Y-%m-%d')
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
    for tenant_id, customer_type in enumerate(customer_types):
        print('tenant_id', tenant_id)
        ranges = customer_type['weekend_orders_range'] if current.weekday() > 4 else customer_type['weekday_orders_range']
        for i in range(random.randint(*ranges)):
            tenant = tenants[tenant_id]
            postal_data = random.choice(postal)
            timestamp = f'{date}T{generate_date()}Z'
            number_of_items = random.randint(*customer_type['number_of_items_range'])
            order_items = []
            for j in range(number_of_items):
                item = random.choice(items)
                quantity = random.randint(*customer_type['quantity_range'])
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
        generate_orders(d, customer_types)
        print(f"Orders generated for {d}")
