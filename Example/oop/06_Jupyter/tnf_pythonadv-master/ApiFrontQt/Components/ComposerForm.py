from PyQt5.QtWidgets import *
from Core.server import webApi

class ComposerFormView(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.parentWindow = parent

        self.__id = 0
        self.lastname = QLineEdit('')
        self.firstname = QLineEdit('')
        self.btnSubmit = QPushButton('Submit')
        self.btnSubmit.clicked.connect(self.submit)
        self.errorLabel = QLabel('')
        self.edit = False

        vLayout = QVBoxLayout()
        vLayout.addWidget(self.lastname)
        vLayout.addWidget(self.firstname)
        vLayout.addWidget(self.btnSubmit)
        vLayout.addWidget(self.errorLabel)
        
        self.setLayout(vLayout)
        
    def editComposer(self, composer):
        self.firstname.setText(composer['firstname'])
        self.firstname.setEnabled()
        self.lastname.setText(composer['lastname'])
        self.__id = composer['id']
        self.edit = True
        
    def submit(self):
        lname = self.lastname.text()
        fname = self.firstname.text()
        method = 'PUT' if self.edit else 'POST'
        
        # if self.edit:
        #     method = 'PUT'
        # else:
        #     method = 'POST'

        url = 'composers/'+ str(self.__id) if self.edit else 'composers/add/'

        # if self.edit:
        #     url = 'composers/'+ str(self.__id)
        # else:
        #     url = 'composers/add/'

        if lname != "" and fname != "":
            success = webApi.getData(url=url, 
                                    data={ 'lastname': lname, 'firstname': fname },
                                    method=method)
            if success:
                self.edit = False
                self.lastname.setText('')
                self.firstname.setText('')
                #print(webApi.getData('composers'))
                self.parentWindow.updateComposerTable()
            else:
                self.errorLabel.setText('Wrong username or password!')                
        else:
            self.errorLabel.setText('Username and password reuqired!')
            
