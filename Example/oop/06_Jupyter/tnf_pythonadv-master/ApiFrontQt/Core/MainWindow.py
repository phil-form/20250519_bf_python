from PyQt5.QtWidgets import *
from Components.LoginView import LoginView
from Components.TableView import ApiTableWidget
from Components.ComposerForm import ComposerFormView

class MainWindow(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs) -> None:
        super().__init__(parent=parent)
        self.__loginLayout = LoginView(parent=self)
        self.__initComposerView()
        self.setLoginLayout()
        
    def setLoginLayout(self):
        self.setCentralWidget(self.__loginLayout)
        
    def setComposerTableView(self):
        self.setCentralWidget(self.__composersWidget)
        self.resize(800, 600)
        
    def __initComposerView(self):
        self.__composersView = ApiTableWidget(parent=self, url='composers/')
        self.__composersWidget = QWidget()
        self.__composerLayout = QVBoxLayout() #from HBox
        self.__composerFormView = ComposerFormView(parent=self)

        self.__composerLayout.addWidget(self.__composerFormView)
        self.__composerLayout.addWidget(self.__composersView)
        self.__composersWidget.setLayout(self.__composerLayout)
        
    def updateComposerTable(self):
        self.__composersView.updateDataFromDb()
        
    def editComposer(self, composer):
        self.__composerFormView.editComposer(composer)