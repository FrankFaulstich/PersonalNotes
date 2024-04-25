from PyQt6.QtWidgets import QMessageBox

class Messagebox:

    def __init__(self):
        pass


    def warning(text):
        s = '<p>Warning</p>'
        s = s + '<p>' + text + '</p> '
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Warning')
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.setText(s)
        msgBox.exec()

    def error(text):
        s = '<p>Error</p>'
        s = s + '<p>' + text + '</p> '
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Error')
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.setText(s)
        msgBox.exec()

    def decision(text):
        s = '<p>Decision</p>'
        s = s + '<p>' + text + '</p> '
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Decision')
        msgBox.setIcon(msgBox.Icon.Question)
        msgBox.setText(s)

        msgBox.addButton(msgBox.StandardButton.Yes)
        msgBox.addButton(msgBox.StandardButton.No)
        msgBox.addButton(msgBox.StandardButton.Cancel)

        msgBox.setDefaultButton(msgBox.StandardButton.Yes)

        response = msgBox.exec()

        if response == msgBox.StandardButton.Yes:
            print('Yes')
            r = 1
        elif response == msgBox.StandardButton.No:
            print('No')
            r = 2
        else:
            print('Cancel')
            r = 0
        
        return r