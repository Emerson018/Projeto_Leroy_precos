import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_pass):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_pass 
        )
        print("MySQL DB connection succesful!")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


pw = 'mano34835965'
db = 'db_leroy'
connection = create_server_connection('localhost','root', pw)

'''
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('DB create successfully!')
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "Create database db_leroy"
create_database(connection, create_database_query)
'''

def create_db_connection(host_name, user_name, user_pass, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_pass,
            database = db_name
        )
        print('MySQL DB connection successfull!')
    except Error as err:
        print(f"Error: '{err}")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query was successful!')
    except Error as err:
        print(f"Error: '{err}'")

'''
create_product_info = """
create table products(
lm int(10) primary key,
title varchar(100) not null,
price varchar(10) not null
)
"""
'''

#connection = create_db_connection("localhost","root", pw, db)
#execute_query(connection, create_product_info)

#lm, title, preco = format_data()

informacoes_do_produto = """
insert into products values
(99999999, 'Carinho de mão', '245.67');
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, informacoes_do_produto)