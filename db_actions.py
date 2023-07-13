import pymysql
from db_config import host, port, user, password, database
def get_base_data():
    try:
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM `product_information` ORDER BY RAND()")
                return cursor.fetchall()

        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)
