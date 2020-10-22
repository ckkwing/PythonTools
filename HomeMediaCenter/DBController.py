import os
import sys

import psycopg2
from common import file_helper


class DBController:
    SQL_GET_ALL_FOLDERS = "SELECT * FROM folder"
    SQL_DELETE_FOLDER_BY_ID = "DELETE FROM folder WHERE %S"
    __conn = None

    def __init__(self):
        __conn = psycopg2.connect(database="Home", user="postgres", password="Nero123!", host="127.0.0.1", port="5432")

    def update_database(self):
        print("updateDB")
        self.deep_cleaning_database()

    def deep_cleaning_database(self):
        cur = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            item_ids_to_delete = list()
            cur.execute(self.SQL_GET_ALL_FOLDERS)
            rows = cur.fetchall()
            for row in rows:
                folder_path = row['path']
                if not os.path.exists(folder_path):
                    item_ids_to_delete.append(row['id'])

            # delete folder which is not exist
            delete_folder_condition = ""
            for folder_id in item_ids_to_delete:
                if 0 == len(delete_folder_condition):
                    delete_folder_condition += "id=" + folder_id
                else:
                    delete_folder_condition += "AND id=" + folder_id
            cur.execute(self.SQL_DELETE_FOLDER_BY_ID, delete_folder_condition)
            cur.commit()
        except Exception as e:
            print("Unexpected error:", sys.exc_info()[0])
        finally:
            cur.close()

    @staticmethod
    def __scan_files__(self, root_folder):
        file_list = list()
        for root, dirs, files in os.walk(root_folder):
            for name in files:
                file_path = os.path.join(root, name)
                print(file_path)
                file_list.append(file_path)
        return file_list
