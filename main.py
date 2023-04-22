from PyQt5.QtWidgets import QGridLayout, QWidget, QApplication, QLineEdit, QPushButton, QSizePolicy
from PyQt5.QtGui import QFont
import sys

my_font = QFont('Cooper', 18)

class Strechable_Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.setMinimumSize(40,40)
        self.setFont(my_font)

        self.setStyleSheet(''' 
            QPushButton {
                background-color: #797784;
                color: #d6f1e4;
                border: none;
                border-radius: 15px;
                padding: 10px;
            }
        ''')

class Display(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.setMinimumSize(40,40)
        self.setFont(my_font)
        self.setStyleSheet(''' 
            QLineEdit {
                background-color: #797784;
                color: #d6f1e4;
                border: 2px solid #d6f1e4;
                border-radius: 15px;
                padding: 10px;
            }
        ''')


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.to_solve = ''

        self.display = Display()
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        self.setStyleSheet(''' 
            QWidget {
                background-color: #5b5364;
            }
        ''')

        btn_1 = Strechable_Button('1')
        btn_2 = Strechable_Button('2')
        btn_3 = Strechable_Button('3')
        btn_4 = Strechable_Button('4')
        btn_5 = Strechable_Button('5')
        btn_6 = Strechable_Button('6')
        btn_7 = Strechable_Button('7')
        btn_8 = Strechable_Button('8')
        btn_9 = Strechable_Button('9')
        btn_0 = Strechable_Button('0')
        btn_back = Strechable_Button('🠔')
        btn_add = Strechable_Button('+')
        btn_substruct = Strechable_Button('-')
        btn_divide = Strechable_Button('/')
        btn_multiply = Strechable_Button('*')
        btn_clear = Strechable_Button('c')
        btn_result = Strechable_Button('=')
        btn_point = Strechable_Button('.')

        layout.addWidget(self.display, 0, 0, 1, 4)

        layout.addWidget(btn_back, 1, 0)
        layout.addWidget(btn_clear, 1, 1)
        layout.addWidget(btn_add, 1, 2)
        layout.addWidget(btn_substruct, 1, 3)

        layout.addWidget(btn_7, 2, 0)
        layout.addWidget(btn_8, 2, 1)
        layout.addWidget(btn_9, 2, 2)
        layout.addWidget(btn_multiply, 2, 3)

        layout.addWidget(btn_4, 3, 0)
        layout.addWidget(btn_5, 3, 1)
        layout.addWidget(btn_6, 3, 2)
        layout.addWidget(btn_divide, 3, 3)

        layout.addWidget(btn_1, 4, 0)
        layout.addWidget(btn_2, 4, 1)
        layout.addWidget(btn_3, 4, 2)
        layout.addWidget(btn_result, 4, 3, 2, 1)

        layout.addWidget(btn_0, 5, 0, 1, 2)
        layout.addWidget(btn_point, 5, 2)

        btn_0.clicked.connect(self.btn_handler)
        btn_1.clicked.connect(self.btn_handler)
        btn_2.clicked.connect(self.btn_handler)
        btn_3.clicked.connect(self.btn_handler)
        btn_4.clicked.connect(self.btn_handler)
        btn_5.clicked.connect(self.btn_handler)
        btn_6.clicked.connect(self.btn_handler)
        btn_7.clicked.connect(self.btn_handler)
        btn_8.clicked.connect(self.btn_handler)
        btn_9.clicked.connect(self.btn_handler)
        btn_back.clicked.connect(self.btn_handler)
        btn_clear.clicked.connect(self.btn_handler)
        btn_add.clicked.connect(self.btn_handler)
        btn_substruct.clicked.connect(self.btn_handler)
        btn_multiply.clicked.connect(self.btn_handler)
        btn_divide.clicked.connect(self.btn_handler)
        btn_point.clicked.connect(self.btn_handler)
        btn_result.clicked.connect(self.btn_handler)

    def btn_handler(self):
        if self.to_solve == 'error':
            self.to_solve = ''

        btn = self.sender()
        if btn.text() in '0123456789+-*%.':
            self.to_solve += btn.text()
        if btn.text() == '<-':
            self.to_solve = self.to_solve[0:-1]
        if btn.text() == 'c':
            self.to_solve = ''
        if btn.text() == '=':
            try:
                self.to_solve = str(eval(self.to_solve))
            except:
                self.to_solve == 'error'
        self.display.setText(self.to_solve)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
