# functions connecting GUI to backend
import subprocess
import json
from PyQt5.QtWidgets import QFileDialog

# complete
def save_target_folder(page):
    folder = str(QFileDialog.getExistingDirectory(page, 'Select Downloads Folder'))
    file_ = open('path.json', 'w')
    file_.write(json.dumps({'monitor_path': folder}))
    file_.close()
    page.target_folder_field.setText(folder)

# complete
def read_target_folder(page):
    file_ = open('path.json', 'r')
    path_settings = json.loads(file_.read())
    file_.close()
    page.target_folder_field.setText(path_settings['monitor_path'])

# complete
def navbar_clicked(widget, stackw):
    name = widget.objectName()
    if name == 'home':
        stackw.setCurrentIndex(0)
    elif name == 'custom':
        stackw.setCurrentIndex(2)
    elif name == 'history':
        stackw.setCurrentIndex(3)
    elif name == 'basic':
        stackw.setCurrentIndex(1)

# completed
def read_extension_settings(page):
    file_ = open('settings.json', 'r')
    settings = json.loads(file_.read())
    file_.close()
    category_settings = [setting for setting_list in settings.values() 
                            for setting in setting_list 
                            if 'category' in setting.keys()]
    page.settings_list = category_settings

# completed
def extension_dropDown_selected(page, widget):
    index = widget.currentIndex()
    page.clear_fields()
    setting = None
    if index == 1:
        setting = getSetting(page, 'IMAGES')
    elif index == 2:
        setting = getSetting(page, 'AUDIO')
    elif index == 3:
        setting = getSetting(page, 'DOCUMENT')
    elif index == 4:
        setting = getSetting(page, 'VIDEOS')
    elif index == 5:
        setting = getSetting(page, 'EXEC')
    if setting:
        page.selected_setting = setting
        page.dest_text_field.setText(setting['path'])
        page.folder_text_field.setText(setting['folder_name'])
        if ((setting['active'] == 'true' and not page.toggle_button.isON) 
        or (setting['active'] == 'false' and page.toggle_button.isON)):
            page.toggle_button.toggled()
    else: page.selected_setting = None

# completed
def extension_save_clicked(page):
    if page.selected_setting:
        settings = json.loads(open('settings.json', 'r').read())
        setting = settings['settings_list'][settings['settings_list'].index(page.selected_setting)]
        setting['active'] = str(page.toggle_button.isON).lower()
        setting['folder_name'] = page.folder_text_field.text()
        setting['path'] = page.dest_text_field.text()
        open('settings.json', 'w').write(json.dumps(settings, indent = 4 ))
        read_extension_settings(page)
        page.clear_fields()

# completed
def getSetting(page, k):
    for s in page.settings_list:
        if s['category'] == k: return s

# completed
def read_keywords_settings(page, wd):
    settings = json.loads(open('settings.json', 'r').read())
    keywords_settings = [setting for setting_list in settings.values() 
                            for setting in setting_list 
                            if 'keywords' in setting.keys()]
    page.settings_list = keywords_settings
    for i in range(page.scrollArea.layout.count()):
        page.scrollArea.layout.itemAt(i).widget().hide()
    for keyword in keywords_settings:
        page.scrollArea.layout.addWidget(wd.CustomItem(keyword, page))

# completed
def custom_save_clicked(page, wd):
    if page.selected_setting:
        settings = json.loads(open('settings.json', 'r').read())
        new_setting = settings['settings_list'][settings['settings_list'].index(page.selected_setting)]
        new_setting['path'] = page.dest_text_field.text()
        new_setting['folder_name'] = page.folder_text_field.text()
        new_setting['keywords'] = page.keywords_text_field.toPlainText().split()
        open('settings.json', 'w').write(json.dumps(settings, indent = 4))
        page.clear_fields()
        page.selected_setting = None
        read_keywords_settings(page, wd)
    else:
        save_new_custom_setting(page, wd)

# completed
def custom_clear_clicked(page):
    page.selected_setting = None
    page.folder_text_field.setText("")
    page.dest_text_field.setText("")
    page.keywords_text_field.setPlainText("")

# completed
def delete_custom_setting(page, wd):
    settings = json.loads(open('settings.json', 'r').read())
    settings['settings_list'].remove(wd.data)
    page.scrollArea.layout.removeWidget(wd)
    wd.hide()
    open('settings.json', 'w').write(json.dumps(settings, indent=4))

# completed
def disable_custom_setting(page, wd):
    settings = json.loads(open('settings.json', 'r').read())
    settings['settings_list'][settings['settings_list'].index(wd.data)]['active'] = str(wd.toggleSwitch.isON).lower()
    open('settings.json', 'w').write(json.dumps(settings, indent=4))
    wd.data['active'] = str(wd.toggleSwitch.isON).lower()

# completed
def save_new_custom_setting(page, wd):
    new_setting = dict()
    new_setting['path'] = page.dest_text_field.text()
    new_setting['folder_name'] = page.folder_text_field.text()
    new_setting['keywords'] = page.keywords_text_field.toPlainText().split()
    if new_setting['path'] and new_setting['folder_name'] and new_setting['keywords']:
        settings = json.loads(open('settings.json', 'r').read())
        for i,s in enumerate(settings['settings_list']):
            if not 'keywords' in s.keys():
                settings['settings_list'].insert(i, new_setting)
                break
        open('settings.json', 'w').write(json.dumps(settings, indent = 4))
        page.clear_fields()
        read_keywords_settings(page, wd)

# completed
def toggle_app(page):
    if page.isOn: stop_main_process(page)
    else: start_main_process(page)
    change_button_text(page)

# completed
def change_button_text(page):
    if not page.isOn:
        page.start_stop_btn.setText("Start")
    else:
        page.start_stop_btn.setText("Stop")

# completed
def start_main_process(page):
    print('starting ...')
    file = open('program.txt', 'w+')
    if file.read() == 'running':
        file.close()
        return
    file.seek(0)
    file.write('running')
    file.close()
    process = subprocess.Popen(['pythonw', 'start.py'])
    page.status_label.setText('App is running: ')
    page.isOn = True

# completed
def stop_main_process(page):
    print('stopping ...')
    try:
        open('program.txt', 'w+').write('stop')
        page.status_label.setText('App is off: ')
        page.isOn = False
    except:
        print("Error: stopping the process")

# completed
def check_process_running(page):
    try:
        status = open('program.txt', 'r+').read()
        if status == "running":
            page.status_label.setText("App is on: ")
            page.isOn = True
        else:
            page.status_label.setText("App is off: ")
            page.isOn = False
        change_button_text(page)
    except:
        print("Error: checking process status")
