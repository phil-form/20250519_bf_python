from PyQt5.QtWidgets import *

from Components.LoginView import LoginView

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.__loginLayout = LoginView(parent=self)
        self.loginViewActive()

        self.show()

    def loginViewActive(self):
        self.setCentralWidget(self.__loginLayout)