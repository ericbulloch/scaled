import csv


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
