from fileManagerClass import FileManager

class ActionController:
    def __init__(self):
        self.fileManager = FileManager()

    def execute_action(self, action, src, dest, ext_list, prefix, folder_name):
        if action == "Copy Only":
            self.fileManager.copy_files(src, dest, ext_list, folder_name)
            
        elif action == "Rename Only":
            self.fileManager.rename_files(src, ext_list, prefix)

        elif action == "Sort Only":
            self.fileManager.sort_files(src, dest, ext_list, folder_name)
            
        elif action == "Copy & Rename":
            finalDest = self.fileManager.copy_files(src, dest, ext_list, folder_name)
            self.fileManager.rename_files(finalDest, ext_list, prefix)
        
        elif action == "Copy & Sort":
            finalDest = self.fileManager.copy_files(src, dest, ext_list, folder_name)
            self.fileManager.sort_files(finalDest, finalDest, ext_list, None)
        
        elif action == "Rename & Sort":
            self.fileManager.rename_files(src, ext_list, prefix)
            self.fileManager.sort_files(src, dest, ext_list, folder_name)

        elif action == "Copy & Rename & Sort":
            finalDest = self.fileManager.copy_files(src, dest, ext_list, folder_name)
            self.fileManager.rename_files(finalDest, ext_list, prefix)
            self.fileManager.sort_files(finalDest, finalDest, ext_list, None)
