from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from Core.server import webApi

class ApiTableWidget(QTableWidget):
    def __init__(self, parent=None, url='', *args, **kwargs):
        super(ApiTableWidget, self).__init__(parent, *args, **kwargs)
        self.parentWindow = parent
        self.__url = url
        self.results = webApi.getData(url)
        self.setRowCount(len(self.results))
        self.itemClicked.connect(self.selectRowAction)
        headers = list(self.results[0].keys())
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)
        self._setupData()
        
    def _setupData(self):
        for resultsIndex, resultsDict in enumerate(self.results):
            for dictIndex, (key, value) in enumerate(resultsDict.items()):
                self.setItem(resultsIndex, dictIndex, QTableWidgetItem(str(value)))
                    
    def filterData(self, key, value):
        self.clear()
        for resultsIndex, resultsDict in enumerate(self.results):
            if(value != "" and resultsDict[key] == value):
                for dictIndex, (key, value) in enumerate(resultsDict.items()):
                    self.setItem(resultsIndex, dictIndex, QTableWidgetItem(str(value)))
    
    def updateDataFromDb(self):
        self.results = webApi.getData(self.__url)
        print(self.results)
        self.setRowCount(len(self.results))
        self.clear()
        self._setupData()
        
    def selectRowAction(self):
        row = self.currentRow()
        self.parentWindow.editComposer(self.results[row])