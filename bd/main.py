import faker as f
import csv
import random


def datageneration(name, records, schema):
    fake = f.Faker('ru_RU')
    file = open(name, 'w')
    for i in range(records):
        s = ''
        for attr in schema:
            if attr == 'id_p':
                s += str(i + 1) + ', '
            elif attr == 'name':
                s += fake.name() + ', '
            elif attr == 'id':
                s += random.

        s += '\n'

        file.write(s)


if __name__ == '__main__':
    name = 'Depo' + '.csv'
    records = 100
    headers = ['id_p', 'name']
    datageneration(name, records, headers)
    print("CSV generation complete!")