# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PersonalNotes.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_Open_Folder = QAction(MainWindow)
        self.action_Open_Folder.setObjectName(u"action_Open_Folder")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, -1, 291, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Add = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        self.pushButton_Add.setIconSize(QSize(24, 24))
        self.pushButton_Add.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_Add)

        self.pushButton_Del = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Del.setObjectName(u"pushButton_Del")
        self.pushButton_Del.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_Del)

        self.pushButton_Up = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Up.setObjectName(u"pushButton_Up")
        self.pushButton_Up.setEnabled(True)
        self.pushButton_Up.setIconSize(QSize(24, 24))
        self.pushButton_Up.setCheckable(False)
        self.pushButton_Up.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_Up)

        self.pushButton_Down = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Down.setObjectName(u"pushButton_Down")
        self.pushButton_Down.setEnabled(True)
        self.pushButton_Down.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_Down)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 60, 291, 471))
        font = QFont()
        font.setBold(True)
        self.listWidget.setFont(font)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(310, 60, 481, 471))
        self.textEdit.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menu_File.addAction(self.action_Open_Folder)

        self.retranslateUi(MainWindow)

        self.pushButton_Up.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Personal Notes", None))
        self.action_Open_Folder.setText(QCoreApplication.translate("MainWindow", u"&Open Folder...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Add.setToolTip(QCoreApplication.translate("MainWindow", u"Add new note", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Add.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_Del.setToolTip(QCoreApplication.translate("MainWindow", u"Delete note", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Del.setText("")
        self.pushButton_Up.setText("")
        self.pushButton_Down.setText("")
#if QT_CONFIG(tooltip)
        self.textEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Click to edit", None))
#endif // QT_CONFIG(tooltip)
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi

