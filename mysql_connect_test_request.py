from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor
import re


# Попытка подключения к БД
def connection():
    try:
        cursor = pymysql.cursors.DictCursor
        connection = pymysql.connect(
            host='192.168.129.58',
            user='asterisk',
            password='c9eec2B4f3',
            db='asterisk',
            charset='utf8mb4',
            cursorclass=cursor
        )
        return connection
    except pymysql.err.OperationalError:
        return 0


# Запрос файла записи разговора из БД и возврат пути к этому файлу
def call_record(connection, i):
    if connection == 0:
        print("error")
    else:
        with closing(connection) as connection:
            with connection.cursor() as cursor:
                query = "SELECT recordingfile FROM cdr WHERE uniqueid = %s" %i
                cursor.execute(query)
                if cursor == 0:
                    print("0")
                else:
                    for row in cursor:
                        print(row['recordingfile'])
                        file_name = row['recordingfile']
                        result = re.split('-', file_name)
                        print(result)
                        #date = result[3]
                        #year = date[0:4]
                        #month = date[4:6]
                        #day = date[6:8]
                        #path = "http://192.168.119.250/monitor/%s/%s/%s/%s" % (year, month, day, file_name)
                        #print(path)

def main():
    print("start")
    id = ['1648375139.27977801', '1648375139.27977796']
    for i in id:
        print(i)
        call_record(connection(), i)
        print("end cycle")


if __name__ == '__main__':
    main()

