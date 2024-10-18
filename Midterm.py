"""
Date:   10-18-2024
Author: Samantha A Erickson
Description:
    This program is designed to sort digital photos and videos of various types 
    by type and then rename them in structure format from oldest to newest.
"""
import os, shutil, timeit, os, glob

def sortFiles():
    count = 0
    dir = "C:/Users/samma/OneDrive/Pictures/Camera Roll/2024"
    extensions = {".heic":"HEIC_Photos",
                ".jpg":"JPG_Photes",
                ".mov":"MOV_Videos" }

    start = timeit.default_timer()
    for file in os.listdir(dir):
        count += 1
        filePath = os.path.join(dir,file)
        if os.path.isfile(filePath):
            ext = os.path.splitext(file)[1].lower()
            if ext in extensions:
                folder = extensions[ext]
                folderPath = os.path.join(dir,folder)
                os.makedirs(folderPath,exist_ok=True)
                newPath = os.path.join(folderPath,file)
                shutil.move(filePath, newPath)
            else:
                count -= 1
                print(f"Skipped file:{file} because extension not listed.")
    elapsed = timeit.default_timer() - start

    print("\nAll related files have been organized.")
    print("The total number of files moved is:",count)
    print("The total time it took to organize is: %.9f seconds\n" % elapsed)

def renameFiles():
    total = 0

    dir = "C:/Users/samma/OneDrive/Pictures/iCloud Photos/Downloads/Sisters"
    myPics = glob.glob(os.path.join(dir, "*.jpg"))
    myPics.sort(key=os.path.getctime)

    start = timeit.default_timer()
    for index, path in enumerate(myPics):
        newName = f"Sisters_{str(index + 1).zfill(2)}.jpg"
        newPath = os.path.join(dir,newName)
        os.rename(path,newPath)
        total += 1
    elapsed = timeit.default_timer() - start

    print("Files renamed Successfully.")
    print("The total number of files renamed is:",total)
    print("The total time it took to search is: %.9f seconds\n" % elapsed)

