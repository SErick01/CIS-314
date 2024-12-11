from fileManagerClass import FileManager


class ActionController:

    def __init__(self):
        self.file_manager = FileManager()

    def execute_action(self, action, src, dest, ext_list, prefix):
        if action == "Copy Only":
            self.file_manager.copy_files(src, dest, ext_list)
        elif action == "Sort Only":
            self.file_manager.sort_files(src, dest, ext_list)
        elif action == "Rename Only":
            self.file_manager.rename_files(src, ext_list, prefix)
        elif action == "Copy & Sort":
            self.file_manager.copy_files(src, dest, ext_list)
            self.file_manager.sort_files(dest, dest, ext_list)
        elif action == "Sort & Rename":
            self.file_manager.sort_files(src, dest, ext_list)
            self.file_manager.rename_files(dest, ext_list, prefix)
        elif action == "Copy & Sort & Rename":
            self.file_manager.copy_files(src, dest, ext_list)
            self.file_manager.sort_files(dest, dest, ext_list)
            self.file_manager.rename_files(dest, ext_list, prefix)
