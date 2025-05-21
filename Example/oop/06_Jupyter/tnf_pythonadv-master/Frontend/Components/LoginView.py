from PyQt5.QtWidgets import *

from Core.Api import WebApi

class LoginView(QWidget):
    # void __init__(void* self, void* parent);
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.parentWindow = parent
        
        self.vLayout = QVBoxLayout()
        self.username = QLineEdit('')
        self.password = QLineEdit('')
        self.password.setEchoMode(QLineEdit.Password)
        self.loginBtn = QPushButton('Login')
        self.loginBtn.clicked.connect(self.login)

        self.vLayout.addWidget(self.username)
        self.vLayout.addWidget(self.password)
        self.vLayout.addWidget(self.loginBtn)

        self.setLayout(self.vLayout)

    def login(self):
        username = self.username.text()
        password = self.password.text()

        if username != "" and password != "":
            print(username)
            print(password)
            success = WebApi.login({ 'username' : username, 'password' : password })

            if success:
                print("connected")
            else:
                print("ERROR")
        else:
            print("form error")

