"""
Date:   10-18-2024
Author: Samantha A Erickson
Description:
    This program is designed to sort digital photos and videos of various types 
    by type and then rename them in structure format from oldest to newest.
"""
import os, shutil, timeit, os, glob

tally = 0
directory = "C:/Users/samma/OneDrive/Pictures"
extensions = {".gif":"GIF_Photos",   ".heic":"HEIC_Photos",
                  ".jpeg":"JPEG_Photos", ".jpg":"JPG_Photos",
                  ".mov":"MOV_Videos",   "png":"PNG_Photos",
                  "webp":"WEBP_Photos" }

def renameFiles(count, dir, ext):
    myPics.sort(key = os.path.getctime)
    start = timeit.default_timer()
    
    for type, name in ext.items():
        myPics = glob.glob(os.path.join(dir, type))
        for index, path in enumerate(myPics):
            newName = name + f"{str(index + 1).zfill(2)}" + type
            newPath = os.path.join(dir, newName)
            os.rename(path, newPath)
            count += 1
    
    elapsed = timeit.default_timer() - start
    printResults("renameFiles", count, elapsed)

def sortFiles(count, dir, ext):
    start = timeit.default_timer()

    for file in os.listdir(dir):
        count += 1
        filePath = os.path.join(dir, file)
        if os.path.isfile(filePath):
            ext = os.path.splitext(file)[1].lower()
            if ext in extensions:
                folder = extensions[ext]
                folderPath = os.path.join(dir, folder)
                os.makedirs(folderPath,exist_ok = True)
                newPath = os.path.join(folderPath, file)
                shutil.move(filePath, newPath)
            else:
                count -= 1
                print(f"Skipped file:{file} because extension not listed.")
    
    elapsed = timeit.default_timer() - start
    printResults("sortFiles", count, elapsed)

def printResults(caller, sum, time):
    if caller == "printResults":
        print("Files renamed Successfully.")
        print("The total number of files renamed is:", sum)
        print("The total time it took to search is: %.9f seconds\n" % time)
    elif caller == "sortFiles":
        print("\nAll related files have been organized.")
        print("The total number of files moved is:", sum)
        print("The total time it took to organize is: %.9f seconds\n" % time)

renameFiles(tally, directory, extensions)
tally = 0
sortFiles(tally, directory, extensions)
