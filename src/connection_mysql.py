import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
user = os.getenv('USER')
password = os.getenv('PASSWORD')

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user=user,
        password=password,
        db='pythondb_mysql'
    )

    if connection.is_connected():
        print('connection succesfull')
        info_server=connection.get_server_info()
        print(info_server)
        cursor=connection.cursor()
        cursor.execute('SELECT DATABASE()')
        row=cursor.fetchone()
        print("Connected to db: {}".format(row))

        data=('SELECT * FROM videogames')
        cursor.execute(data)
        videogames=cursor.fetchall()

        for i in videogames:
            print("Name: ", i[1], ", Description: ", i[2])

except Exception as ex:
    print(ex)
finally:
    if connection.is_connected():
        connection.close()
        print("Desconnected")