# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(650, 550)
        SecondWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 460, 140, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(153, 227, 113);\n"
"border-color: rgb(9, 9, 9);\n"
"border-width: thick;\n"
"border-radius:20px;")
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 460, 140, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(153, 227, 113);\n"
"border-color: rgb(9, 9, 9);\n"
"border-width: thick;\n"
"border-radius:20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 460, 140, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(153, 227, 113);\n"
"border-color: rgb(9, 9, 9);\n"
"border-width: thick;\n"
"border-radius:20px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 10, 140, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(153, 227, 113);\n"
"border-color: rgb(9, 9, 9);\n"
"border-width: thick;\n"
"border-radius:20px;\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 26))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(parent=SecondWindow)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=SecondWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=SecondWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtGui.QAction(parent=SecondWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtGui.QAction(parent=SecondWindow)
        self.action_6.setObjectName("action_6")
        self.menu_2.addAction(self.action_6)
        self.menu_2.addSeparator()
        self.menu.addSeparator()
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.pushButton.setText(_translate("SecondWindow", "О авторе"))
        self.pushButton_2.setText(_translate("SecondWindow", "О программе"))
        self.pushButton_3.setText(_translate("SecondWindow", "НАЗАД"))
        self.pushButton_4.setText(_translate("SecondWindow", "Ошибка программы"))
        self.menu_2.setTitle(_translate("SecondWindow", "Вид"))
        self.menu.setTitle(_translate("SecondWindow", "Файл"))
        self.action.setText(_translate("SecondWindow", "Сохранить"))
        self.action_2.setText(_translate("SecondWindow", "Открыть"))
        self.action_3.setText(_translate("SecondWindow", "."))
        self.action_5.setText(_translate("SecondWindow", "Выйти из программы"))
        self.action_6.setText(_translate("SecondWindow", "Настройки"))

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     SecondWindow = QtWidgets.QMainWindow()
#     ui = Ui_SecondWindow()
#     ui.setupUi(SecondWindow)
#     SecondWindow.show()
#     sys.exit(app.exec())
