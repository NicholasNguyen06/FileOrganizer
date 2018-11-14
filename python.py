import os
import datetime
import shutil #Use shutil instead of os.rename because files from external harddriver
outputFolder = os.getcwd() + "/Organized"

def main():
    pathInput = input("Please enter directory to look through: ")
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    for path, dirs, files in os.walk(pathInput):
        for filename in files:
            filePath = os.path.join(path, filename)
            x = os.stat(filePath)
            dateCreated = datetime.datetime.fromtimestamp(x.st_ctime)    
            createFolder(filePath, dateCreated)

def createFolder(filePath, dateCreated):
    fileMonth = dateCreated.strftime("%B")
    fileYear = dateCreated.year
    newYearFolder = outputFolder + "/" + str(fileYear)
    newMonthFolder = newYearFolder + "/" + str(fileMonth)
    if not os.path.exists(newYearFolder):
        os.makedirs(newYearFolder)
    if not os.path.exists(newMonthFolder):
        os.makedirs(newMonthFolder)
    shutil.move(filePath, newMonthFolder)

main()
