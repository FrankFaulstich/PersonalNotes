import json
import sys

from InstallPyQt6 import installPyQt6
installPyQt6()

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    config = {}

    # Dictionary with all notes
    notes = {}

    # Current note
    currentNote = {}

    # Content of current MD file
    content =''

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = uic.loadUi("./PersonalNotes.ui", self)
        self.readConfig()
        self.openNotes()
        self.refreshList()

        # 1st item in the list is the current item
        self.setCurrentNote(0)
        # TODO: #11 The 1st item should be selected in the list.

        # Slots
        self.ui.listWidget.itemClicked.connect(self.onItemClicked)

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

    def setCurrentNote(self, itemNumber):
        self.currentNote = self.notes['item'][itemNumber]
        self.displayContent(self.currentNote['note'])

    def displayContent(self, file):
        fullFileName = self.config['NotesFolder'] + file
        with open(fullFileName, 'r') as f:
            self.content = f.read()

        # TODO: #17 Convert Markdown into HTML
        self.ui.textBrowser.setText(self.content)

    def onItemClicked(self, item):
        # Number of selected line
        self.setCurrentNote(self.ui.listWidget.currentRow())
        

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
