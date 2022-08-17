# GUI File
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import events as e
from homepage import Home_page
from basicPage import Basic_page
from custompage import Custom_page
from historyPage import History_page
from styles import *
import widgets as wd

class Ui(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Segregator | Dashboard")
        self.resize(QtCore.QSize(900, 650))
        self.setMinimumSize(900, 600)
        self.setStyleSheet(window_style)
        self.initUI()

    def initUI(self):
        # central widget
        self.centralWidget = QtWidgets.QWidget()
        self.mainLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        # navbar and its VLayout
        self.navbar = QtWidgets.QFrame(self.centralWidget)
        self.navbar.setMinimumWidth(200)
        self.navlayout = QtWidgets.QVBoxLayout(self.navbar)
        self.navlayout.setSpacing(0)
        self.navlayout.setContentsMargins(0, 0, 0, 0)
        self.navbar.setProperty("cssClass", "navBar")
        # navbar buttons
        self.home_button = QtWidgets.QPushButton(self.navbar)
        self.home_button.setMaximumHeight(50)
        self.home_button.setText("Home")
        self.home_button.setObjectName("home")
        self.home_button.setProperty("cssClass", "navButton")
        self.basic_button = QtWidgets.QPushButton(self.navbar)
        self.basic_button.setMaximumHeight(50)
        self.basic_button.setText("Basic")
        self.basic_button.setObjectName("basic")
        self.basic_button.setProperty("cssClass", "navButton")
        self.custom_button = QtWidgets.QPushButton(self.navbar)
        self.custom_button.setMaximumHeight(50)
        self.custom_button.setText("Custom")
        self.custom_button.setObjectName("custom")
        self.custom_button.setProperty("cssClass", "navButton")
        self.history_button = QtWidgets.QPushButton(self.navbar)
        self.history_button.setMaximumHeight(50)
        self.history_button.setText("History")
        self.history_button.setObjectName("history")
        self.history_button.setProperty("cssClass", "navButton")

        self.navlayout.addWidget(self.home_button)
        self.navlayout.addWidget(wd.Seperator())
        self.navlayout.addWidget(self.basic_button)
        self.navlayout.addWidget(wd.Seperator())
        self.navlayout.addWidget(self.custom_button)
        self.navlayout.addWidget(wd.Seperator())
        self.navlayout.addWidget(self.history_button)
        self.navlayout.addWidget(QtWidgets.QFrame())

        # stackwidget
        self.stackWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackWidget.setStyleSheet("")

        # main page
        self.home_page = Home_page()

        # basic page
        self.basic_page = Basic_page()
        
        # custom settings page
        self.custom_page = Custom_page()

        # history page
        self.historyPage = History_page()

        # add all frames and widgets to central widget
        self.stackWidget.addWidget(self.home_page)
        self.stackWidget.addWidget(self.basic_page)
        self.stackWidget.addWidget(self.custom_page)
        self.stackWidget.addWidget(self.historyPage)
        self.mainLayout.addWidget(self.navbar)
        self.mainLayout.addWidget(self.stackWidget)
        self.setCentralWidget(self.centralWidget)

        # add events
        self.home_button.clicked.connect(lambda: e.navbar_clicked(self.home_button, self.stackWidget))
        self.basic_button.clicked.connect(lambda: e.navbar_clicked(self.basic_button, self.stackWidget))
        self.custom_button.clicked.connect(lambda: e.navbar_clicked(self.custom_button, self.stackWidget))
        self.history_button.clicked.connect(lambda: e.navbar_clicked(self.history_button, self.stackWidget))

if __name__ == "__main__":
    app = 0
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())