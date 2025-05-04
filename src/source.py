import csv
import json
import os
import uuid


def read_postal_csv(file_path):
    black_list = set(['PR', 'PW', 'GU', 'VI', 'MP', 'AS', 'MH', 'FM', 'DC'])
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = []
        for i, row in enumerate(reader):
            if not i:
                continue
            postal = row[9]
            state = row[8]
            if state in black_list:
                continue
            obj = {'postal': postal, 'state': state}
            data.append(obj)
    return data


def get_tenants():
    file_name = 'tenants.json'
    if os.path.exists(file_name):
        with open(file_name, 'r') as fp:
            return json.load(fp)
    else:
        tenants =  [{"id": str(uuid.uuid4()), "name": f"Tenant {i}"} for i in range(1, 31)]
        with open(file_name, 'w') as fp:
            json.dump(tenants, fp, indent=4)
        return tenants
