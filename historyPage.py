# GUI File
from PyQt5 import QtWidgets, QtGui
import widgets as wd

class History_page(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.read_lines = 0
        self.initUI()
        self.load_history()
    
    def initUI(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setSpacing(16)
        self.layout.setContentsMargins(8, 8, 8, 8)
    
        # content
        self.title = QtWidgets.QLabel("History")
        self.title.setMaximumHeight(50)
        self.title.setProperty("cssClass", "bigFont")
        self.clearHistoryBtn = QtWidgets.QPushButton(self)
        self.clearHistoryBtn.setText('Clear History')
        self.clearHistoryBtn.setProperty("cssClass", "normalBtn")
        self.clearHistoryBtn.clicked.connect(self.clearHistory)

        # contents
        self.contentFrame = QtWidgets.QFrame(self)
        self.layout_2 = QtWidgets.QVBoxLayout(self.contentFrame)
        self.layout_2.setContentsMargins(0, 0, 0, 0)
        self.layout_2.setSpacing(0)
        self.historyList = wd.ListWidget()
        
        # add layout
        self.layout.addWidget(self.title)
        self.layout.addWidget(wd.Seperator())
        self.layout.addWidget(self.contentFrame)
        self.layout.addWidget(self.historyList)
        self.layout.addWidget(self.clearHistoryBtn)
    
    def showEvent(self, e):
        self.load_history()

    def clearHistory(self):
        file_ = open('history.log', 'w')
        file_.truncate()
        file_.close()
        for i in range(self.historyList.layout.count()):
            self.historyList.layout.itemAt(i).widget().hide()

    def load_history(self):
        file_ = open('history.log', 'r')
        file_.seek(self.read_lines)
        logs = file_.readlines()
        self.read_lines = file_.tell()
        file_.close()
        count = self.historyList.layout.count()
        if count > 0:
            self.historyList.layout.removeItem(self.historyList.layout.itemAt(count -1))
        for line in logs:
            self.historyList.layout.addWidget(wd.HistoryItem(" ".join(line.split()[2:])))
        self.historyList.layout.addWidget(QtWidgets.QFrame())