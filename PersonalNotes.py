import json
import sys

from InstallPyQt6 import installPyQt6
installPyQt6()

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    config = {}
    notes = {}

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = uic.loadUi("./PersonalNotes.ui", self)
        self.readConfig()
        self.openNotes()
        self.refreshList()

    def readConfig(self):
         # TODO: #1 Was passiert, wenn die Config nicht gefunden wird?
         with open('./config.json', 'r') as f:
            self.config = json.load(f)

    def openNotes(self):
         file_name = self.config['NotesFolder'] + self.config['NotesFilename'] 
         # TODO: #2 Was passiert, wenn die Datei nicht gefunden wird?
         with open(file_name, 'r') as f:
            self.notes = json.load(f)

    def refreshList(self):
        itemList = []
        for i in range(len(self.notes['item'])):
            itemList.append( self.notes['item'][i]['name'])

        self.ui.listWidget.addItems(itemList)
        

def window():
    app = QApplication(sys.argv)
    with open('./styles.qss', 'r') as f:
        style = f.read()
        app.setStyleSheet(style)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
	window()
