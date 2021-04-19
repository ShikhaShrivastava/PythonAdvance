# Dynamic Read/Select

import mysql.connector

host = 'localhost'
port = 3306
user = 'root'
password = 'root123'
database = 'cricketerdetails'


def close_connection(my_con, my_cursor):
    if my_con.is_connected():
        my_cursor.close()
        print('cursor object is closed')
        my_con.close()
        print(f'connection got closed from :{database} database')


def select_record():
    try:
        my_con = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database)
        print(f'python program got connected to the database: {database}')

        my_cursor = my_con.cursor()
        print(f'cursor object got created which is pointing to the table')

        # select * from `tablename` where `columnname`=%s
        sql_select_query = """select * from `cricketer` where `name` = %s"""
        name = input('Enter the name of the cricketer\n')
        input_data = (name,)

        my_cursor.execute(sql_select_query, input_data)
        print('sql query got executed on the table')

        record = my_cursor.fetchone()
        print(record)
        print(type(record))
        print('The data available within 1st row')
        print(f'Name: {record[0]}')
        print(f'Age: {record[1]}')
        print(f"Country: {record[2]}")

    except mysql.connector.Error as msg:
        print(f'The cause of the exception is: {msg}')

    finally:
        close_connection(my_con, my_cursor)


if __name__ == '__main__':
    select_record()