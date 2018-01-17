import os
# import sys
# from os.path import join, getsize

# for dirpath, dirnames, filenames in os.walk("D:\Stash\mou\src\Debug"):
#     # print(dirpath, "consumes", end=" ")
#     # print(sum(getsize(join(dirpath, name)) for name in filenames), end=" ")
#     # print("bytes in", len(filenames), "non-directory files")
#     print("start path: " + dirpath)
#     for dir in dirnames:
#         print("sub folder: " + dir)
#     for file in filenames:
#         print("file: " + file)

selfHistoryExtension = ".history"

def updateHistory(rootPath):
    strRootPath = rootPath
    strHistoryFileName = "{0}{1}".format(os.path.basename(strRootPath), selfHistoryExtension)
    strHistoryFilePath = os.path.join(strRootPath, strHistoryFileName)

    historyList = list()
    bHistoryFileExist = bool(False)

    if os.path.exists(strHistoryFilePath):
        bHistoryFileExist = True
        with open(strHistoryFilePath, "r") as file:
            for line in file:
                strTemp = line.strip()
                print("exist line: " + strTemp)
                if strTemp != "":
                    historyList.append(strTemp)

    #     file_fd = os.open(strHistoryFilePath, os.O_RDWR)
    #     try:
    #         for line in file_fd:
    #             print(line)
    #     except OSError as err:
    #         print("OS error: {0}".format(err))
    #     except:
    #         print("Unexpected error:", sys.exc_info()[0])
    #         # raise
    #

    currentList = list()
    systemFiles = os.listdir(strRootPath)
    for systemFile in systemFiles:
        fullFileName = os.path.join(strRootPath, systemFile)
        if os.path.isdir(fullFileName):
            print("dir: " + fullFileName)
        if os.path.isfile(fullFileName):
            print("file: " + fullFileName)
            if os.path.splitext(fullFileName)[1] == selfHistoryExtension:
                continue
        currentList.append(fullFileName)

    newHistory = list()
    for filePath in currentList:
        if filePath not in historyList:
            newHistory.append(filePath)


    with open(strHistoryFilePath, "a") as file:
        for newLine in newHistory:
            file.write(newLine)
            file.write("\n")

    str = "temp"


listScannedPaths1Rank = [
    "D:\\Media\\Movie\\Carton"
]

listScannedPaths2Rank =[
    #"G:\\Backup\\Especial"
]

for parentPath in listScannedPaths2Rank:
    systemFiles = os.listdir(parentPath)
    for systemFile in systemFiles:
        fullFileName = os.path.join(parentPath, systemFile)
        if os.path.isdir(fullFileName):
            listScannedPaths1Rank.append(fullFileName)

for path in listScannedPaths1Rank:
    updateHistory(path)