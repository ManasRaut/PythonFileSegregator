# backend File
import os
import shutil
import json
import logging

def basedOnKeywords(keyword_list, fileName):
    for pref in keyword_list:
        for word in pref["keywords"]:
            if fileName.find(word) != -1:
                return os.path.join(pref["path"], pref["folder_name"])
    return ""

def basedOnCategory(category_list, fileCategory):
    for pref in category_list:
        if fileCategory == pref["category"]:
            return os.path.join(pref["path"], pref["folder_name"])
    return ""

class SegregateFiles:
    def __init__(self, path):
        self.directories = json.loads(open("extentions.json", "r").read())
        self.target_path = path
        self.FILE_FORMATS = {file_format: directory
                             for directory, file_formats in self.directories.items()
                             for file_format in file_formats}
        self.settings = json.loads(open("settings.json", "r").read())
        logging.basicConfig(filename="history.log", format="%(asctime)s %(message)s", filemode="a")
        self.logger = logging.getLogger()
        self.logger.setLevel(20)

    def moveFile(self, currLoc, file):
        file_name, file_extension = os.path.splitext(file)
        keyword_list = [preferences for setting_list in self.settings.values()
                        for preferences in setting_list
                        if "keywords" in preferences.keys() and preferences['active'] == 'true']
        category_list = [preferences for setting_list in self.settings.values()
                         for preferences in setting_list
                         if "category" in preferences.keys() and preferences['active'] == 'true']
        keyWordPref = basedOnKeywords(keyword_list, file_name)
        if file_extension in self.FILE_FORMATS.keys():
            categoryPref = basedOnCategory(category_list, self.FILE_FORMATS[file_extension])
        else:
            categoryPref = ""
        if keyWordPref:
            folder_path = keyWordPref
        elif categoryPref:
            folder_path = categoryPref
        else:
            folder_name = file_extension[1:].upper()
            if file_extension in self.FILE_FORMATS.keys():
                folder_name = self.FILE_FORMATS[file_extension]
            folder_name += "_Files"
            folder_path = os.path.join(self.target_path, folder_name)
        try:
            os.mkdir(folder_path)
        except OSError:
            print("Already Exists..")
        try:
            shutil.move(currLoc, folder_path)
            self.logger.info(os.path.split(currLoc)[1] + " >> " + folder_path)
        except :
            pass
