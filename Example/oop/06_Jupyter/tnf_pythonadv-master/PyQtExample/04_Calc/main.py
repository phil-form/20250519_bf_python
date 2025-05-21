from PyQt5.QtWidgets import *

class BaseWindow(QMainWindow):
    
    def __init__(self):
        super(BaseWindow, self).__init__()
        
        widget = QWidget()
        self.setCentralWidget(widget)
        
        layout = QHBoxLayout()
        widget.setLayout(layout)
        
        self.op1 = QSpinBox()
        self.op2 = QSpinBox()
        
        self.cmBox = QComboBox()
        
        self.eqLabel = QLabel('=')
        
        self.cmBox.addItems(['+', '-', '*', '/'])
        self.result = QLineEdit()
        
        self.button = QPushButton('=')
        
        
        layout.addWidget(self.op1)
        layout.addWidget(self.cmBox)
        layout.addWidget(self.op2)
        layout.addWidget(self.button)
        layout.addWidget(self.result)
        self.button.clicked.connect(self.compute)
        
        self.loop = 0
        self.compute()
        self.loop = 1
    
    def compute(self):
        a = self.op1.value()
        b = self.op2.value()
        
        if(self.cmBox.currentText() == '+'):
            result = a + b      
        elif(self.cmBox.currentText() == '-'):
            result = a - b      
        elif(self.cmBox.currentText() == '*'):
            result = a * b      
        else:
            try:
                result = a / b
            except ZeroDivisionError as e:
                result = "divide by 0!"
                
        self.result.setText(str(result))
                
        
    
app = QApplication([])

wdw = BaseWindow()

wdw.show()
app.exec_()