import os

# Characters that aren't allowed in file and folder names  in OneDrive, OneDrive for Business on Office 365,
# and SharePoint Online
SPECIAL_CHARAS_ONEDRIVE_1 = ''' * : < > ? / \ |'''
# Characters that aren't allowed in file and folder names in OneDrive for Business on SharePoint Server 2013
SPECIAL_CHARAS_ONEDRIVE_2 = '''~ " # % & * : < > ? / \ { | }.'''


def create_special_characters(root):
    if not os.path.exists(root):
        print("not exists")
        return

    str_characters = SPECIAL_CHARAS_ONEDRIVE_1
    str_characters += SPECIAL_CHARAS_ONEDRIVE_2
    for str in str_characters:
        if str == " ":
            continue
        file_name = os.path.join(root, str + ".txt")
        if os.path.exists(file_name):
            continue
        try:
            f = open(file_name, 'w')
            print
            file_name
            f.write("testtest")
            f.close()
            # with os.open(file_name, "a", encoding='utf-8') as file:
            #     print("file_name created")
            # os.mknod(file_name)
        except Exception as e:
            print(e)


print("Start-----------------")
inputStr = input("Selet your folder: ")
rootpath = inputStr.strip()
create_special_characters(rootpath)
print("End-----------------")

