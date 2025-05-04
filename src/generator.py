from datetime import datetime, timedelta
import random

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
