import pymysql
from config import HOST, PORT, USER, PASSWORD, DATABASE
def get_base_data(sql_query):
    try:
        connection = pymysql.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                return cursor.fetchall()

        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)
