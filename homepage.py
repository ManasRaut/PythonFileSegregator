# GUI File
from PyQt5 import QtWidgets, QtGui
import widgets as wd
import events
import threading
import time
import monitor
import organize

class Home_page(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.isOn = False
        events.read_target_folder(self)
        thread = threading.Thread(target=lambda: self.check_status(self.status_label), daemon=True).start()
        
    def check_status(self, label):
        while True:
            events.check_process_running(self)
            time.sleep(2)        

    def initUI(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(8, 8, 8, 8)
        self.layout.setSpacing(8)
    
        # title 
        self.title = QtWidgets.QLabel("Home")
        self.title.setMaximumHeight(50)
        self.title.setProperty("cssClass", "bigFont")

        self.frame_1 = QtWidgets.QFrame(self)
        self.layout_1 = QtWidgets.QHBoxLayout(self.frame_1)
        self.layout_1.setContentsMargins(0, 0, 0, 0)
        self.layout_1.setSpacing(4)
        self.status_label = QtWidgets.QLabel("App is Off: ")
        self.start_stop_btn = QtWidgets.QPushButton(self)
        self.start_stop_btn.setText("Start")
        self.start_stop_btn.setProperty('cssClass', 'special_btn')
        self.start_stop_btn.setFixedSize(70, 30)

        self.frame_2 = QtWidgets.QFrame(self)
        self.layout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.layout_2.setContentsMargins(0, 0, 0, 0)
        self.layout_2.setSpacing(4)
        self.label_2 = QtWidgets.QLabel("Run App once: ")
        self.organize_btn = QtWidgets.QPushButton(self)
        self.organize_btn.setText("Organize")
        self.organize_btn.setProperty('cssClass', 'special_btn')
        self.organize_btn.setFixedSize(70, 30)

        self.frame_3 = QtWidgets.QFrame(self)
        self.layout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.layout_3.setContentsMargins(0, 0, 0, 0)
        self.layout_3.setSpacing(4)
        self.label_3 = QtWidgets.QLabel("Downloads Folder: ")
        self.target_folder_field = QtWidgets.QLineEdit(self)
        self.target_folder_field.setFixedSize(300, 30)
        self.browse_folder_btn = QtWidgets.QPushButton(self)
        self.browse_folder_btn.setText('Select')
        self.browse_folder_btn.setProperty('cssClass', 'special_btn')
        self.browse_folder_btn.setFixedSize(70, 30)
        
        h_spacer_1 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        # add layout
        self.layout.addWidget(self.title)
        self.layout.addWidget(wd.Seperator())
        self.layout.addWidget(self.frame_1)
        self.layout.addWidget(self.frame_2)
        self.layout.addWidget(self.frame_3)
        self.layout_1.addWidget(self.status_label)
        self.layout_1.addWidget(self.start_stop_btn)
        self.layout_1.addItem(h_spacer_1)
        self.layout_2.addWidget(self.label_2)
        self.layout_2.addWidget(self.organize_btn)
        self.layout_2.addItem(h_spacer_1)
        self.layout_3.addWidget(self.label_3)
        self.layout_3.addWidget(self.target_folder_field)
        self.layout_3.addWidget(self.browse_folder_btn)
        self.layout_3.addItem(h_spacer_1)
        self.layout.addWidget(QtWidgets.QFrame())

        self.start_stop_btn.clicked.connect(lambda: events.toggle_app(self))
        self.organize_btn.clicked.connect(self.organize)
        self.browse_folder_btn.clicked.connect(lambda: events.save_target_folder(self))
    
    def organize(self):
        organize.one_time_sort()