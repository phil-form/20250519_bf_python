import sys
from PyQt5.QtGui import QTextBlock
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Core.server import webApi
from PyQt5.QtWidgets import *
from Components.LoginView import LoginView
from Components.TableView import ApiTableWidget
from Core.MainWindow import MainWindow

# ls -l /bin
# argv ['ls', '-l', '/bin']
app = QApplication(sys.argv)

mainWindow = MainWindow()


# mainLayout = LoginView(parent=mainWindow)
# testLayout = QHBoxLayout()
# table = ApiTableWidget(parent=mainWindow, url='composers')
# testLayout.addWidget(table)
# testWdg = QWidget()
# testWdg.setLayout(testLayout)
# mainWindow.setCentralWidget(testWdg)
mainWindow.show()
 
sys.exit(app.exec_())