from PyQt5.QtWidgets import *
from Core.server import webApi

class LoginView(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.parentWindow = parent
        self.username = QLineEdit('')
        self.password = QLineEdit('')
        self.password.setEchoMode(QLineEdit.Password)
        self.btnLogin = QPushButton('Login')
        self.btnLogin.clicked.connect(self.login)
        self.errorLabel = QLabel('')

        vLayout = QVBoxLayout()
        vLayout.addWidget(self.username)
        vLayout.addWidget(self.password)
        vLayout.addWidget(self.btnLogin)
        vLayout.addWidget(self.errorLabel)
        
        self.setLayout(vLayout)
        
    def login(self):
        uname = self.username.text()
        pword = self.password.text()
        if uname != "" and pword != "":
            print(uname)
            print(pword)
            success = webApi.login('auth/token/', { 'username': uname, 'password': pword })
            if success:
                #print(webApi.getData('composers'))
                self.parentWindow.setComposerTableView()
            else:
                self.errorLabel.setText('Wrong username or password!')                
        else:
            self.errorLabel.setText('Username and password reuqired!')
