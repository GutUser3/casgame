import sqlite3

def connection(db_name):
    con = None
    try:
        con = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return con

connect = connection('places.db')

def cities_from_db(connection):
    sql = ''' SELECT * FROM cities '''
    id_names = []
    try:
        cursor_obj = connection.cursor()
        cursor_obj.execute(sql)
        all_cities = cursor_obj.fetchall()
        for city in all_cities:
            id_names.append(city[0:2])
    except sqlite3.Error as e:
        print(e)
    return id_names

def employee_by_city_id(connection, city_id):
    sql = '''SELECT employees.first_name, employees.last_name, cities.title, countries.title, cities.area
             FROM employees
             JOIN cities ON employees.city_id = cities.id
             JOIN countries ON cities.country_id = countries.id
             WHERE cities.id = ?'''
    try:
        cursor_obj = connection.cursor()
        cursor_obj.execute(sql, (city_id, ))
        employees = cursor_obj.fetchall()
        for employee in employees:
            print('-' * 20)
            print(f"First Name: {employee[0]}")
            print(f"Last Name: {employee[1]}")
            print(f"City: {employee[2]}")
            print(f"Country: {employee[3]}")
            print(f"City Area: {employee[4]}")
    except sqlite3.Error as e:
        print(e)

def getting_info():
    cities = cities_from_db(connect)
    print('Вы можете отобразить список сотрудников '
          'по выбранному id города из перечня городов ниже. '
          'Для выхода из программы введите 0: ')
    for id, name in cities:
        print(f'{id} - {name}')
    user = input('Введите ID города: ')
    if user.isnumeric():
        if user == 0:
            print("Exiting program.")
        else:
            employee_by_city_id(connect, user)
    else:
        print("Invalid input. Please enter a numeric City ID.\n")
        getting_info()

getting_info()