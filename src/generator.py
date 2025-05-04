import random

def generate_date():
    hour = str(random.randint(0, 23))
    minute = str(random.randint(0, 59))
    second = str(random.randint(0, 59))
    return f'{hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}'
