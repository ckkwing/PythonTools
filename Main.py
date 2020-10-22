import os
import common.utility
import re

def remove_all_special_characters(rootPath):
    if not os.path.exists(rootPath):
        print("Error: " + rootPath + " not exists")
        return
    characters_to_remove_from_file = ["javme.me_", "[44x.me]", "[FHD]", ".FHD", ".HD", "-SD"]
    characters_to_remove_from_folder = ["-C"]
    for c in characters_to_remove_from_file:
        characters_to_remove_from_folder.append(c)
    #characters_to_remove_from_folder.remove("-")
    errorList = list()
    url = rootPath
    for dirpath, dirs, files in os.walk(url):
        for dir in dirs:
            newDirName = dir
            for char in characters_to_remove_from_folder:
                reg = re.compile(re.escape(char), re.IGNORECASE)
                newDirName = reg.sub("", newDirName)
                #newDirName = newDirName.replace(char, "")
            try:
                os.renames(os.path.join(dirpath, dir), os.path.join(dirpath, newDirName))
            except Exception as e:
                errorList.append(dir)
        for file in files:
            newFileName = file
            for char in characters_to_remove_from_file:
                reg = re.compile(re.escape(char), re.IGNORECASE)
                newFileName = reg.sub("", newFileName)
                #newFileName = newFileName.replace(char.lower(), "")
            try:
                os.renames(os.path.join(dirpath, file), os.path.join(dirpath, newFileName))
            except Exception as e:
                errorList.append(file)
    if len(errorList) > 0:
        print("#####################Have Errors#####################")
        for error in errorList:
            print(error)


def rename_fist_image_to_cover(rootDir):
    errorList = list()
    imageFiles = list()
    for dirpath, dirs, files in os.walk(rootDir):
        for dir in dirs:
            findDir = os.path.join(dirpath, dir)
            imageFileList = common.utility.get_img_file(findDir)
            if len(imageFileList) > 0:
                iscoverfound = False
                for imageFile in imageFileList:
                    fileName = common.utility.get_file_name_without_extension(imageFile)
                    if ("cover" == fileName.lower()):
                        iscoverfound = True
                        break
                if not iscoverfound:
                    imageFiles.append(imageFileList[0])


    for imageFile in imageFiles:
        try:
            fileName = common.utility.get_file_name_without_extension(imageFile)
            if ("cover" != fileName.lower()):
                fileExtension = common.utility.get_file_extension(imageFile)
                newFileName = os.path.join(os.path.dirname(imageFile), "cover" + fileExtension)
                os.renames(imageFile, newFileName)
        except Exception as e:
            errorList.append(dir)

    if len(errorList) > 0:
        print("#####################Have Errors#####################")
        for error in errorList:
            print(error)


rootPath = r"\\192.168.1.104\Extra Disk\Temp"
remove_all_special_characters(rootPath)


rename_fist_image_to_cover(rootPath)

