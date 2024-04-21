# Form implementation generated from reading ui file '/Users/frankfaulstich/git/PersonalNotes/PersonalNotes.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 170, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Add = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_Add.setText("")
        self.pushButton_Add.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_Add.setFlat(True)
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.horizontalLayout.addWidget(self.pushButton_Add)
        self.pushButton_Del = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_Del.setText("")
        self.pushButton_Del.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_Del.setFlat(True)
        self.pushButton_Del.setObjectName("pushButton_Del")
        self.horizontalLayout.addWidget(self.pushButton_Del)
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 291, 491))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(310, 40, 481, 491))
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByKeyboard|QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextBrowserInteraction|QtCore.Qt.TextInteractionFlag.TextEditable|QtCore.Qt.TextInteractionFlag.TextEditorInteraction|QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(620, 0, 170, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Mail = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.pushButton_Mail.setText("")
        self.pushButton_Mail.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_Mail.setFlat(True)
        self.pushButton_Mail.setObjectName("pushButton_Mail")
        self.horizontalLayout_2.addWidget(self.pushButton_Mail)
        self.pushButton_Copy = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.pushButton_Copy.setText("")
        self.pushButton_Copy.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_Copy.setFlat(True)
        self.pushButton_Copy.setObjectName("pushButton_Copy")
        self.horizontalLayout_2.addWidget(self.pushButton_Copy)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(parent=self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Info = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Info.setObjectName("menu_Info")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open_Folder = QtGui.QAction(parent=MainWindow)
        self.action_Open_Folder.setObjectName("action_Open_Folder")
        self.action_save_as_MD = QtGui.QAction(parent=MainWindow)
        self.action_save_as_MD.setObjectName("action_save_as_MD")
        self.action_save_as_HTML = QtGui.QAction(parent=MainWindow)
        self.action_save_as_HTML.setObjectName("action_save_as_HTML")
        self.action_save_as_ODT = QtGui.QAction(parent=MainWindow)
        self.action_save_as_ODT.setObjectName("action_save_as_ODT")
        self.action_save_as_DOCX = QtGui.QAction(parent=MainWindow)
        self.action_save_as_DOCX.setObjectName("action_save_as_DOCX")
        self.action_Exit = QtGui.QAction(parent=MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_About = QtGui.QAction(parent=MainWindow)
        self.action_About.setObjectName("action_About")
        self.menu_File.addAction(self.action_Open_Folder)
        self.menu_File.addAction(self.action_save_as_MD)
        self.menu_File.addAction(self.action_save_as_HTML)
        self.menu_File.addAction(self.action_save_as_ODT)
        self.menu_File.addAction(self.action_save_as_DOCX)
        self.menu_File.addAction(self.action_Exit)
        self.menu_Info.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Info.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Notes"))
        self.pushButton_Add.setToolTip(_translate("MainWindow", "Add new note"))
        self.pushButton_Del.setToolTip(_translate("MainWindow", "Delete note"))
        self.textEdit.setToolTip(_translate("MainWindow", "Click to edit"))
        self.pushButton_Mail.setToolTip(_translate("MainWindow", "Mail"))
        self.pushButton_Copy.setToolTip(_translate("MainWindow", "Copy in Clipboard"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Info.setTitle(_translate("MainWindow", "Info"))
        self.action_Open_Folder.setText(_translate("MainWindow", "&Open Folder..."))
        self.action_save_as_MD.setText(_translate("MainWindow", "Save as &Markdown..."))
        self.action_save_as_HTML.setText(_translate("MainWindow", "Save as &HTML..."))
        self.action_save_as_ODT.setText(_translate("MainWindow", "Save as &ODT..."))
        self.action_save_as_DOCX.setText(_translate("MainWindow", "Save as &DOCX..."))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_About.setText(_translate("MainWindow", "About..."))
