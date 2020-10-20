# from selenium import webdriver
import os
import psycopg2
from common import FileHelper

# print(os.getcwd())
# chrome = webdriver.Chrome("chromedriver.exe")
#
# chrome.get("http://www.baidu.com")


file_list = list()
for root, dirs, files in os.walk(r"E:\SynologyDriveTeam\Software"):
    # for name in dirs:
    #     print(os.path.join(root, name))
    for name in files:
        file_path = os.path.join(root, name)
        print(file_path)
        # print("##"+os.path.dirname(file_path) +"##" + os.path.basename(file_path))
        file_stat = os.stat(file_path)
        file_list.append(file_path)

sql_format_insert_file = "INSERT INTO file (name, extension, path) VALUES (%s, %s, %s)"
conn = psycopg2.connect(database="Home", user="postgres", password="Nero123!", host="127.0.0.1", port="5432")

cur = conn.cursor()
for path in file_list:
    # sql_insert_str=sql_format_insert_file.format(os.path.basename(path), common.FileHelper.FileHelper.get_file_extension(path), path)
    # print(sql_insert_str)
    cur.execute(sql_format_insert_file,
                (os.path.basename(path),
                 FileHelper.get_file_extension(path),
                 os.path.normpath(path)))
    break
conn.commit()
conn.close()
