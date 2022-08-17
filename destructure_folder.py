# backend File
import os
import shutil

def destructure_folder(directory_path):
    destructured_path = os.path.join(directory_path,"destructured_file_storage")
    try:
        os.mkdir(destructured_path)
    except OSError:
        print("Folder already destructured")

    for root, directories, files in os.walk(directory_path):
        for file in files:
            src_path = os.path.join(root, file)
            shutil.move(src_path, os.path.join(destructured_path, file))

    file_obj = os.scandir(directory_path)
    for entry in file_obj:
        if entry.is_dir():
            if entry.name != "destructured_file_storage":
                shutil.rmtree(os.path.join(directory_path, entry.name))

    print("Destructuring completed!")


