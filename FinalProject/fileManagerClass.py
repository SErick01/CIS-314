import os, shutil, glob


extensions = {
    # Images
    ".bmp": "BMP_Images", ".gif": "GIF_Images", ".heic": "HEIC_Images",
    ".jpeg": "JPEG_Images", ".jpg": "JPG_Images", ".png": "PNG_Images",
    ".tiff": "TIFF_Images", ".webp": "WEBP_Images",

    # Videos
    ".avi": "AVI_Videos", ".mkv": "MKV_Videos", ".mov": "MOV_Videos",
    ".mp4": "MP4_Videos", ".mpeg": "MPEG_Videos", ".wmv": "WMV_Videos",

    # Audio
    ".aac": "AAC_Audio", ".flac": "FLAC_Audio", ".mp3": "MP3_Audio",
    ".ogg": "OGG_Audio", ".wav": "WAV_Audio", ".wma": "WMA_Audio",

    # Documents
    ".doc": "DOC_Documents", ".docx": "DOCX_Documents", ".pdf": "PDF_Documents",
    ".ppt": "PPT_Documents", ".pptx": "PPTX_Documents", ".txt": "TXT_Documents",
    ".xls": "XLS_Documents", ".xlsx": "XLSX_Documents",

    # Compressed Files
    ".7z": "7Z_Compressed", ".bz2": "BZ2_Compressed", ".gz": "GZ_Compressed",
    ".rar": "RAR_Compressed", ".tar": "TAR_Compressed", ".zip": "ZIP_Compressed",

    # Programming/Code Files
    ".c": "C_Code", ".cpp": "CPP_Code", ".cs": "CS_Code", ".html": "HTML_Code",
    ".java": "JAVA_Code", ".js": "JS_Code", ".json": "JSON_Files",
    ".php": "PHP_Code", ".py": "PY_Code", ".rb": "RB_Code", ".xml": "XML_Files",

    # Executables
    ".exe": "EXE_Files", ".msi": "MSI_Files", ".sh": "SH_Scripts", ".bat": "BAT_Scripts",

    # Miscellaneous
    ".csv": "CSV_Files", ".ics": "ICS_Calendar", ".md": "Markdown_Files",
    ".rtf": "RTF_Documents", ".sqlite": "SQLite_Databases", ".yml": "YAML_Files"
}


class FileManager:

    @staticmethod
    def copy_files(src, dest, ext_list):
        for file in os.listdir(src):
            if os.path.splitext(file)[1] in ext_list:
                shutil.copy(os.path.join(src, file), dest)

    @staticmethod
    def sort_files(src, dest, ext_list):
        for file in os.listdir(src):
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in ext_list:
                folder = extensions.get(file_ext, "Other_Files")
                folder_path = os.path.join(dest, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(os.path.join(src, file), folder_path)

    @staticmethod
    def rename_files(src, ext_list, prefix):
        for ext in ext_list:
            files = glob.glob(os.path.join(src, f"*{ext}"))
            files.sort(key=os.path.getctime)
            for index, file in enumerate(files):
                new_name = f"{prefix}_{str(index + 1).zfill(3)}{ext}"
                os.rename(file, os.path.join(src, new_name))
