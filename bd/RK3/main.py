from peewee import *

con = PostgresqlDatabase('RK3', user='postgres', password='1', host='localhost')
cursor = con.cursor()


class BaseModel(Model):
    class Meta:
        database = con


class Emp(BaseModel):
    id_emp = AutoField(column_name='id_emp', primary_key=True)
    name = CharField(column_name='name', max_length=64)
    birthdate = DateField(column_name='birthdate')
    department = CharField(column_name='department', max_length=64)

    class Meta:
        table_name = 'employee'


class Log(BaseModel):
    id_emp = ForeignKeyField(Emp, column_name='id_emp')
    sysdate = DateField(column_name='sysdate')
    week = CharField(column_name='day_week', max_length=64)
    systime = TimeField(column_name='systime')
    type = IntegerField(column_name='type')

    class Meta:
        table_name = 'time_log'


def task_1(cur):
    cur.execute('SELECT department '
                'FROM employee '
                'GROUP BY department '
                'HAVING count(id_emp) > 10 ')
    res = cur.fetchall()
    for line in res:
        print(line)


def task_1_2():
    q = (Emp.select(Emp.department)
         .group_by(Emp.department)
         .having(fn.count(Emp.id_emp) > 10))
    for line in q:
        print(line.department)


def task_2(cur, date):
    cur.execute('SELECT employee.id_emp, employee.name '
                'FROM employee JOIN ('
                '   SELECT id_emp '
                '   FROM time_log '
                '   WHERE sysdate = %(date)s '
                '   GROUP BY id_emp '
                '   HAVING COUNT(*) <= 2 '
                ') AS tmp ON tmp.id_emp = employee.id_emp', {"date": date})
    res = cur.fetchall()
    for line in res:
        print(line)


def task_2_2(date):
    tmp = (Log.select(Log.id_emp)
           .where(Log.sysdate == date)
           .group_by(Log.id_emp)
           .having(fn.count(Log.id_emp) <= 2))
    q = (Emp.select(Emp.id_emp, Emp.name).join(tmp, on=(tmp.c.id_emp == Emp.id_emp)))
    for line in q:
        print(line.id_emp, line.name)


def task_3(cur, date):
    start = '9:00'
    cur.execute('SELECT department '
                'FROM employee JOIN ( '
                'SELECT id_emp '
                'FROM time_log '
                'WHERE sysdate = %(date)s AND type = 1 '
                'GROUP BY id_emp '
                'HAVING MIN(systime) > %(start)s ) '
                'AS tmp ON tmp.id_emp = employee.id_emp', {"date": date, "start": start})
    res = cur.fetchall()
    for line in res:
        print(line)


def task_3_2(date):
    tmp = (Log.select(Log.id_emp)
           .where(Log.sysdate == date, Log.type == 1)
           .group_by(Log.id_emp)
           .having(fn.min(Log.systime) > '9:00'))
    q = (Emp.select(Emp.department)
         .join(tmp, on=(tmp.c.id_emp == Emp.id_emp)))
    for line in q:
        print(line.department)


def menu():
    print('1) Найти все отделы, в которых работает более 10 сотрудников SQL')
    print('2) Найти все отделы, в которых работает более 10 сотрудников ORM')
    print('3) Найти сотрудников, которые не выходят с рабочего места в течение всего рабочего дня SQL')
    print('4) Найти сотрудников, которые не выходят с рабочего места в течение всего рабочего дня ORM')
    print('5) Найти все отделы, в которых есть сотрудники, опоздавшие в определенную дату SQL')
    print('6) Найти все отделы, в которых есть сотрудники, опоздавшие в определенную дату ORM')


while True:
    menu()
    i = int(input(' Введите число: '))
    if i == 1:
        task_1(cursor)
    elif i == 2:
        task_1_2()
    elif i == 3:
        date = '2020-12-28'
        task_2(cursor, date)
    elif i == 4:
        date = '2020-12-28'
        task_2_2(date)
    elif i == 5:
        date = input(' Введите дату (2020-12-28): ')
        task_3(cursor, date)
    elif i == 6:
        date = input(' Введите дату (2020-12-28): ')
        task_3_2(date)
