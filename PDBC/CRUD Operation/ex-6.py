'''write a python program to establish the connection with database and perform some deletion wrt data
available within table and display the data before and after updation is performed.'''

import mysql.connector

host = 'localhost'
port = 3306
user = 'root'
password = 'root123'
database = 'mydatabase'


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

        # select * from tablename
        sql_select_query = """select * from Employee"""

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

        # delete from tablename where columnname=data
        sql_delete_query = """delete from `Employee` where `location` = 'Mysore'"""
        my_cursor.execute(sql_delete_query)
        my_con.commit()
        print('new data has been deleted from the table')
        print()
        print('*************************************************************************************')

        sql_select_query = """select * from Employee"""

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