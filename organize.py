# backend File
import create_folders
import destructure_folder
import os
import shutil
import fileSegregation
import json

def one_time_sort():
    path = json.loads(open('path.json', 'r').read())
    file_sort = fileSegregation.SegregateFiles(path['monitor_path'])
    destructured_path = os.path.join(file_sort.target_path, "destructured_file_storage")
    destructure_folder.destructure_folder(file_sort.target_path)
    FILE_FORMATS = {file_format: directory
                    for directory, file_formats in file_sort.directories.items()
                    for file_format in file_formats}

    file_obj = os.walk(destructured_path)
    for root, directories, files in file_obj:
        for file in files:
            file_sort.moveFile(os.path.join(root,file), file)

    shutil.rmtree(destructured_path)
