import json
import sys
import markdown
import os
import pyperclip
import subprocess

from datetime import date

from InstallPyQt6 import installPyQt6
installPyQt6()

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QIcon

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
        self.setCurrentNote(0)

        # Add icons to buttons
        self.ui.pushButton_Add.setIcon(QIcon('./icons/add.svg'))
        self.ui.pushButton_Del.setIcon(QIcon('./icons/del.svg'))
        self.ui.pushButton_Copy.setIcon(QIcon('./icons/copy.svg'))
        self.ui.pushButton_Mail.setIcon(QIcon('./icons/mail.svg'))

        # Slots
        self.ui.action_Open_Folder.triggered.connect(self.onOpenFolder)
        self.ui.listWidget.itemClicked.connect(self.onItemClicked)
        self.ui.pushButton_Add.clicked.connect(self.onButtonAdd)
        self.ui.pushButton_Del.clicked.connect(self.onButtonDel)
        self.ui.pushButton_Copy.clicked.connect(self.onButtonCopy)
        self.ui.pushButton_Mail.clicked.connect(self.onButtonMail)
        QApplication.instance().focusChanged.connect(self.onFocusChanged)
    

    def readConfig(self):
        try:
            with open('./config.json', 'r') as f:
                self.config = json.load(f)
        except:
            self.config = {
                                "NotesFolder": "./Notes/",
                                "NotesFilename": "notes.json",
                                "CommentFolder": "./Comments/",
                                "ChecklistFolder": "./Checklists/",
                                "PictureFolder": "./Pictures/"
            }
             
            self.saveConfig()


    def saveConfig(self):
        with open('./config.json', 'w') as f:
            json.dump(self.config, f)


    def openNotes(self):
        file_name = self.config['NotesFolder'] + self.config['NotesFilename'] 
        try:
            with open(file_name, 'r') as f:
                self.notes = json.load(f)

                # No creation date in file
                
                for i in range(len(self.notes['item'])):
                    item = self.notes['item'][i]
               
                    if not 'date_creation' in item:
                        # Add key 'date_creation' to the dictionary
                        self.notes['item'][i]['date_creation'] = self.notes['item'][i]['date']
                
        except:
            # TODO: #64  Replace it with a message box
            print('Notes file not found. A new file is created.')
            self.notes = {
                            "LastNoteID": 1,
                            "LastNote": 1,
                            "LastComment": 1,
                            "LastChecklist": 1,
                            "item": []
            }

            self.saveNotes()


    def saveNotes(self):
        file_name = self.config['NotesFolder'] + self.config['NotesFilename']
        with open(file_name, 'w') as f:
            json.dump(self.notes, f)


    def refreshList(self):
        itemList = []
        for i in range(len(self.notes['item'])):
            s = self.notes['item'][i]['name']
            if s[0] == '#':
                s = s.lstrip('#')
                s = s.lstrip()

            if len(s) > 40:
                s = s[:40] + ' ...\n'

            s = s + self.notes['item'][i]['date'] + '\n'
            itemList.append(s)

        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(itemList)
        self.ui.listWidget.setCurrentRow(0)


    def setCurrentNote(self, itemNumber):
        self.currentNote = self.notes['item'][itemNumber]
        self.displayContent(self.currentNote['note'])


    def displayContent(self, file):
        fullFileName = self.config['NotesFolder'] + file
        # TODO #65 Error handling if the Markdown file not found
        with open(fullFileName, 'r') as f:
            self.content = f.read()

        # Convert Markdown into HTML
        contentHTML = markdown.markdown(self.content)

        self.ui.textEdit.setHtml(contentHTML)
        self.ui.textEdit.setReadOnly(True)


    def onOpenFolder(self):
        # Menu item "Open Folder"
        directory = QFileDialog.getExistingDirectory(self, "Open Folder")
        self.config['NotesFolder'] = directory + '/'
        
        self.saveConfig()
        self.openNotes()
        self.refreshList()
        self.setCurrentNote(0)


    def onItemClicked(self, item):
        # Number of selected line
        self.currentNoteNumber = self.ui.listWidget.currentRow()
        self.setCurrentNote(self.currentNoteNumber)


    def onButtonAdd(self):
        self.ui.listWidget.setFocus()
        # Write the MD file
        self.notes['LastNote'] = self.notes['LastNote'] +1
        file = self.notes['LastNote']
        fullFileName = self.config['NotesFolder'] + str(file) + '.md'
        with open(fullFileName, 'w') as f:
            f.write('')
        # Add a new item into dictionary
        today = date.today()
        newItem ={
            "name": "New Note\n",
            "date": str(today),
            "note": str(file) + '.md'
        }
        self.notes['item'].insert(0, newItem)
        self.saveNotes()
        self.refreshList()


    def onButtonDel(self):
        self.ui.listWidget.setFocus()
        # Which item is in focus?
        row = self.listWidget.currentRow()
        
        # Delete Markdown file
        fullFileName = self.config['NotesFolder'] + self.currentNote['note']

        if os.path.exists(fullFileName):
            os.remove(fullFileName)
        else:
            # TODO: #41 Replace it with a message box
            print("The file does not exist.")
        
        # Delete the item in list
        self.notes['item'].remove(self.notes['item'][row])

        self.saveNotes()
        self.refreshList()
        self.setCurrentNote(0)
        self.ui.textEdit.setReadOnly(True)


    def onButtonCopy(self):
        pyperclip.copy(self.content)


    def onButtonMail(self):
        address = 'email@example.com'
        l = self.content.splitlines(True)
        if len(l) > 0:
            subject = l[0]
        else:
            subject = 'New Item\n'

        if subject[0] == '#':
            subject = subject.lstrip('#')
            subject = subject.lstrip()

        body = self.content

        if sys.platform == 'darwin':
            # macOS
            subprocess.call(["open", "mailto:" + address + "?subject=" + subject + "&body=" + body])
        else:
            # Windows, Linux
            os.system("start mailto:" + address + "?subject=" + subject + "&body=" + body)


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
            l = self.content.splitlines(True)
            if len(l) > 0:
                name = l[0]
            else:
                name = 'New Item\n'
            
            newItem['name'] = name
            newItem['date'] = str(today)
            newItem['note'] = self.currentNote['note']
            
            del(self.notes['item'][self.currentNoteNumber])
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
