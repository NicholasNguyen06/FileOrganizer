import os
import datetime
import shutil #Use shutil instead of os.rename because files from external harddrive
outputFolder = os.getcwd() + "/Organized"
video_set = {".mp4", ".c4d", ".mov", ".avi", ".wmv"}
picture_set = {".jpeg", ".png", ".raw", ".pdf", ".tiff", ".gif"}

def main():
    pathInput = input("Please enter directory to look through: ")
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    for path, dirs, files in os.walk(pathInput):
        for filename in files:
            filePath = os.path.join(path, filename)
            fullPath, extension = os.path.splitext(filePath)
            print (fullPath, extension)
            x = os.stat(filePath)
            dateCreated = datetime.datetime.fromtimestamp(x.st_ctime)    
            createDateFolders(filePath, dateCreated)

# Creates the Year and Month subdirectories based on time created
def createDateFolders(filePath, dateCreated):
    fileMonth = dateCreated.strftime("%B")
    fileYear = dateCreated.year
    newYearFolder = outputFolder + "/" + str(fileYear)
    newMonthFolder = newYearFolder + "/" + str(fileMonth)
    fullPath, extension = os.path.splitext(filePath)
    if not os.path.exists(newYearFolder):
        os.makedirs(newYearFolder)
    if not os.path.exists(newMonthFolder):
        os.makedirs(newMonthFolder)
    createMediaFolders(filePath, newMonthFolder)

# Creates the media folders (Photo, Video) and moves the file accordingly
def createMediaFolders(filePath, directory):
    fullPath, extension = os.path.splitext(filePath)
    if extension in video_set:
        newVideoFolder = os.path.join(directory, "Video")
        if not os.path.exists(newVideoFolder):
            os.makedirs(newVideoFolder)
        shutil.copy2(filePath, newVideoFolder)
    elif extension in picture_set:
        newPictureFolder = os.path.join(directory, "Picture")
        if not os.path.exists(newPictureFolder):
            os.makedirs(newPictureFolder)
        shutil.copy2(filePath, newPictureFolder)
    else: 
        newOtherFolder = os.path.join(directory, "Other")
        if not os.path.exists(newOtherFolder):
            os.makedirs(newOtherFolder)
        shutil.copy2(filePath, newOtherFolder)
        

main()
