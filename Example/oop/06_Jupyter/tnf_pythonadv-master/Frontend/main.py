import sys
from PyQt5.QtWidgets import *
from Core.MainWindow import MainWindow

app = QApplication(sys.argv)

mainWindow = MainWindow()

sys.exit(app.exec_())