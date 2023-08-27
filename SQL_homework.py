import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def select_all_products(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        product_list = cursor.fetchall()
        for product in product_list:
            print(product)
    except sqlite3.Error as e:
        print(e)

def select_products_limits(connection):
    sql = '''SELECT * FROM products
    WHERE price < 100 and quantity > 5'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        product_list = cursor.fetchall()
        for product in product_list:
            print(product)
    except sqlite3.Error as e:
        print(e)

def add_products_from_list(connection, product):
    sql = '''INSERT INTO products 
    (product_title, price, quantity)
    VALUES(?, ?, ?) '''
    try:
        cursor = connection.cursor()
        for item in product:
            cursor.execute(sql, item)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_quantity(connection, product):
    sql = '''UPDATE products SET quantity = ?
    WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_price(connection, product):
    sql = '''UPDATE products SET price = ?
    WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(connection, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def search_products(connection, keyword):
    sql = '''SELECT * FROM products
    WHERE product_title LIKE ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, ('%' + keyword + '%',))
        product_list = cursor.fetchall()
        for product in product_list:
            print(product)
    except sqlite3.Error as e:
        print(e)

sql_create_table_of_products = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
product_title VARCHAR(200) NOT NULL,
price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

products_to_add = [
    ("Laptop", 999.99, 3),
    ("Smartphone", 699.50, 4),
    ("Headphones", 149.99, 50),
    ("Tablet", 299.75, 15),
    ("Camera", 499.00, 8),
    ("Monitor", 349.00, 12),
    ("Keyboard", 89.99, 30),
    ("Mouse", 29.95, 40),
    ("Speaker", 79.50, 25),
    ("Printer", 199.00, 5),
    ("Router", 69.00, 18),
    ("External Drive", 119.00, 15),
    ("Microphone", 59.99, 20),
    ("Scanner", 129.50, 10),
    ("Webcamera", 39.95, 30)
]

connection = create_connection('hw.db')
# create_table(connection, sql_create_table_of_products)

if connection is not None:
    # add_products_from_list(connection, products_to_add)    # select_all_products(connection)
    select_products_limits(connection)
    update_quantity(connection, (4, 2))
    update_price(connection, (98.3, 9))
    delete_product(connection, 1)
    search_products(connection, 'camera')




