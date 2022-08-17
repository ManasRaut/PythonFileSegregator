# backend File
import os

def create_directories():
    directory_path = "C:/Users/DELL/Desktop/test_folder_structure"

    for i in range(1, 6):
        path = os.path.join(directory_path, 'directory{number}'.format(number=i))
        try:
            os.mkdir(path)
        except OSError:
            print("directory skipped")

    idx = 0
    obj = os.scandir(directory_path)

    for entry in obj:
        folder = os.path.join(directory_path, entry.name)
        for i in range(5):
            new_path = os.path.join(folder, "subdirectory{number}".format(number=i))
            try:
                os.mkdir(new_path)
            except OSError:
                print("directory skipped")
            for j in range(5):
                txt_file = open(os.path.join(new_path, "sample{index}.txt".format(index=idx)), "w")
                txt_file.close()
                idx += 1

    print("Folders Created!")



