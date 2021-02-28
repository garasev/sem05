import psycopg2


class DatabaseFacade:
    def __init__(self):
        self.connection = psycopg2.connect(dbname='depo', user='postgres',
                                           password='1', host='localhost')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()
        self.cursor.close()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseFacade, cls).__new__(cls)
        return cls.instance

    def query_result(self):
        data = self.cursor.fetchall()
        if data is None:
            print(' No query provided!')
        else:
            print(type(data))
            print(type(data[0]))
            for row in data:
                # print(' ', row)
                for info in row:
                    print(info, end=')(')
                print('')

    # Сколько всего трамваев в депо
    def get_0(self):
        self.cursor.execute("SELECT COUNT(*) "
                            "FROM trams")

    # Первые 10 штрафов
    def get_1(self):
        self.cursor.execute("SELECT *"
                            "FROM fines "
                            "JOIN finers ON finers.finer_id = fines.finer_id "
                            "JOIN conductors ON conductors.conductor_id = fines.conductor_id "
                            "WHERE fines.fine_id <= 10")

    # Мин и макс зайцы в пределах своего рейтинга
    def get_2(self):
        self.cursor.execute("WITH CTE (name, raiting, finer_count, min_finer, max_finer) "
                            "AS "
                            "( "
                            "SELECT name, raiting, finer_count, "
                            "MIN(finer_count) OVER (PARTITION BY raiting) AS min_finer, "
                            "MAX(finer_count) OVER (PARTITION BY raiting) AS max_finer "
                            "FROM conductors "
                            ") "
                            "SELECT * "
                            "FROM CTE ")

    # Инфа
    def get_3(self):
        self.cursor.execute("SELECT table_name, table_type "
                            "FROM information_schema.tables "
                            "WHERE table_schema = 'public'")

    # функция
    def get_4(self):
        self.cursor.callproc("get_tram_count")

    # Многооператорная
    def get_5(self, hour):
        self.cursor.callproc("get_shedule_top_driver_after_hour", [hour])

    # Процедура
    def get_6(self, pid, cap):
        self.cursor.execute("CALL inc_capacity({}, {})".format(pid, cap))
        self.connection.commit()
        self.cursor.execute("SELECT * FROM models ")

    # Процедура
    def get_7(self):
        self.cursor.callproc("version")

    # Создание
    def get_8(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS task_8 (LIKE schedules INCLUDING ALL)")
        self.connection.commit()

    # Удаление
    def drop_8(self):
        self.cursor.execute("DROP TABLE IF EXISTS task_8 CASCADE")
        self.connection.commit()

    # Вставка
    def get_9(self):
        self.cursor.execute("INSERT INTO task_8 SELECT * FROM schedules")
        self.cursor.execute("SELECT * FROM task_8")


def print_options():
    print(" [0] Скалярный запрос")
    print(" [1] Запрос с несколькими соединениями")
    print(" [2] Запрос с ОТВ(CTE) и оконными функциями")
    print(" [3] Запрос к метаданным")
    print(" [4] Скалярная функция")
    print(" [5] Многооператорная или табличная функция")
    print(" [6] Хранимая процедура")
    print(" [7] Системная функция или процедура")
    print(" [8] Создать таблицу в базе данных")
    print(" [9] Выполнить вставку данных")


def menu():
    facade = DatabaseFacade()
    while True:
        print_options()
        option = int(input(" Choose wisely: "))
        if option == 0:
            facade.get_0()
            facade.query_result()
        elif option == 1:
            facade.get_1()
            facade.query_result()
        elif option == 2:
            facade.get_2()
            facade.query_result()
        elif option == 3:
            facade.get_3()
            facade.query_result()
        elif option == 4:
            facade.get_4()
            facade.query_result()
        elif option == 5:
            facade.get_5("02:00")
            facade.query_result()
        elif option == 6:
            facade.get_6(1, 10)
            facade.query_result()
        elif option == 7:
            facade.get_7()
            facade.query_result()
        elif option == 8:
            facade.get_8()
        elif option == 9:
            facade.get_9()
            facade.query_result()
        elif option == 88:
            facade.drop_8()


if __name__ == '__main__':
    menu()
