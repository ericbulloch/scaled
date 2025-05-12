import json


def map_order(order):
    return tuple([
        order['tenant_uuid'],
        order['tenant_name'],
        order['postal'],
        order['state'],
        order['timestamp'],
        json.dumps(order['items']),
    ])
