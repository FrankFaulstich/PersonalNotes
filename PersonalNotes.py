import json
import sys

from InstallPyQt5 import installPyQt5
installPyQt5()

# TODO: #3 Umstellung auf PyQt6
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    config = {}
    notes = {}

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = uic.loadUi("./PersonalNotes.ui", self)
        self.readConfig()
        self.openNotes()

    def readConfig(self):
         # TODO: #1 Was passiert, wenn die Config nicht gefunden wird?
         with open('./config.json', 'r') as f:
            self.config = json.load(f)
            #print(self.config)

    def openNotes(self):
         file_name = self.config['NotesFolder'] + self.config['NotesFilename'] 
         #print(file_name)
         # TODO: #2 Was passiert, wenn die Datei nicht gefunden wird?
         with open(file_name, 'r') as f:
            self.notes = json.load(f)
            #print(self.notes)
    

def window():
    app = QApplication(sys.argv)
    with open('./styles.qss', 'r') as f:
        style = f.read()
        app.setStyleSheet(style)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
	window()
