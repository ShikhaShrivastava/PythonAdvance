'''write a python program to establish connection with database and insert a record/data within the table
dynamically(by collecting input from the user)'''

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


def insert_record():
    try:
        my_con = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database)
        print(f'python program got connected to the database: {database}')

        my_cursor = my_con.cursor()
        print(f'cursor object got created which is pointing to the table')

        # insert into tablename(columnnames) values(data/record)
        sql_insert_query = """insert into `cricketer`(`name`,`age`,`country`) values(%s,%s,%s)"""

        name = input('Enter the name of the cricketer\n')
        age = int(input('Enter the age of the cricketer\n'))
        country = input('Enter the country of the cricketer\n')
        record = (name, age, country)

        my_cursor.execute(sql_insert_query, record)
        print('sql query got executed on the table')

        my_con.commit()
        print('changes made within the table got committed in the database')

        print(f'The record got inserted within :{database} database')

    except mysql.connector.Error as msg:
        print(f'The cause of the exception is: {msg}')


    finally:
        close_connection(my_con, my_cursor)


if __name__ == '__main__':
    insert_record()