from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Mon super titre!")
        self.setFixedHeight(600)
        self.setFixedWidth(800)

        self.label_1 = QLabel("Beautiful label!")
        self.label_1.resize(150, 50)
        self.label_2 = QLabel("Other label")
        self.label_2.resize(150, 50)

        self.v_layout = QHBoxLayout(self)
        self.v_layout.addWidget(self.label_1)
        self.v_layout.addWidget(self.label_2)

        self.label_1.setStyleSheet("border: 3px solid black")
        self.label_2.setStyleSheet("border: 3px solid gold")

        self.show()


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())