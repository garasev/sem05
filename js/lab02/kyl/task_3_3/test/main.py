import csv
from random import *
from faker import Faker

records = 2000
people = []
people_health = ['alive' for _ in range(records)]
ts = []
dtp = []


alph = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

def generateModel():
    string = ''
    string+=choice(alph)
    string+=choice(alph)
    string+=str(randint(0, 10))
    string+=str(randint(0, 10))
    return string

def generateUniqeString():
    array = []
    for i in range(0, records):
        while True:
            string = generateNumber(10)
            if string not in array:
                array.append(string)
                break
            else:
                continue
    return array

def generateNumber(count):
    return ''.join(str(randint(0,10)) for _ in range(count))


def createPeople():
    with open('people.csv', 'w', newline='') as csvfile:
        fieldnames = ['id_person', 'person_name', 'sex', 'birthdate', 'passport', 'drive_license']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(len(people)):
            writer.writerow(people[i])
    print("Writing complete")

def createTS():
    with open('ts.csv', 'w', newline='') as csvfile:
        fieldnames = ['id_ts', 'id_person', 'type_ts', 'brand', 'model', 'release_year', 'register_number', 'color']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(len(ts)):
            writer.writerow(ts[i])
    print("Writing complete")

def createDTP():
    with open('dtp.csv', 'w', newline='') as csvfile:
        fieldnames = ['id_dtp', 'date_dtp', 'time_dtp', 'region_dtp', 'city_dtp', 'type_dtp', 'participant_dtp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(len(dtp)):
            writer.writerow(dtp[i])
    print("Writing complete")


def createParticipantDTP():
    with open('participantDtp.csv', 'w', newline='') as csvfile:
        fieldnames = ['id_participant', 'id_person', 'id_ts', 'state_health', 'type_participant', 'blame', 'id_violation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(len(participantDTP)):
            writer.writerow(participantDTP[i])
    print("Writing complete")


def getPeople():
    fake = Faker('ru_RU')
    passport = generateUniqeString()
    drive_license = generateUniqeString()
    sex = ["муж", "жен"]
    for i in range(0, records):
        sex_person = choice(sex)
        if sex_person == "муж":
            name_person = fake.name_male()
        else:
            name_person = fake.name_female()
        birthdate_person = fake.date()
        if birthdate_person > "2006-01-01":
            passport_person = "NULL"
        else:
            passport_person = passport[i]
        if birthdate_person > "2002-01-01":
            drive_license_person = "NULL"
        else:
            drive_license_person = drive_license[i]
        people.append(dict([
            ('id_person', i),
            ('person_name', name_person),
            ('sex', sex_person),
            ('birthdate', birthdate_person),
            ('passport', passport_person),
            ('drive_license', drive_license_person)
        ]
        ))

ts_cucher = []
ts_bycicle = []
ts_machine = []
ts_motocycle = []

def getTS():
    typeTS = ['легковой автомобиль', 'грузовой автомобиль', 'мотоцикл', 'трамвай', 'автобус', 'троллейбус', 'поезд', 'гужевой транспорт', 'велосипед']
    markaLAuto = ['Alpha Romeo', 'Aston Martin', 'Audi', 'Bentley', 'BMW', 'Bugatti',
                 'Cadillac', 'Chevrolet', 'Chery', 'Citroen', 'Corvette', 'Daewoo', 'Ferrari',
                 'Ford', 'Haval', 'Honda', 'Hyundai', 'Infinity', 'Jaguar', 'Jeep', 'Kamaz',
                 'KIA', 'Lada', 'Lifan', 'Lamborghini', 'Land Rover', 'Lexus', 'Mazda', 'Mini',
                 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'Opel', 'Peugeot', 'Porsche', 'Renault',
                 'Skoda', 'Suzuki', 'Tesla', 'Tayota', 'UAZ', 'Volvo', 'Volkswagen']
    markaGAuto = ['Тонор', 'БелАз', 'MAN', 'KAMAZ', 'MAZ', 'Foton']
    markaTrain = ['Уралтрансмаш', 'Рузхиммаш', 'Новокузнецкий ВСЗ', 'Метровагонмаш', 'Коломенский завод']
    markaBus = ['ГАЗ', 'ЗИЛ', 'ЛАЗ', 'РАФ']
    markaBicycle = ['Eltreco', 'KHE', 'Maxiscoo', 'Polisport', 'Scott', 'Stern', 'Trek']
    markaAnimal = ['Лошади', 'Волы', 'Буйволы', 'Ослы', 'Мулы', 'Собаки', 'Олени', 'Овцы']
    markaMotocycle = ['Hero', 'Irbis', 'Suzuki', 'BMW', 'Harley-Davidson', 'Triumph', 'Kawasaki', 'Honda',
                      'Yamaha', 'Ducati']

    color = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубый', 'синий', 'фиолетовый',
             'розовый', 'белый', 'черный', 'золотой', 'серебристый', 'коричневый']

    register = generateUniqeString()
    id_person = 0
    for i in range(0, records):
        while True:
            index = randint(0, 1999)
            person = people[index]
            if person.get('passport') == "NULL":
                continue
            else:
                id_person = index
                break

        type_ts = choice(typeTS)
        register_ts = register[i]
        model_ts = generateModel()
        color_ts = choice(color)
        release_year_ts = randint(1980, 2020)

        if type_ts == 'легковой автомобиль':
            marka_ts = choice(markaLAuto)

        if type_ts == 'грузовой автомобиль':
            marka_ts = choice(markaGAuto)

        if type_ts == 'мотоцикл':
            marka_ts = choice(markaMotocycle)

        if type_ts == 'велосипед':
            marka_ts = choice(markaBicycle)
            register_ts = "NULL"

        if type_ts == 'поезд' or type_ts == 'трамвай':
            marka_ts = choice(markaTrain)

        if type_ts == 'автобус' or type_ts == 'троллейбус':
            marka_ts = choice(markaBus)

        if type_ts == 'гужевой транспорт':
            marka_ts = choice(markaAnimal)
            release_year_ts = "NULL"
            model_ts = "NULL"
            color_ts = "NULL"
            register_ts = "NULL"

        ts_dict = dict([
            ('id_ts', i),
            ('id_person', id_person),
            ('type_ts', type_ts),
            ('brand', marka_ts),
            ('model', model_ts),
            ('release_year', release_year_ts),
            ('register_number', register_ts),
            ('color', color_ts)
        ]
        )

        ts.append(ts_dict)

        if type_ts == 'гужевой транспорт':
            ts_cucher.append(ts_dict)
        elif type_ts == 'велосипед':
            ts_bycicle.append(ts_dict)
        else:
            ts_machine.append(ts_dict)

region = [
'Республика Адыгея',
 'Республика Алтай',
'Алтайский край',
'Амурская область',
'Архангельская область',
'Астраханская область',
'Республика Башкортостан',
'Белгородская область',
'Брянская область',
'Республика Бурятия',
'Владимирская область',
'Волгоградская область',
'Вологодская область',
'Воронежская область',
'Республика Дагестан',
'Еврейская АО',
'Забайкальский край',
'Ивановская область',
'Республика Игушетия',
'Иркутская область',
'Кабардино-Балкария',
'Калининградская область',
'Республика Калмыкия',
'Калужская область',
'Камчатский край',
'Карачаево-Черкесия',
'Республика Карелия',
'Кемеровская область',
'Кировская область',
'Республика Коми',
'Костромская область',
'Краснодарский край',
'Красноярский край',
'Республика Крым',
'Севастополь',
'Курганская область',
'Курская область',
'Ленинградская область',
'Липецкая область',
'Магаданская область',
'Республика Марий Эл',
'Республика Мордовия',
'Москва',
'Московская область',
'Мурманская область',
'Ненецкий АО',
'Нижегородская область',
'Новгородская область',
'Новосибирская область',
'Омская область',
'Оренбургская область',
'Орловская область',
'Пензенская область',
'Пермский край',
'Приморский край',
'Псковская область',
'Ростовская область',
'Рязанская область',
'Самарская область',
'Санкт-Петербург',
'Саратовская область',
'Сахалинская область',
'Свердловская область',
'Республика Северная Осетия - Алания',
'Смоленская область',
'Ставропольский край',
'Тамбовская область',
'Республика Татарстан',
'Тверская область',
'Томская область',
'Тульская область',
'Республика Тыва',
'Тюменская область',
'Удмуртская Республика',
'Ульяновская область',
'Хабаровский край',
'Республика Хакасия',
'Ханты-Мансийский АО',
'Челябинская область',
'Республика Чечня',
'Чувашская Республика',
'Чукотский АО',
'Республика Саха (Якутия)',
'Ямало-Ненецкий АО',
'Ярославская область']

city = [[] for i in range(85)]
def readCity():
    f = open('city.txt')
    for line in f:
        newline = line.replace('),\n', '')
        newline = newline.replace('(', '')
        newline = newline.replace(';', '')
        newline = newline.replace(')', '')
        newline = newline.replace("'", '')
        tmp = newline.split(', ')
        city[int(tmp[1])-1].append(tmp[2])



count_type_dtp = [[] for _ in range(records)]
count_participant_dtp = [[] for _ in range(records)]
type_participant_dtp = [[] for _ in range(records)]
id_participant = 0

def getDTP():
    for i in range(0, 1000):
        date = ''
        year = randint(2018, 2020)
        date += str(year)
        date += '-'
        month = randint(1, 12)
        if month < 10:
            date += '0'
        date += str(month)
        date += '-'
        tmp = randint(1, 31)
        if month == 2:
            if year == 2020:
                tmp = randint(1, 29)
            else:
                tmp = randint(1, 28)
        elif month == 4 or month==6 or month == 9 or month == 11:
            tmp = randint(1, 30)
        else:
            tmp = randint(1, 31)
        if tmp < 10:
            date += '0'
        date += str(tmp)

        time = ''
        tmp = randint(0, 23)
        if tmp < 10:
            time += '0'
        time+=str(tmp)
        time+=':'
        tmp = randint(0, 59)
        if tmp < 10:
            time += '0'
        time += str(tmp)

        index_r = randint(0, 84)
        region_dtp = region[index_r]

        index_c = randint(0, len(city[index_r]) - 1)
        city_dtp = city[index_r][index_c]

        count_tag_dtp = randint(0, 3)

        passanger = 0
        driver = 1
        bicyclist = 0
        walker = 0
        cucher = 0

        for j in range(count_tag_dtp):
            while True:
                tmp = randint(0, 9)
                if tmp not in count_type_dtp[i]:
                    count_type_dtp[i].append(tmp)
                    if tmp == 0:
                        driver +=1
                    if tmp == 7:
                        passanger = 1
                    if tmp == 4:
                        walker = 1
                    if tmp == 5:
                        bicyclist = 1
                    if tmp == 6:
                        cucher = 1
                    break
                else:
                    continue

        count_part_dtp = driver + passanger + walker + bicyclist + cucher

        tmp = count_part_dtp
        if count_part_dtp < 5:
            count_part_dtp = randint(count_part_dtp, 5)

        for _ in range(tmp, count_part_dtp):
            passanger+=1

        type_participant_dtp[i].append(driver)
        type_participant_dtp[i].append(passanger)
        type_participant_dtp[i].append(walker)
        type_participant_dtp[i].append(bicyclist)
        type_participant_dtp[i].append(cucher)

        global id_participant
        for j in range(count_part_dtp):
            id_participant += 1
            count_participant_dtp[i].append(id_participant)

        for j in range(count_part_dtp):
            for k in range(count_tag_dtp):
                dtp.append(dict([
                    ('id_dtp', i),
                    ('date_dtp', date),
                    ('time_dtp', time),
                    ('region_dtp', region_dtp),
                    ('city_dtp', city_dtp),
                    ('type_dtp', count_type_dtp[i][k]),
                    ('participant_dtp', count_participant_dtp[i][j])
                ]))


participantDTP=[]
def getParticipant():
    blame = ['виновен', 'невиновен']
    health = ['цел', 'ранен', 'погиб']
    for i in range(0, 1000):
        print(i)
        count_driver = type_participant_dtp[i][0]
        count_passanger = type_participant_dtp[i][1]
        count_walker = type_participant_dtp[i][2]
        count_byciclist = type_participant_dtp[i][3]
        count_cucher = type_participant_dtp[i][4]
        count_all = count_cucher+count_walker+count_driver+count_byciclist + count_passanger
        tmp_state_health = [choice(health) for _ in range(count_all)]
        count_death = 0
        count_ranen = 0
        for k in range(len(tmp_state_health)):
            if tmp_state_health[k] == 'погиб':
                count_death+=1
            if tmp_state_health[k] == 'ранен':
                count_ranen+=1

        count = 0
        id = 0
        id_person_dtp = []
        id_ts_person_dtp = []
        while count < count_driver:
            while True:
                person = choice(people)
                if people_health[person.get('id_person')] == 'death' or person.get('drive_license') == 'NULL':
                    continue
                else:
                    if person.get('id_person') not in id_person_dtp:
                        id_person_dtp.append(person.get('id_person'))
                        break
                    else:
                        continue
            while True:
                ts_dtp = choice(ts_machine)
                if ts_dtp.get('id_ts') not in id_ts_person_dtp:
                    id_ts_person_dtp.append(ts_dtp.get('id_ts'))
                    break
                else:
                    continue
            hp = tmp_state_health[id]
            person_blame = choice('виновен')
            if person_blame == 'виновен':
                if hp == 'погиб' and count_death > 2:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'водитель'),
                        ('blame', person_blame),
                        ('id_violation', 6)
                    ]))
                if hp != 'погиб' and count_death > 1:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'водитель'),
                        ('blame', person_blame),
                        ('id_violation', 6)
                    ]))
                if hp == 'ранен' and count_ranen > 2:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'водитель'),
                        ('blame', person_blame),
                        ('id_violation', choice([4,5]))
                    ]))
                if hp != 'ранен' and count_ranen > 1:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'водитель'),
                        ('blame', person_blame),
                        ('id_violation', choice([4,5]))
                    ]))
                tmp = choice(['yes', 'no'])
                if tmp == 'yes':
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'водитель'),
                        ('blame', person_blame),
                        ('id_violation', choice([1, 3]))
                    ]))
            else:
                participantDTP.append(dict([
                    ('id_participant', count_participant_dtp[i][id]),
                    ('id_person', person.get('id_person')),
                    ('id_ts', ts_dtp.get('id_ts')),
                    ('state_health', hp),
                    ('type_participant', 'водитель'),
                    ('blame', 'невиновен'),
                    ('id_violation', 'NULL')
                ]))
            if hp == 'погиб':
                people_health[person.get('id_person')] = 'death'
            count+=1
            id+=1

        count = 0
        while count < count_passanger:
            hp = choice(health)
            while True:
                person = choice(people)
                if people_health[person.get('id_person')] == 'death':
                    continue
                else:
                    if person.get('id_person') not in id_person_dtp:
                        id_person_dtp.append(person.get('id_person'))
                        break
                    else:
                        continue
            hp = tmp_state_health[id]
            person_blame = choice(blame)
            if person_blame == 'виновен':
                if hp == 'погиб' and count_death > 2:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'пассажир'),
                        ('blame', person_blame),
                        ('id_violation', 6)
                    ]))
                if hp != 'погиб' and count_death > 1:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'пассажир'),
                        ('blame', person_blame),
                        ('id_violation', 6)
                    ]))
                participantDTP.append(dict([
                    ('id_participant', count_participant_dtp[i][id]),
                    ('id_person', person.get('id_person')),
                    ('id_ts', ts_dtp.get('id_ts')),
                    ('state_health', hp),
                    ('type_participant', 'пассажир'),
                    ('blame', person_blame),
                    ('id_violation', 3)
                ]))



            if hp == 'погиб':
                people_health[person.get('id_person')] = 'death'
            count+=1
            id+=1

        count = 0
        while count < count_walker:
            hp = choice(health)
            while True:
                person = choice(people)
                if people_health[person.get('id_person')] == 'death':
                    continue
                else:
                    if person.get('id_person') not in id_person_dtp:
                        id_person_dtp.append(person.get('id_person'))
                        break
                    else:
                        continue
            hp = tmp_state_health[id]
            person_blame = choice(blame)
            if person_blame == 'виновен':
                if hp == 'погиб' and count_death > 2:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'пешеход'),
                        ('blame', person_blame),
                        ('id_violation', 6)
                    ]))
                if hp != 'погиб' and count_death > 1:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'пешеход'),
                        ('blame', person_blame),
                        ('id_violation', 6)
                    ]))
                participantDTP.append(dict([
                    ('id_participant', count_participant_dtp[i][id]),
                    ('id_person', person.get('id_person')),
                    ('id_ts', ts_dtp.get('id_ts')),
                    ('state_health', hp),
                    ('type_participant', 'пешеход'),
                    ('blame', person_blame),
                    ('id_violation', 3)
                ]))
            if hp == 'погиб':
                people_health[person.get('id_person')] = 'death'
            count+=1
            id+=1

        count = 0
        while count < count_byciclist:
            hp = choice(health)
            while True:
                person = choice(people)
                if people_health[person.get('id_person')] == 'death':
                    continue
                else:
                    if person.get('id_person') not in id_person_dtp:
                        id_person_dtp.append(person.get('id_person'))
                        break
                    else:
                        continue
            while True:
                ts_dtp = choice(ts_bycicle)
                if ts_dtp.get('id_ts') not in id_ts_person_dtp:
                    id_ts_person_dtp.append(ts_dtp.get('id_ts'))
                    break
                else:
                    continue
            hp = tmp_state_health[id]
            person_blame = choice(blame)
            if person_blame == 'виновен':
                if hp == 'погиб' and count_death > 2:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'велосипедист'),
                        ('blame', person_blame),
                        ('id_violation', 6)
                    ]))
                if hp != 'погиб' and count_death > 1:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'велосипедист'),
                        ('blame', person_blame),
                        ('id_violation', 6)
                    ]))
                participantDTP.append(dict([
                    ('id_participant', count_participant_dtp[i][id]),
                    ('id_person', person.get('id_person')),
                    ('id_ts', ts_dtp.get('id_ts')),
                    ('state_health', hp),
                    ('type_participant', 'велосипедист'),
                    ('blame', person_blame),
                    ('id_violation', 7)
                ]))
            if hp == 'погиб':
                people_health[person.get('id_person')] = 'death'
            count+=1
            id+=1

        count = 0
        while count < count_cucher:
            hp = choice(health)
            while True:
                person = choice(people)
                if people_health[person.get('id_person')] == 'death' or person.get('drive_license') == 'NULL':
                    continue
                else:
                    if person.get('id_person') not in id_person_dtp:
                        id_person_dtp.append(person.get('id_person'))
                        break
                    else:
                        continue
            while True:
                ts_dtp = choice(ts_cucher)
                if ts_dtp.get('id_ts') not in id_ts_person_dtp:
                    id_ts_person_dtp.append(ts_dtp.get('id_ts'))
                    break
                else:
                    continue
            hp = tmp_state_health[id]
            person_blame = choice(blame)
            if person_blame == 'виновен':
                if hp == 'погиб' and count_death > 2:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'кучер'),
                        ('blame', person_blame),
                        ('id_violation', 6)
                    ]))
                if hp != 'погиб' and count_death > 1:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'кучер'),
                        ('blame', person_blame),
                        ('id_violation', 6)
                    ]))
                if hp == 'ранен' and count_ranen > 2:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'кучер'),
                        ('blame', person_blame),
                        ('id_violation', choice([4, 5]))
                    ]))
                if hp != 'ранен' and count_ranen > 1:
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'кучер'),
                        ('blame', person_blame),
                        ('id_violation', choice([4, 5]))
                    ]))
                tmp = choice(['yes', 'no'])
                if tmp == 'yes':
                    participantDTP.append(dict([
                        ('id_participant', count_participant_dtp[i][id]),
                        ('id_person', person.get('id_person')),
                        ('id_ts', ts_dtp.get('id_ts')),
                        ('state_health', hp),
                        ('type_participant', 'кучер'),
                        ('blame', person_blame),
                        ('id_violation', choice([1,7]))
                    ]))
            if hp == 'погиб':
                people_health[person.get('id_person')] = 'death'
            count+=1
            id+=1


if __name__ == '__main__':
    readCity()

    getPeople()
    getTS()
    getDTP()
    getParticipant()
    createPeople()
    createTS()
    createDTP()
    createParticipantDTP()