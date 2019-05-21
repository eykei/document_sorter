'''
description: Sorts all documents in a folder and places them into a folder based on the year it was created.
usage: specify the directory path, then run the file
status: Working
todo:
'''
import os, datetime, shutil


directoryPath="C:\\Users\\Austin\\Documents\\my documents\\old\\"

for file in os.listdir(directoryPath):
    if len(file) == 4 and file.isdigit():  # check if it is a 'year folder', if so skip
        continue
    initialPath = os.path.join(directoryPath, file)
    info = os.stat(initialPath)  # pull metadata from file
    mtime = info.st_mtime  # access modified time attribute
    dt=datetime.datetime.fromtimestamp(mtime)  # convert modified time (unix epoch) to datetime standard
    year=str(dt.year)
    os.makedirs(os.path.join(directoryPath,year), exist_ok=True)  # make a directory for that year. if it exists, that is fine.
    finalPath=(os.path.join(directoryPath,year,file))
    shutil.move(initialPath,finalPath)
