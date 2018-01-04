import os

fileName = "F:\\Temp\\rework.nero.backitup_2012.MSI.ism"
outFile = fileName + ".tmp"
findText = "<table name=\"Property\">"
replaceText = "<row><td>NERO.RETAIL</td><td>YES</td><td/></row>"

fin=open(fileName,"r",encoding='UTF-8')
fout=open(outFile,"w",encoding='UTF-8')

found = 0
for l in fin.readlines():
    if found == 0 or l.find(replaceText) == -1:
        fout.write(l)
    if found > 0:
        found = found + 1
    if found == 8:
        fout.write("\t\t" + replaceText + "\n")
        print("Write: " + replaceText)
    if found == 0 and l.find(findText) != -1:
        print("Found: " + findText)
        found = 1

fin.close()
fout.close()

os.remove(fileName)
os.rename(outFile, fileName)