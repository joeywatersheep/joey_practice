import sys
import math
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui()
    def ui(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(1600, 300, 300, 300)
        self.setStyleSheet('background: lightgray')
        self.input_area = QtWidgets.QLineEdit()
        self.input_area.setStyleSheet('background: white;'
                                      'color: blue')
        self.button1 = QtWidgets.QPushButton('1')
        self.button2 = QtWidgets.QPushButton('2')
        self.button3 = QtWidgets.QPushButton('3')
        self.button4 = QtWidgets.QPushButton('4')
        self.button5 = QtWidgets.QPushButton('5')
        self.button6 = QtWidgets.QPushButton('6')
        self.button7 = QtWidgets.QPushButton('7')
        self.button8 = QtWidgets.QPushButton('8')
        self.button9 = QtWidgets.QPushButton('9')
        self.button0 = QtWidgets.QPushButton('0')
        self.buttonClear = QtWidgets.QPushButton('C')
        self.buttonClear.setStyleSheet('color: red')
        self.buttonPlus = QtWidgets.QPushButton('+')
        self.buttonPlus.setStyleSheet('color: red')
        self.buttonEquals = QtWidgets.QPushButton('=')
        self.buttonEquals.setStyleSheet('color: red')
        h_box1 = QtWidgets.QHBoxLayout()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box3 = QtWidgets.QHBoxLayout()
        h_box4 = QtWidgets.QHBoxLayout()
        h_box5 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.button4)
        h_box3.addWidget(self.button5)
        h_box3.addWidget(self.button6)
        h_box3.addWidget(self.buttonPlus)
        h_box3.addStretch()
        h_box5.addStretch()
        h_box5.addWidget(self.button0)
        h_box5.addStretch()
        h_box4.addStretch()
        h_box4.addWidget(self.button7)
        h_box4.addWidget(self.button8)
        h_box4.addWidget(self.button9)
        h_box4.addWidget(self.buttonEquals)
        h_box4.addStretch()
        h_box1.addStretch()
        h_box1.addWidget(self.button1)
        h_box1.addWidget(self.button2)
        h_box1.addWidget(self.button3)
        h_box1.addWidget(self.buttonClear)
        h_box1.addStretch()
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.input_area)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)
        v_box.addStretch()
        h_box2.addStretch()
        h_box2.addLayout(v_box)
        h_box2.addStretch()
        self.setLayout(h_box2)
        self.buttonClear.clicked.connect(self.clear)
        self.button1.clicked.connect(self.numClicked)
        self.button2.clicked.connect(self.numClicked)
        self.button3.clicked.connect(self.numClicked)
        self.button4.clicked.connect(self.numClicked)
        self.button5.clicked.connect(self.numClicked)
        self.button6.clicked.connect(self.numClicked)
        self.buttonPlus.clicked.connect(self.numClicked)
        self.button7.clicked.connect(self.numClicked)
        self.button8.clicked.connect(self.numClicked)
        self.button9.clicked.connect(self.numClicked)
        self.button0.clicked.connect(self.numClicked)
        self.buttonEquals.clicked.connect(self.numClicked)
        self.show()
    def clear(self):
        self.input_area.clear()
    def numClicked(self):
        sender = self.sender()

        if sender.text() == '1':
            self.a = self.input_area.text()
            self.a += '1'
            self.input_area.setText(self.a)
        elif sender.text() == '2':
            self.a = self.input_area.text()
            self.a += '2'
            self.input_area.setText(self.a)
        elif sender.text() == '3':
            self.a = self.input_area.text()
            self.a += '3'
            self.input_area.setText(self.a)
        elif sender.text() == '4':
            self.a = self.input_area.text()
            self.a += '4'
            self.input_area.setText(self.a)
        elif sender.text() == '5':
            self.a = self.input_area.text()
            self.a += '5'
            self.input_area.setText(self.a)
        elif sender.text() == '6':
            self.a = self.input_area.text()
            self.a += '6'
            self.input_area.setText(self.a)
        elif sender.text() == '7':
            self.a = self.input_area.text()
            self.a += '7'
            self.input_area.setText(self.a)
        elif sender.text() == '8':
            self.a = self.input_area.text()
            self.a += '8'
            self.input_area.setText(self.a)
        elif sender.text() == '9':
            self.a = self.input_area.text()
            self.a += '9'
            self.input_area.setText(self.a)
        elif sender.text() == '0':
            self.a = self.input_area.text()
            self.a += '0'
            self.input_area.setText(self.a)
        elif sender.text() == '+':
            self.num1 = int(self.input_area.text())
            self.input_area.clear()
        elif sender.text() == '=':
            self.num2 = int(self.input_area.text())
            self.input_area.clear()
            self.input_area.setText(str(self.num1 + self.num2))
app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit((app.exec_()))
