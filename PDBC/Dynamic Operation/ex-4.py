# Dynamic Update

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


def update_record():
    try:
        my_con = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database)
        print(f'python program got connected to the database: {database}')

        my_cursor = my_con.cursor()
        print(f'cursor object got created which is pointing to the table')

        # select * from tablename where columnname=data
        sql_select_query = """select * from cricketer"""

        my_cursor.execute(sql_select_query)
        print('sql query got executed on the table')

        records = my_cursor.fetchall()
        print(records)
        print(type(records))
        print('The data available within table')
        for record in records:
            print(f'Name: {record[0]}')
            print(f'Subject: {record[1]}')
            print(f"Location: {record[2]}")
        print('*************************************************************************************')

        # update tablename set columnname=%s where columnname=%s
        sql_update_query = """update cricketer set name = %s where country = %s"""
        name = input('Enter the name of cricketer\n')
        country = input('Enter the country of the cricketer\n')
        input_data = (name, country)
        my_cursor.execute(sql_update_query, input_data)
        my_con.commit()
        print('new data has been updated within the table')
        print()
        print('*************************************************************************************')

        sql_select_query = """select * from cricketer"""

        my_cursor.execute(sql_select_query)
        print('sql query got executed on the table')

        records = my_cursor.fetchall()
        print(records)
        print(type(records))
        print('The data available within table')
        for record in records:
            print(f'Name: {record[0]}')
            print(f'Subject: {record[1]}')
            print(f"Location: {record[2]}")



    except mysql.connector.Error as msg:
        print(f'The cause of the exception is: {msg}')

    finally:
        close_connection(my_con, my_cursor)


if __name__ == '__main__':
    update_record()