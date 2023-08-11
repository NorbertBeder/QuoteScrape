import os

import mysql.connector
from mysql.connector import Error


def my_sql():
    try:
        connection = mysql.connector.connect(host=os.getenv('HOST_IP'),
                                             database=os.getenv('DATABASE_NAME'),
                                             user=os.getenv("USER_NAME"),
                                             password=os.getenv('PASSWORD'),
                                             connect_timeout=int(os.getenv('CONNECTION_TIMEOUT'))
                                             )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("select database();")
            cursor.fetchone()
            return connection
    except Error as e:
        print("Error while connecting to database", e)


def execute_sql(statement):
    connection = my_sql()
    cursor = connection.cursor()
    cursor.execute(statement)
    connection.commit()
    connection.close()
