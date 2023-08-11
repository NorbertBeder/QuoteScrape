from src.db.connectors import my_sql, execute_sql


def read_from_mysql(table, column):
    connection = my_sql()
    cursor = connection.cursor()
    cursor.execute(f'SELECT ({column}) FROM {table}')
    data_list = cursor.fetchall()

    return data_list


