from PyQt6.QtWidgets import QMessageBox

class About:
    
    def __init__(self, version) -> None:
        s = '<p>Persional Notes Version ' + version +  '</p>'
        s = s + '<p>More Information:</p> '
        s = s + '<a href=\"https://github.com/FrankFaulstich/PersonalNotes\">https://github.com/FrankFaulstich/PersonalNotes</a></p>'
        msgBox = QMessageBox()
        msgBox.setText(s)
        msgBox.exec()

