import mysql.connector
from mysql.connector import Error


pw = 'mano34835965'
db = 'db_leroy'


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


def execute_query(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print('Query was successful!')
    except Error as err:
        print(f"Error: '{err}'")



lm = 11111111
title = 'lol'
preco = '24.65'

data = (lm,title,preco)

informacoes_do_produto = """
INSERT INTO products (lm, title, price) VALUES
(%s, %s, %s);
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, informacoes_do_produto,data)
