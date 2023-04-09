"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(host='localhost', database = 'north', user = 'postgres', password = '150774')
try:
    with conn:
        with conn.cursor()as cur:
            with open('../homework-1/north_data/customers_data.csv', 'r') as file: #получение данных из файла cuctomers.csv
                customers_data = csv.DictReader(file)
                for data in customers_data:
                    cur.execute('insert into customers values (%s, %s, %s)',
                                (data['customer_id'], data['company_name'], data['contact_name'])) #добавление данных в БД
            with open('../homework-1/north_data/employees_data.csv', 'r') as file: #получение данных из файла employees_data.csv
                employees_data = csv.DictReader(file)
                for id, data in enumerate(employees_data, 1):
                    cur.execute('insert into employees values (%s, %s, %s, %s, %s, %s)',
                                (id, data['first_name'], data['last_name'],
                                 data['title'], data['birth_date'], data['notes'])) #добавление данных в БД
                with open('../homework-1/north_data/orders_data.csv', 'r') as file: #получение данных из файла orders_data.csv
                    orders_data = csv.DictReader(file)
                    for data in orders_data:
                        cur.execute('insert into orders values (%s, %s, %s, %s, %s)',
                                    (data['order_id'], data['customer_id'],
                                     data['employee_id'], data['order_date'], data['ship_city'])) #добавление данных в БД
finally:
    conn.close() #закрытие соединения с БД

