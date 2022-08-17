# GUI File
from PyQt5 import QtWidgets, QtGui
import widgets as wd
import events

class Basic_page(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings_list = list()
        self.selected_setting = None
        events.read_extension_settings(self)
    
    def initUI(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(16, 16, 16, 16)
        self.layout.setSpacing(16)
    
        # title 
        self.title = QtWidgets.QLabel("Basic Settings")
        self.title.setMaximumHeight(50)
        self.title.setProperty("cssClass", "bigFont")

        # sort by extension
        self.label1 = QtWidgets.QLabel("Sort by file type")
        self.label1.setMaximumHeight(20)
        self.h_spacer_1 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.frame_1 = QtWidgets.QFrame(self)
        self.layout_1 = QtWidgets.QHBoxLayout(self.frame_1)
        self.layout_1.setSpacing(10)
        self.layout_1.setContentsMargins(0, 0, 0, 0)
        self.dropDown = QtWidgets.QComboBox(self)
        self.label_2 = QtWidgets.QLabel('Select file type: ')
        items = ['None', 'images', 'music', 'documents', 'videos', 'executables']
        self.dropDown.addItems(items)
        self.dropDown.setMinimumWidth(200)
        self.layout_1.addWidget(self.label_2)
        self.layout_1.addWidget(self.dropDown)
        self.layout_1.addItem(self.h_spacer_1)

        self.frame_2 = QtWidgets.QFrame(self)
        self.layout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.layout_2.setSpacing(10)
        self.layout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QtWidgets.QLabel('Folder name: ')
        self.folder_text_field = QtWidgets.QLineEdit(self.frame_2)
        self.layout_2.addWidget(self.label_3)
        self.layout_2.addWidget(self.folder_text_field)
        self.layout_2.addItem(self.h_spacer_1)

        self.frame_3 = QtWidgets.QFrame(self)
        self.layout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.layout_3.setSpacing(10)
        self.layout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QtWidgets.QLabel('Destination folder: ')
        self.dest_text_field = QtWidgets.QLineEdit(self.frame_3)
        self.browse_folder_btn = QtWidgets.QPushButton(self)
        self.browse_folder_btn.setText('Select')
        self.browse_folder_btn.setProperty('cssClass', 'special_btn')
        self.browse_folder_btn.setFixedSize(70, 30)
        self.layout_3.addWidget(self.label_4)
        self.layout_3.addWidget(self.dest_text_field)
        self.layout_3.addWidget(self.browse_folder_btn)
        self.layout_3.addItem(self.h_spacer_1)

        self.frame_4 = QtWidgets.QFrame(self)
        self.layout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.layout_4.setSpacing(10)
        self.layout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QtWidgets.QLabel('On : ')
        self.toggle_button = wd.ToggleSwitch(self)
        self.layout_4.addWidget(self.label_5)
        self.layout_4.addWidget(self.toggle_button)
        self.layout_4.addItem(self.h_spacer_1)

        self.saveButton = QtWidgets.QPushButton(self)
        self.saveButton.setText("Save")
        self.saveButton.setFixedSize(100, 35)
        self.saveButton.setProperty("cssClass", "normalBtn")

        # add layout
        self.layout.addWidget(self.title)
        self.layout.addWidget(wd.Seperator())
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.frame_1)
        self.layout.addWidget(self.frame_2)
        self.layout.addWidget(self.frame_3)
        self.layout.addWidget(self.frame_4)
        self.layout.addWidget(self.saveButton)
        self.v_spacer_1 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout.addItem(self.v_spacer_1)

        self.dropDown.currentIndexChanged.connect(lambda: events.extension_dropDown_selected(self, self.dropDown))
        self.saveButton.clicked.connect(lambda: events.extension_save_clicked(self))
        self.browse_folder_btn.clicked.connect(lambda: self.dest_text_field.setText(str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Downloads Folder'))))
    
    def clear_fields(self):
        self.folder_text_field.setText('')
        self.dest_text_field.setText('')
        self.selected_setting = None
        self.dropDown.setCurrentIndex(0)
        if not self.toggle_button.isON:
            self.toggle_button.toggled()