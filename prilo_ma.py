# from PyQt6 import QtCore,  QtWidgets,   QtGui
# import time
# import sys

from windows.prilo_calendar import *

import sys

app = QtWidgets.QApplication(sys.argv)
Main_cal_Window = QtWidgets.QMainWindow()
ui = Ui_Main_cal_Window()
ui.setupUi(Main_cal_Window)
Main_cal_Window.show()
# ui.label.setText("ldldldl")


def on_click():
    print(ui.plainTextEdit.toPlainText())
    print(ui.dateEdit.dateTime().toString('dd-MM-yyyy '))
    print("clicked!!!")
    # print(ui.calendarWidget.selectedDate().toString('dd-MM-yyyy '))
    # date=QDate(2022, 9,17)
    # ui.calendarWidget.setSelectedDate(date)


def on_click_calendar():
    print(ui.calendarWidget.selectedDate().toString('dd-MM-yyyy '))
    ui.dateEdit.setDate(ui.calendarWidget.selectedDate())

def on_dateedit_change():
    print(ui.dateEdit.dateTime().toString('dd-MM-yyyy '))
    ui.calendarWidget.setSelectedDate(ui.dateEdit.date())


ui.pushButton.clicked.connect(on_click)
ui.calendarWidget.clicked.connect(on_click_calendar)
ui.dateEdit.dateChanged.connect(on_dateedit_change)
sys.exit(app.exec())