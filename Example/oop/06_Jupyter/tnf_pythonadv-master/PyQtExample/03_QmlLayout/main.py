from PyQt5.QtCore import QDateTime, Qt, QTime
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

Form, Window = uic.loadUiType('dialog.ui')

app = QApplication(sys.argv)
window = Window()
form = Form()

form.setupUi(window)
window.show()
app.exec_()
