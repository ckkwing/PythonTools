import os
import codecs
import wmi
import common.Utility

HISTORY_FILE_NAME = ".history"


def clean(root):
    if not os.path.exists(root):
        print("not exists")
        return

    if not os.path.isdir(root):
        print("not a dir")
        return

    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if common.Utility.get_file_extension(filename) == HISTORY_FILE_NAME:
                os.remove(os.path.join(dirpath, filename))


def create_histories(root, isfileincluded):
    if not os.path.exists(root):
        print("not exists")
        return

    if not os.path.isdir(root):
        print("not a dir")
        return

    for dirpath, dirnames, filenames in os.walk(root):
        print("dirpath: " + dirpath)
        historyList = list()
        historyfilename = os.path.join(dirpath, (os.path.basename(dirpath) + HISTORY_FILE_NAME))
        if os.path.exists(historyfilename):
            with codecs.open(historyfilename, "r", encoding='utf-8') as file:
                for line in file:
                    strtemp = line.strip()
                    print("exist line: " + strtemp)
                    if strtemp != "":
                        historyList.append(strtemp)

        realitemlen = len(dirnames)
        if isfileincluded:
            realitemlen += len(filenames)

        if realitemlen > 0:
            with codecs.open(historyfilename, "a", encoding='utf-8') as file:
                newline = ""
                for dirname in dirnames:
                    print("dirname: " + dirname)
                    newline = os.path.join(dirpath, dirname)
                    if newline not in historyList:
                        file.write(newline)
                        file.write(os.linesep)

                if isfileincluded:
                    for filename in filenames:
                        print("filename: " + filename)
                        if common.Utility.get_file_extension(filename) == HISTORY_FILE_NAME:
                            continue
                        newline = os.path.join(dirpath, filename)
                        if newline not in historyList:
                            file.write(newline)
                            file.write(os.linesep)


print("Start-----------------")
c = wmi.WMI()
inputStr = input("Selet your folder: ")
rootpath = inputStr.strip()
# clean(rootpath)
create_histories(rootpath, False)
print("End-----------------")
