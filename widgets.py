# GUI File
from PyQt5 import QtWidgets, QtCore, QtGui
from styles import *
import events

class ExtensionPageItem(QtWidgets.QFrame):
    def __init__(self, **kwargs):
        super().__init__()
        self.initUI(kwargs)

    def initUI(self, dic):
        self.setMaximumSize(600, 160)
        self.resize(600, 40)
        self.setProperty("cssClass", "listItem")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(8, 8, 8, 8)

        self.nameLabel = QtWidgets.QLabel(dic['name'])

        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setMaximumHeight(80)
        self.layout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.layout_2.setSpacing(0)
        self.layout_2.setContentsMargins(0, 0, 0, 0)

        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setMaximumWidth(400)
        self.layout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.layout_3.setSpacing(8)
        self.layout_3.setContentsMargins(8, 8, 8, 8)
        self.label_1 = QtWidgets.QLabel('Folder name: ')
        self.folder_name_field = QtWidgets.QLineEdit(self.frame_3)
        self.folder_name_field.setText(dic['destination_folder'])
        self.folder_browse_btn = QtWidgets.QPushButton(self.frame_3)
        self.folder_browse_btn.setText('..')
        self.folder_browse_btn.setMaximumSize(25, 25)
        self.layout_3.addWidget(self.label_1)
        self.layout_3.addWidget(self.folder_name_field)
        self.layout_3.addWidget(self.folder_browse_btn)

        self.frame_4 = QtWidgets.QFrame(self)
        self.frame_4.setMaximumWidth(400)
        self.layout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.layout_4.setSpacing(8)
        self.layout_4.setContentsMargins(8, 8, 8, 8)
        self.label_2 = QtWidgets.QLabel('Destination folder: ')
        self.dest_name_field = QtWidgets.QLineEdit(self.frame_4)
        self.dest_name_field.setText(dic['destination_folder'])
        self.dest_browse_btn = QtWidgets.QPushButton(self.frame_4)
        self.dest_browse_btn.setText('..')
        self.dest_browse_btn.setMaximumSize(25, 25)
        self.layout_4.addWidget(self.label_2)
        self.layout_4.addWidget(self.dest_name_field)
        self.layout_4.addWidget(self.dest_browse_btn)

        self.frame_5 = QtWidgets.QFrame(self)
        self.layout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.layout_5.setSpacing(2)
        self.layout_5.setContentsMargins(8, 8, 8, 8)
        self.toggleSwitch = ToggleSwitch(self)
        self.statusLabel = QtWidgets.QLabel('On: ')
        self.statusLabel.setMaximumWidth(50)
        self.layout_5.addWidget(self.statusLabel)
        self.layout_5.addWidget(self.toggleSwitch)
        self.layout_5.addWidget(QtWidgets.QFrame())

        self.layout_2.addWidget(self.frame_3)
        self.layout_2.addWidget(self.frame_4)
        self.layout.addWidget(self.nameLabel)
        self.layout.addWidget(self.frame_2)
        self.layout.addWidget(self.frame_5)

# complete
class ToggleSwitch(QtWidgets.QFrame):
    def __init__(self, parent = None):
        super().__init__()
        self.parent = parent
        self.isON = True
        self.onstyle = '''
        *[cssClass="switchBody"] {
        background-color: white;
        border: 1px solid rgb(150, 150, 150);
        border-radius: 13px;}
        *[cssClass="switchButton"] {
        border: 1px solid rgb(235, 235, 235);
        border-radius: 10px;
        background-color: rgb(0, 153, 204);}'''
        self.offstyle = '''
        *[cssClass="switchBody"] {
        background-color: white;
        border: 1px solid rgb(150, 150, 150);
        border-radius: 13px;}
        *[cssClass="switchButton"] {
        border: 1px solid rgb(235, 235, 235);
        border-radius: 10px;
        background-color: lightgrey;}'''
        self.initUI()

    def initUI(self):
        self.setFixedSize(60 ,26)
        self.setProperty("cssClass", "switchBody")
        self.setStyleSheet(self.onstyle)
        self.switchButton = QtWidgets.QPushButton(self)
        self.switchButton.setFixedSize(QtCore.QSize(20, 20))
        self.switchButton.setText("  ")
        self.switchButton.setGeometry(QtCore.QRect(35, 3, 20, 20))
        self.switchButton.setProperty("cssClass", "switchButton")
        self.switchButton.clicked.connect(self.toggled)

    def toggled(self):
        self.animate()
   
    def animate(self):
        self.animation = QtCore.QPropertyAnimation(self.switchButton, b"geometry")
        if not self.isON:
            self.animation.setStartValue(QtCore.QRect(5, 3, 20, 20))
            self.animation.setEndValue(QtCore.QRect(35, 3, 20, 20))
            self.setStyleSheet(self.onstyle)
        else:
            self.animation.setStartValue(QtCore.QRect(35, 3, 20, 20))
            self.animation.setEndValue(QtCore.QRect(5, 3, 20, 20))
            
            self.setStyleSheet(self.offstyle)
        self.isON = not self.isON
        self.animation.setDuration(500)
        self.animation.start()

# complete
class ListWidget(QtWidgets.QScrollArea):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.frame = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.frame)
        self.layout.setSpacing(4)
        self.layout.setContentsMargins(8, 8, 8, 8)
        self.setWidgetResizable(True)
        self.setWidget(self.frame)

# complete
class Seperator(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(2)
        self.setMinimumHeight(2)
        self.setStyleSheet("background-color: rgb(156,164,180);margin-left5px;")

# complete
class HistoryItem(QtWidgets.QFrame):
    def __init__(self, t):
        super().__init__()
        self.text = t
        self.initUI()
    def initUI(self):
        self.setProperty("cssClass", "listItem")
        self.setMaximumHeight(50)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(16, 16, 16, 16)
        self.label = QtWidgets.QLabel(self)
        self.label.setText(self.text)
        self.layout.addWidget(self.label)

# complete
class CustomItem(QtWidgets.QFrame):
    def __init__(self, data, page):
        super().__init__()
        self.initUI(data)
        self.data = data
        self.page = page

    def initUI(self, data):
        self.setFixedHeight(60)
        self.setProperty("cssClass", "listItem")
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setSpacing(8)
        self.layout.setContentsMargins(8, 8, 8, 8)

        k = ''
        for keyword in data['keywords']: k += keyword + ' '

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText("Keywords: " + k)
        self.toggleSwitch = ToggleSwitch(self)
        self.delete_button = QtWidgets.QPushButton(self)
        self.delete_button.setText("x")
        self.delete_button.setFixedSize(20, 20)
        self.delete_button.setProperty("cssClass", "deleteItemBtn")

        self.layout.addWidget(self.label_1)
        self.layout.addWidget(self.toggleSwitch)
        self.layout.addWidget(self.delete_button)

        self.toggleSwitch.switchButton.clicked.connect(self.disable_setting)
        self.delete_button.clicked.connect(self.delete_setting)
    
    def disable_setting(self):
        if self.page.selected_setting == self.data :
            self.page.clear_fields()
        events.disable_custom_setting(self.page, self)
    
    def delete_setting(self):
        self.page.clear_fields()
        events.delete_custom_setting(self.page, self)
    
    def mousePressEvent(self, event):
        self.page.selected_setting = self.data
        k = ''
        for keyword in self.data['keywords']: k += keyword + ' '
        self.page.keywords_text_field.setPlainText(k)
        self.page.folder_text_field.setText(self.data['folder_name'])
        self.page.dest_text_field.setText(self.data['path'])