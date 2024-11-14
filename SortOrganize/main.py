import os, shutil, timeit, glob

tally = 0
directory = "C:/Users/samma/OneDrive/Pictures"
extensions = {".gif":"GIF_Photos",   ".heic":"HEIC_Photos",
              ".jpeg":"JPEG_Photos", ".jpg":"JPG_Photos",
              ".mov":"MOV_Videos",   ".png":"PNG_Photos",
              ".webp":"WEBP_Photos" }

def rename_files(count, dir, ext):
    start = timeit.default_timer()
    
    #Locates files & sorted by date
    for type, name in ext.items():
        myPics = glob.glob(os.path.join(dir, "*" + type))
        myPics.sort(key = os.path.getctime)
        
        #Renames the files
        for index, path in enumerate(myPics):
            newName = name + f"{str(index + 1).zfill(2)}" + type
            newPath = os.path.join(dir, newName)
            os.rename(path, newPath)
            count += 1
    
    elapsed = timeit.default_timer() - start
    print_results("rename_files", count, elapsed)

def sort_files(count, dir, ext):
    start = timeit.default_timer()

    #Locates files
    for file in os.listdir(dir):
        filePath = os.path.join(dir, file)
        
        #Separating file from path
        if os.path.isfile(filePath):
            ext = os.path.splitext(file)[1].lower()
            
            #Locates new path, join new path to file, places file in new location
            #If folder for file does not exist, it will create folder
            if ext in extensions:
                folder = extensions[ext]
                folderPath = os.path.join(dir, folder)
                os.makedirs(folderPath,exist_ok = True)
                newPath = os.path.join(folderPath, file)
                shutil.move(filePath, newPath)
                count += 1
            
            else:
                print(f"Skipped file:{file} because extension not listed.")
    
    elapsed = timeit.default_timer() - start
    print_results("sort_files", count, elapsed)

def print_results(caller, sum, time):
    if caller == "rename_files":
        print("\nFiles renamed Successfully.")
        print("The total number of files renamed is:", sum)
        print("The total time it took to search is: %.9f seconds\n" % time)
    elif caller == "sort_files":
        print("\nFiles have been organized.")
        print("The total number of files moved is:", sum)
        print("The total time it took to organize is: %.9f seconds\n" % time)

if __name__ == "__main__":
    rename_files(tally, directory, extensions)
    tally = 0
    sort_files(tally, directory, extensions)
