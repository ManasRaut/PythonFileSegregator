# backend File
import time
import os
import fileSegregation
import json
from pathlib import Path

def scan_dir():
    file_sort = fileSegregation.SegregateFiles(monitor_path)
    folder_obj = os.scandir(monitor_path)
    for file in folder_obj:
        if file.is_file():
            file_sort.moveFile(os.path.join(monitor_path,file), file)

def save_home_path():
    file = open('path.json', 'w+')
    data = {'monitor_path': os.path.join(Path.home(), 'Desktop\\test_folder_structure')}
    file.write(json.dumps(data))
    file.close()
    return data['monitor_path']

def start():
    file = open('program.txt', 'r')
    while True:
        try:
            time.sleep(3)
            file.seek(0)
            txt = file.read()
            if txt == 'stop':
                file.close()
                raise Exception()
            scan_dir()
            print("Scanned", monitor_path)
        except: 
            file = open('program.txt', 'w')
            file.write('stop')
            file.close()
            print("Stopping ..")
            break

monitor_path = json.loads(open("path.json", "r").read())["monitor_path"]
if not os.path.exists(monitor_path):
    monitor_path = save_home_path()