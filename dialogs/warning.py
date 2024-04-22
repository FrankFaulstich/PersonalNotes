from PyQt6.QtWidgets import QMessageBox

class Warning:
    """Display a warning

    Display a warning dialog.
    """
    
    def __init__(self, text) -> None:
        s = '<p>Warning</p>'
        s = s + '<p>' + text + '</p> '
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Warning')
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.setText(s)
        msgBox.exec()

