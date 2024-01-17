import json
import sys
import markdown
import os

from datetime import date

from InstallPyQt6 import installPyQt6
installPyQt6()

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    # Global configuration
    config = {}

    # Dictionary with all notes
    notes = {}

    # Current note
    currentNote = {}

    currentNoteNumber = 0

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

        # Disable not used buttons
        self.pushButton_Up.setEnabled(False)
        self.pushButton_Down.setEnabled(False)

        # Slots
        self.ui.listWidget.itemClicked.connect(self.onItemClicked)
        self.ui.pushButton_Add.clicked.connect(self.onButtonAdd)
        self.ui.pushButton_Del.clicked.connect(self.onButtonDel)
        QApplication.instance().focusChanged.connect(self.onFocusChanged)
    

    def readConfig(self):
         # TODO: #1 Was passiert, wenn die Config nicht gefunden wird?
         with open('./config.json', 'r') as f:
            self.config = json.load(f)


    def openNotes(self):
         file_name = self.config['NotesFolder'] + self.config['NotesFilename'] 
         # TODO: #2 Was passiert, wenn die Datei nicht gefunden wird?
         with open(file_name, 'r') as f:
            self.notes = json.load(f)


    def saveNotes(self):
        file_name = self.config['NotesFolder'] + self.config['NotesFilename']
        with open(file_name, 'w') as f:
            json.dump(self.notes, f)


    def refreshList(self):
        itemList = []
        for i in range(len(self.notes['item'])):
            itemList.append(self.notes['item'][i]['name'])

        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(itemList)


    def setCurrentNote(self, itemNumber):
        self.currentNote = self.notes['item'][itemNumber]
        self.displayContent(self.currentNote['note'])


    def displayContent(self, file):
        fullFileName = self.config['NotesFolder'] + file
        with open(fullFileName, 'r') as f:
            self.content = f.read()

        # Convert Markdown into HTML
        contentHTML = markdown.markdown(self.content)

        self.ui.textEdit.setHtml(contentHTML)
        self.ui.textEdit.setReadOnly(True)


    def onItemClicked(self, item):
        # Number of selected line
        self.currentNoteNumber = self.ui.listWidget.currentRow()
        #print(self.currentNoteNumber)
        self.setCurrentNote(self.currentNoteNumber)


    def onButtonAdd(self):
        # Write the MD file
        self.notes['LastNote'] = self.notes['LastNote'] +1
        file = self.notes['LastNote']
        fullFileName = self.config['NotesFolder'] + str(file) + '.md'
        with open(fullFileName, 'w') as f:
            f.write('')
        # Add a new item into dictionary
        today = date.today()
        newItem ={
            "name": "New note",
            "date": str(today),
            "note": str(file) + '.md'
        }
        self.notes['item'].insert(0, newItem)
        self.saveNotes()
        self.refreshList()


    def onButtonDel(self):
        # Which item is in focus?
        row = self.listWidget.currentRow()
        
        # Delete Markdown file
        fullFileName = self.config['NotesFolder'] + self.currentNote['note']

        if os.path.exists(fullFileName):
            os.remove(fullFileName)
        else:
            # TODO: #41 Replace it with a message box
            print("The file does not exist")
        
        # Delete the item in list
        self.notes['item'].remove(self.notes['item'][row])

        self.saveNotes()
        self.refreshList()


    def onFocusChanged(self, oldWidget, nowWidget):
        if self.ui.textEdit is nowWidget:
            # QTextEdit is in focus
            # TODO: #32 Change the background color

            # Make QTextEdit editable
            self.ui.textEdit.setReadOnly(False)
            self.ui.textEdit.setPlainText(self.content)

        if self.ui.textEdit is oldWidget:
            # QTextEdit is no longer in focus
            # TODO: #32 Change the background color
            
            self.content = self.ui.textEdit.toPlainText()
            
            # Save the file
            fullFileName = self.config['NotesFolder'] + self.currentNote['note']
            with open(fullFileName, 'w') as f:
                f.write(self.content)

            # Display the content as HTML
            self.displayContent(self.currentNote['note'])
            
            # Change the date and move it on the 1st place
            today = date.today()
            newItem = {}
            # Here I have to change the name for the solution to issue #43.
            newItem['name'] = self.currentNote['name']
            ###
            newItem['date'] = str(today)
            newItem['note'] = self.currentNote['note']
            
            self.notes['item'].remove(self.currentNote)
            self.notes['item'].insert(0, newItem)
            self.saveNotes()
            self.refreshList()
                    

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
