from PyQt5.QtWidgets import *
from test import Ui_MainWindow
from widgetForm import Ui_Form
from widgetTest2 import Ui_Form as Ui_Form2
import psycopg2

import sys

from mysql.connector import (connection)

def setupWidget(widget):
    print(testTextForm.toPlainText())
    testTextForm.setText("COUCOU")
    try:
        cnx = psycopg2.connect(dbname="app", user="app", password="1234", host="127.0.0.1", port="5435")
        # cnx = connection.MySQLConnection(user='root', password='password',
        #                              host='127.0.0.1',
        #                              database='dbslide')
        cursor = cnx.cursor()

        query = ("SELECT goalid, goalreference FROM goals")

        cursor.execute(query)
        
        dbid, ref  = cursor.fetchone()
        testTextForm.setText(ref)
        form.lineEdit.setText(ref)
        # for c in cursor:
        #     print(c)
        
        cursor.close()
        cnx.close()
    except:
        print("EXCEPTION")

def resetData(asdasda):
    form.lineEdit.clear()
    form.lineEdit_2.clear()
    form.lineEdit_3.clear()
    form.lineEdit_4.clear()

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.actionasdasd.triggered.connect(setupWidget)

Form = QWidget()
form = Ui_Form()
form.setupUi(Form)
ui.tab_2.layout = QVBoxLayout(ui.tab_2)
ui.tab_2.layout.addWidget(Form)
form.pushButton.clicked.connect(setupWidget)
form.pushButton_2.clicked.connect(resetData)

Form2 = QWidget()
form2 = Ui_Form2()
form2.setupUi(Form2)
testTextForm = form2.textBrowser
ui.tab.layout = QVBoxLayout(ui.tab)
ui.tab.layout.addWidget(Form2)

ui.tab_2
MainWindow.show()
sys.exit(app.exec_())

dict = {}

def registerEvent(eventName):
    dict[eventName] = []

def registerCallback(eventName, callback):
    dict[eventName].append(callback)

def triggerEvent(eventName):
    for callback in dict[eventName]:
        callback()

def event1():
    print("COUCOU")