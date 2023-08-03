import sqlite3


class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(
            r"C:\\Users\\Елена\\lena_repo1" + r"\\become_qa_auto.sqlite"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"  # виводить версію бд
        self.cursor.execute(sqlite_select_Query)  # виконання запиту в бд
        record = self.cursor.fetchall()  # отримання результатів виконання
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):  # метод для отримання даних про всіх покупців
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)  # запит в базу даних
        record = self.cursor.fetchall()  # присвоюємо результат виконання запиту
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"  # змінна має текстовий формат тому лапки обов'язкові
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # медод для зміни (апдейту) кількості продукту
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"  # змінні мають числовий формат тому можна не брати в лапки
        self.cursor.execute(query)
        self.connection.commit()  # підтвердження змін в базі даних

    # метод перевірки того що дані змінилися
    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # метод що вставляє дані в таблицю Products
    def insert_product(self, product_id, name, descriprion, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{descriprion}', {qnt})"  # \ розбиває запит на декілька рядків
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    # метод що буде отримувати об'єднані дані з таблиці products
    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
