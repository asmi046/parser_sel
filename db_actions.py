import pymysql
from config import HOST, PORT, USER, PASSWORD, DATABASE
def get_connection():
     return pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        cursorclass=pymysql.cursors.DictCursor)
def get_base_data(sql_query):
    try:
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
        finally:
            connection.close()
            return cursor.fetchall()
    except Exception as ex:
        print("Connection refused...")
        print(ex)

def create_load_field(count_in_base):
    try:
        connection = get_connection()
        try:
            query = "INSERT INTO `loads` (`id`, `created_at`, `updated_at`, `start_at`, `finish_at`, `count_in_base`, `count_fine`, `count_bug`, `bug_track`) VALUES (NULL, NULL, NULL, current_timestamp(), NULL, %s, NULL, NULL, NULL);"
            with connection.cursor() as cursor:
                cursor.execute(query,(count_in_base,))
        finally:
            connection.commit()
            connection.close()
            return cursor.lastrowid
    except Exception as ex:
        print("Connection refused...")
        print(ex)

def update_load_field(id=0, count_fine=0, count_bug=0, bug_track=""):
    try:
        connection = get_connection()
        try:
            query = "UPDATE `loads` SET `count_fine` = %s, `finish_at` = current_timestamp(), `count_bug` = %s, `bug_track` = %s  WHERE `loads`.`id` = %s;"
            with connection.cursor() as cursor:
                cursor.execute(query, (count_fine, count_bug, bug_track, id))
        finally:
            connection.commit()
            connection.close()
            return cursor.lastrowid
    except Exception as ex:
        print("Connection refused...")
        print(ex)

def create_price_line(price_info={}, tovar_info={}, load_id=0, product_id=0, loadet=False):
    try:
        connection = get_connection()
        try:
            query = "INSERT INTO `getting_prices`(`id`, `created_at`, `updated_at`, `load_at`, `load_id`, `product_information_id`, `name`, `marketplace`, `src_price_value`, `total_price_value`, `one_price_value`, `loadet`)" \
                    "VALUES(NULL, NULL, NULL, current_timestamp(), %s, %s, %s, %s, %s, %s, %s, %s);"
            with connection.cursor() as cursor:
                cursor.execute(query, (load_id, product_id, tovar_info['name'], tovar_info['marketplace'], price_info['src'], price_info['rez_cer'], price_info['metr'], loadet))
        finally:
            connection.commit()
            connection.close()
            return cursor.lastrowid
    except Exception as ex:
        print("Connection refused...")
        print(ex)