from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

def on_click():
    alert = QMessageBox()
    alert.setText('Button clicked!')
    alert.exec_()

layout.addWidget(QLabel('Hello world'))
layout.addWidget(QLabel('This is awesome!'))
button = QPushButton('Useless button!')
button.clicked.connect(on_click)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()