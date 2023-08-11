from mysql.connector import Error
from src.db.connectors import my_sql, execute_sql


def write_to_mariadb(object_list):
    for o in object_list:
        quote_id = ()
        author_id = ()
        tag_id_list = []
        for key, value in o.__dict__.items():
            try:
                match key:
                    case 'quote':
                        quote_id = add_row_if_not_exists(key, 'text', value)
                    case 'author':
                        author_id = add_row_if_not_exists(key, 'name', value)
                    case 'tags':
                        for k, v in value.items():
                            tag_id_list.append(add_row_if_not_exists(key, "(tag, link)", (k, v)))

                if author_id != () and quote_id != ():
                    execute_sql(f'INSERT IGNORE INTO quote_author VALUES {quote_id[0], author_id[0]}')
                    author_id = ()

                if quote_id != () and tag_id_list != []:
                    for t in tag_id_list:
                        execute_sql(f'INSERT IGNORE INTO quote_tag VALUES {quote_id[0], t[0]}')
                    quote_id = ()
                    tag_id_list = []

            except Error as e:
                print(f"Error adding entry to database: {e}")


def add_row_if_not_exists(table_name, column_names, values):
    col_name = column_names
    val = values
    if "," in col_name:
        col_name = column_names.split(',')[0][1:].strip()
        val = values[0]
        values = '","'.join(values)
        column_names = column_names.strip('()')
    val = val.replace('"', "'")

    connection = my_sql()
    cursor = connection.cursor()

    cursor.execute(f'SELECT id FROM {table_name} WHERE {col_name} = "{val}"')

    if not cursor.fetchone():
        if len(values) > 100:
            values = val
        execute_sql(f'INSERT INTO {table_name} ({column_names}) VALUES ("{values}")')

    connection = my_sql()
    cursor = connection.cursor()

    cursor.execute(f'SELECT id FROM {table_name} WHERE ({col_name}) = ("{val}")')
    data = cursor.fetchone()

    connection.close()

    return data
