from PyQt6.QtWidgets import QMessageBox

class Error:
    """Display a error

    Display a error dialog.
    """
    
    def __init__(self, text) -> None:
        s = '<p>Error</p>'
        s = s + '<p>' + text + '</p> '
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Error')
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.setText(s)
        msgBox.exec()

