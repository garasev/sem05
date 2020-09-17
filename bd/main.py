import faker as f
import csv
import random
import string
import numpy
from datetime import date, timedelta



symbols = string.ascii_uppercase + string.digits


def random_ascii(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


def random_digits(length):
    return ''.join(random.choice(string.digits) for _ in range(length))


def random_string(length):
    return ''.join(random.choice(symbols) for _ in range(length))


def datageneration(data_base):
    name = data_base[0]
    records = data_base[1]
    schema = data_base[2]
    fake = f.Faker('ru_RU')
    file = open(name, 'w')
    for i in range(records):
        s = ''
        for j, attr in enumerate(schema):
            if attr == 'id_p':
                s += str(i + 1)
            elif attr == 'name':
                s += fake.name()
            elif attr == 'rating':
                s += str(round(random.random() * 5, 1))
            elif attr == 'experience':
                s += str(round(random.random() * 5))
            elif attr == 'model':
                s += 'model-' + random_string(3)
            elif attr == 'random_m':
                s += str(round(random.random() * 3) * 10 + 80)
            elif attr == 'country':
                s += fake.country()
            elif attr == 'plate':
                s += random_digits(1) + random_ascii(3) + random_digits(2)
            elif attr == 'id_10':
                s += str(round(random.random() * 9) + 1)
            elif attr == 'random_h':
                s += str(round(random.random() * 1000) * 100)
            elif attr == 'ready':
                s += str(True) if random.random() > 0.05 else str(False)
            elif attr == 'id_80':
                s += str(round(random.random() * 79) + 1)
            elif attr == 'id_40':
                s += str(round(random.random() * 39) + 1)
            elif attr == 'time':
                t = i * 4
                h = t // 60
                if h < 10:
                    s += '0'
                s += str(h) + ':'

                m = t % 60
                if m < 10:
                    s += '0'
                s += str(m)

            if j != len(schema) - 1:
                s += ', '
        s += '\n'

        file.write(s)
    file.close()
    print(' *', name, 'generation complete!')


def create_matrix():
    conductor_list = []
    bunny_list = []
    fake = f.Faker('ru_RU')

    for i in range(80):
        conductor_item = [fake.name(), str(round(random.random() * 5, 1)), 0]
        conductor_list.append(conductor_item)

    for i in range(1000):
        bunny_list.append([fake.name(), 0])

    file = open('fines.csv', 'w')
    for i in range(5000):
        s = ''
        s += str(i + 1) + ', '
        id_c = round(random.random() * 79)
        conductor_list[id_c][2] += 1
        id_b = round(random.random() * 999)
        bunny_list[id_b][1] += 1
        s += str(id_c + 1) + ', '
        s += str(id_b + 1) + ', '
        d1 = date(2018, 9, 18)  # начальная дата
        d2 = date(2020, 9, 18)  # конечная дата

        delta = (d2 - d1) * random.random()
        s += str(d1 + delta)
        s += '\n'

        file.write(s)
    file.close()
    print(' *', 'fines.csv', 'generation complete!')

    file = open('conductor.csv', 'w')

    for i in range(80):
        s = str(i + 1) + ', ' + conductor_list[i][0] + ', ' + conductor_list[i][1] + ', ' + str(conductor_list[i][2])
        s += '\n'
        file.write(s)

    file.close()
    print(' *', 'conductor.csv', 'generation complete!')

    file = open('bunny.csv', 'w')

    for i in range(1000):
        s = str(i + 1) + ', ' + bunny_list[i][0] + ', ' + str(bunny_list[i][1])
        s += '\n'
        file.write(s)

    file.close()
    print(' *', 'bunny.csv', 'generation complete!')


data_base = [
    ['drivers.csv', 80, ['id_p', 'name', 'rating', 'experience']],
    ['models.csv', 10, ['id_p', 'model', 'random_m', 'country']],
    ['tram.csv', 40, ['id_p', 'plate', 'id_10', 'random_h', 'ready']],
    ['schedule.csv', 360, ['id_p', 'time', 'id_40', 'id_80', 'id_80', ]],
]
if __name__ == '__main__':
    datageneration(data_base[0])
    datageneration(data_base[1])
    datageneration(data_base[2])
    datageneration(data_base[3])

    create_matrix()

    print("CSV generation complete!")
