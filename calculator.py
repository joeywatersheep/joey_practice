import sys
import math
import time
from functools import reduce
from PyQt5 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.ui()
    def ui(self):

        self.isToplama = False
        self.isCarpma = False
        self.isBolme = False
        self.isCikarma = False
        self.isUs = False
        self.isDivisors = False
        self.isisPrime = False
        self.isEbob = False
        self.isEkok = False
        self.isAsalBulma = False
        self.isKok = False
        self.isKal = False
        self.isfaktor = False

        self.setWindowTitle('Calculator')
        self.setGeometry(1600, 300, 300, 300)
        self.setStyleSheet('background: lightgray')

        self.input_area = QtWidgets.QLineEdit()
        self.input_area.setStyleSheet('background: white;'
                                      'color: blue')
        self.input_area.setReadOnly(True)
        self.input_area.setAlignment(QtCore.Qt.AlignRight)

        font = self.input_area.font()
        font.setPointSize(font.pointSize() + 8)
        self.input_area.setFont(font)

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

        self.buttonpi = QtWidgets.QPushButton('π')
        self.buttonpi.setStyleSheet('color: purple')

        self.buttonClear = QtWidgets.QPushButton('C')
        self.buttonClear.setStyleSheet('color: red')

        self.buttonPlus = QtWidgets.QPushButton('+')
        self.buttonPlus.setStyleSheet('color: red')

        self.buttonEquals = QtWidgets.QPushButton('=')
        self.buttonEquals.setStyleSheet('color: red')

        self.buttonMinus = QtWidgets.QPushButton('-')
        self.buttonMinus.setStyleSheet('color: red')

        self.buttonCarp = QtWidgets.QPushButton('x')
        self.buttonCarp.setStyleSheet('color: red')

        self.buttonBol = QtWidgets.QPushButton('÷')
        self.buttonBol.setStyleSheet('color: red')

        self.buttonUs = QtWidgets.QPushButton('xʸ')
        self.buttonUs.setStyleSheet('color: red')

        self.buttonKal = QtWidgets.QPushButton('%')
        self.buttonKal.setStyleSheet('color: red')

        self.buttonCarpanBulma = QtWidgets.QPushButton('Find Divisors')
        self.buttonCarpanBulma.setStyleSheet('color: green')

        self.buttonPrime = QtWidgets.QPushButton('Is Prime?')
        self.buttonPrime.setStyleSheet('color: green')

        self.buttonDot = QtWidgets.QPushButton('.')
        self.buttonDot.setStyleSheet('color: green')

        self.buttonPN = QtWidgets.QPushButton('+/-')
        self.buttonPN.setStyleSheet('color: green')

        self.buttonEbob = QtWidgets.QPushButton('EBOB')
        self.buttonEbob.setStyleSheet('color: blue')

        self.buttonEKOK = QtWidgets.QPushButton('EKOK')
        self.buttonEKOK.setStyleSheet('color: blue')

        self.buttonPrimeDiv = QtWidgets.QPushButton('Prime Div')
        self.buttonPrimeDiv.setStyleSheet('color: blue')

        self.buttonkok = QtWidgets.QPushButton('√')
        self.buttonkok.setStyleSheet('color: blue')

        self.buttonFaktoriel = QtWidgets.QPushButton('x!')
        self.buttonFaktoriel.setStyleSheet('color: purple')

        h_box1 = QtWidgets.QHBoxLayout()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box3 = QtWidgets.QHBoxLayout()
        h_box4 = QtWidgets.QHBoxLayout()
        h_box5 = QtWidgets.QHBoxLayout()
        h_box6 = QtWidgets.QHBoxLayout()
        h_box7 = QtWidgets.QHBoxLayout()

        v_box1 = QtWidgets.QVBoxLayout()
        v_box2 = QtWidgets.QVBoxLayout()
        v_box3 = QtWidgets.QVBoxLayout()
        v_box4 = QtWidgets.QVBoxLayout()
        v_box5 = QtWidgets.QVBoxLayout()
        v_box6 = QtWidgets.QVBoxLayout()

        v_box1.addStretch()
        v_box1.addWidget(self.button1)
        v_box1.addWidget(self.button4)
        v_box1.addWidget(self.button7)
        v_box1.addStretch()

        v_box2.addStretch()
        v_box2.addWidget(self.button2)
        v_box2.addWidget(self.button5)
        v_box2.addWidget(self.button8)
        v_box2.addStretch()

        v_box3.addStretch()
        v_box3.addWidget(self.button3)
        v_box3.addWidget(self.button6)
        v_box3.addWidget(self.button9)
        v_box3.addStretch()

        v_box5.addStretch()
        v_box5.addWidget(self.buttonClear)
        v_box5.addWidget(self.buttonEquals)
        v_box5.addWidget(self.buttonPlus)
        v_box5.addWidget(self.buttonMinus)
        v_box5.addStretch()

        h_box2.addStretch()
        h_box2.addWidget(self.button0)
        h_box2.addStretch()

        h_box1.addStretch()
        h_box1.addLayout(v_box1)
        h_box1.addLayout(v_box2)
        h_box1.addLayout(v_box3)
        h_box1.addStretch()

        v_box4.addStretch()
        v_box4.addLayout(h_box1)
        v_box4.addLayout(h_box2)
        v_box4.addStretch()

        h_box3.addStretch()
        h_box3.addLayout(v_box4)
        h_box3.addLayout(v_box5)
        h_box3.addStretch()

        h_box4.addStretch()
        h_box4.addWidget(self.buttonUs)
        h_box4.addWidget(self.buttonKal)
        h_box4.addWidget(self.buttonCarp)
        h_box4.addWidget(self.buttonBol)
        h_box4.addStretch()

        h_box5.addStretch()
        h_box5.addWidget(self.buttonPN)
        h_box5.addWidget(self.buttonDot)
        h_box5.addWidget(self.buttonPrime)
        h_box5.addWidget(self.buttonCarpanBulma)
        h_box5.addStretch()

        h_box6.addStretch()
        h_box6.addWidget(self.buttonEbob)
        h_box6.addWidget(self.buttonEKOK)
        h_box6.addWidget(self.buttonPrimeDiv)
        h_box6.addWidget(self.buttonkok)
        h_box6.addStretch()

        h_box7.addStretch()
        h_box7.addWidget(self.buttonpi)
        h_box7.addWidget(self.buttonFaktoriel)
        h_box7.addStretch()

        v_box6.addStretch()
        v_box6.addWidget(self.input_area)
        v_box6.addLayout(h_box3)
        v_box6.addLayout(h_box4)
        v_box6.addLayout(h_box5)
        v_box6.addLayout(h_box6)
        v_box6.addLayout(h_box7)
        v_box6.addStretch()

        self.setLayout(v_box6)

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
        self.buttonMinus.clicked.connect(self.numClicked)
        self.buttonUs.clicked.connect(self.numClicked)
        self.buttonBol.clicked.connect(self.numClicked)
        self.buttonCarp.clicked.connect(self.numClicked)
        self.buttonEquals.clicked.connect(self.numClicked)
        self.buttonCarpanBulma.clicked.connect(self.numClicked)
        self.buttonPrime.clicked.connect(self.numClicked)
        self.buttonDot.clicked.connect(self.numClicked)
        self.buttonPN.clicked.connect(self.numClicked)
        self.buttonEbob.clicked.connect(self.numClicked)
        self.buttonpi.clicked.connect(self.numClicked)
        self.buttonEKOK.clicked.connect(self.numClicked)
        self.buttonPrimeDiv.clicked.connect(self.numClicked)
        self.buttonkok.clicked.connect(self.numClicked)
        self.buttonKal.clicked.connect(self.numClicked)
        self.buttonFaktoriel.clicked.connect(self.numClicked)

        self.show()
    def clear(self):
        self.input_area.clear()
    def carp(self,x,y):
        return x*y
    def kok(self, num1):
        asal = list()
        num = num1
        i = num

        def isPrime(num):
            if num >= 3:
                for i in range(2, num):
                    if num % i == 0:
                        return False
            elif num == 2:
                return True
            else:
                return False
            return True

        if num > 0:
            while i != 1:
                if isPrime(i):
                    if num % i == 0:
                        asal.append(i)
                        num //= i
                        continue
                    else:
                        i -= 1
                else:
                    i -= 1
        dis = 1
        ic = 1
        no_list = []
        for i in asal:
            if i in no_list:
                continue
            else:
                i_num = 0
                for j in asal:
                    if i == j:
                        i_num += 1
                if i_num % 2 == 0:
                    i_num //= 2
                    eklenecek = i ** i_num
                    dis *= eklenecek
                else:
                    i_num2 = i_num - 1
                    i_num2 //= 2
                    ekleneck = i ** i_num2
                    dis *= ekleneck
                    ekleneck2 = i ** (i_num - i_num2 * 2)
                    ic *= ekleneck2
                no_list.append(i)
        toplam = str(dis) + '√' + str(ic)
        return toplam
    def PrimeDiv(self, num1):
        list1 = list()
        num = num1
        i = num
        def isPrime(num):
            if num >= 3:
                for i in range(2, num):
                    if num % i == 0:
                        return False
            elif num == 2:
                return True
            else:
                return False
            return True
        if num > 0:
            while i != 1:
                if isPrime(i):
                    if num % i == 0:
                        list1.append(i)
                        num //= i
                        continue
                    else:
                        i -= 1
                else:
                    i -= 1
        toplam = str()
        sayi = 0
        for i in list1:
            if sayi == len(list1) - 1:
                toplam += str(i)
                continue
            else:
                toplam += str(i) + 'x'
                sayi += 1
        return toplam
    def Ekok(self, num1, num2):
        list1 = list()
        num = num1
        i = num
        def isPrime(num):
            if num >= 3:
                for i in range(2, num):
                    if num % i == 0:
                        return False
            elif num == 2:
                return True
            else:
                return False
            return True
        if num > 0:
            while i != 1:
                if isPrime(i):
                    if num % i == 0:
                        list1.append(i)
                        num //= i
                        continue
                    else:
                        i -= 1
                else:
                    i -= 1
        list2 = list()
        num = num2
        i = num
        def isPrime(num):
            if num >= 3:
                for i in range(2, num):
                    if num % i == 0:
                        return False
            elif num == 2:
                return True
            else:
                return False
            return True
        if num > 0:
            while i != 1:
                if isPrime(i):
                    if num % i == 0:
                        list2.append(i)
                        num //= i
                        continue
                    else:
                        i -= 1
                else:
                    i -= 1
        toplam_list = list()
        nolist = []
        a = 0
        for i in list1:
            if i in nolist:
                continue
            else:
                if i == a:
                    continue
                else:
                    list1num = 0
                    list2num = 0
                    for b in list1:
                        if b == i:
                            list1num += 1
                    for b in list2:
                        if b == i:
                            list2num += 1
                    if list1num > list2num:
                        for j in range(1, list1num + 1):
                            toplam_list.append(i)
                    elif list2num > list1num:
                        for j in range(1, list2num + 1):
                            toplam_list.append(i)
                    elif list2num == list1num:
                        for j in range(1, list2num + 1):
                            toplam_list.append(i)
                    nolist.append(i)
                a = i
        a = 0
        for i in list2:
            if i in nolist:
                continue
            else:
                if i == a:
                    continue
                else:
                    list1num = 0
                    list2num = 0
                    for b in list1:
                        if b == i:
                            list1num += 1
                    for b in list2:
                        if b == i:
                            list2num += 1
                    if list1num > list2num:
                        for j in range(1, list1num + 1):
                            toplam_list.append(i)
                    elif list2num > list1num:
                        for j in range(1, list2num + 1):
                            toplam_list.append(i)
                    elif list2num == list1num:
                        for j in range(1, list2num + 1):
                            toplam_list.append(i)
                    nolist.append(i)
                a = i
        return reduce(self.carp, toplam_list)
    def divisorFinder(self, num):
        liste = list()
        for i in range(1, int(num + 1)):
            if num % i == 0:
                liste.append(i)
        deger = str()
        sayi = 0
        for i in liste:
            if sayi == len(liste) - 1:
                deger += str(i)
            else:
                deger += str(i) + ', '
                sayi += 1
        return deger
    def isPrime(self, num):
        for i in range(2, int(num)):
            if num % i == 0:
                return 'Not Prime'
        if num == 1 or num <= 0:
            return 'Not Prime'
        else:
            return 'Prime'
    def ebob(self, num1, num2):
        liste1 = list()
        for i in range(1, int(num1 + 1)):
            if num1 % i == 0:
                liste1.append(i)
        liste2 = list()
        for i in range(1, int(num2 + 1)):
            if num2 % i == 0:
                liste2.append(i)
        liste3 = list()
        for i in liste1:
            for j in liste2:
                if i == j:
                    liste3.append(i)
        return max(liste3)
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

        elif sender.text() == 'π':
            self.a = self.input_area.text()
            self.a += str(math.pi)
            self.input_area.setText(self.a)

        elif sender.text() == '+/-':
            try:
                self.a = float(self.input_area.text())
                self.a *= -1
                self.input_area.setText(str(self.a))
            except:
                self.input_area.setText('A Problem Showed Up')

        elif sender.text() == '+':
            try:
                self.num1 = float(self.input_area.text())
                self.input_area.clear()
                self.isToplama = True
            except:
                self.input_area.setText('Enter a Number...')

        elif sender.text() == '=':
            try:
                if self.isToplama:
                    self.num2 = float(self.input_area.text())
                    self.input_area.clear()
                    self.input_area.setText(str(self.num1 + self.num2))
                    self.isToplama = False
                elif self.isCikarma:
                    self.num2 = float(self.input_area.text())
                    self.input_area.clear()
                    self.input_area.setText(str(self.num1 - self.num2))
                    self.isCikarma = False
                elif self.isEbob:
                    self.num2 = float(self.input_area.text())
                    self.input_area.clear()
                    self.input_area.setText(str(self.ebob(self.num1, self.num2)))
                    self.isEbob = False
                elif self.isBolme:
                    self.num2 = float(self.input_area.text())
                    self.input_area.clear()
                    self.input_area.setText(str(self.num1 / self.num2))
                    self.isBolme = False
                elif self.isCarpma:
                    self.num2 = float(self.input_area.text())
                    self.input_area.clear()
                    self.input_area.setText(str(self.num1 * self.num2))
                    self.isCarpma = False
                elif self.isUs:
                    self.num2 = float(self.input_area.text())
                    self.input_area.clear()
                    self.input_area.setText(str(self.num1 ** self.num2))
                    self.isUs = False
                elif self.isDivisors:
                    self.input_area.setText(str(self.divisorFinder(self.num1)))
                    self.isDivisors = False
                elif self.isisPrime:
                    self.input_area.setText(self.isPrime(self.num1))
                    self.isisPrime = False
                elif self.isEkok:
                    self.num2 = float(self.input_area.text())
                    self.input_area.clear()
                    self.input_area.setText(str(self.Ekok(int(self.num1), int(self.num2))))
                    self.isEkok = False
                elif self.isAsalBulma:
                    self.input_area.setText(str(self.PrimeDiv(int(self.num1))))
                    self.isAsalBulma = False
                elif self.isKok:
                    self.input_area.setText(str(self.kok(int(self.num1))))
                    self.isKok = False
                elif self.isKal:
                    self.num2 = float(self.input_area.text())
                    self.input_area.setText(str(self.num1 % self.num2))
                    self.isKal = False
                elif self.isfaktor:
                    self.input_area.setText(str(float(math.factorial(int(self.num1)))))
                    self.isfaktor = False
            except:
                self.input_area.setText('A Problem Showed Up')
        elif sender.text() == 'x':
            try:
                self.num1 = float(self.input_area.text())
                self.input_area.clear()
                self.isCarpma = True
            except:
                self.input_area.setText('Enter a Number...')
        elif sender.text() == '-':
            try:
                self.num1 = float(self.input_area.text())
                self.input_area.clear()
                self.isCikarma = True
            except:
                self.input_area.setText('Enter a Number...')
        elif sender.text() == '÷':
            try:
                self.num1 = float(self.input_area.text())
                self.input_area.clear()
                self.isBolme = True
            except:
                self.input_area.setText('Enter a Number...')
        elif sender.text() == 'xʸ':
            try:
                self.num1 = float(self.input_area.text())
                self.input_area.clear()
                self.isUs = True
            except:
                self.input_area.setText('Enter a Number...')
        elif sender.text() == 'Find Divisors':
            try:
                self.num1 = float(self.input_area.text())
                self.input_area.clear()
                self.input_area.setText('Enter Equal Sign')
                self.isDivisors = True
            except:
                self.input_area.setText('A Problem Showed Up')
        elif sender.text() == '.':
            self.a = self.input_area.text()
            self.a += '.'
            self.input_area.setText(self.a)
        elif sender.text() == 'Is Prime?':
            try:
                self.num1 = float(self.input_area.text())
                self.input_area.clear()
                self.input_area.setText('Enter Equal Sign')
                self.isisPrime = True
            except:
                self.input_area.setText('A Prob lem Showed Up')
        elif sender.text() == 'EBOB':
            try:
                self.num1 = float(self.input_area.text())
                self.input_area.clear()
                self.isEbob  = True
            except:
                self.input_area.setText('A Problem Showed Up')
        elif sender.text() == 'EKOK':
            try:
                self.num1 = float(self.input_area.text())
                self.input_area.clear()
                self.isEkok = True
            except:
                self.input_area.setText('A Problem Showed Up')
        elif sender.text() == 'Prime Div':
            try:
                self.num1 = float(self.input_area.text())
                self.clear()
                self.input_area.setText('Enter Equal Sign')
                self.isAsalBulma = True
            except:
                self.input_area.setText('A Problem Showed Up')
        elif sender.text() == '√':
            try:
                self.num1 = float(self.input_area.text())
                self.clear()
                self.input_area.setText('Enter Equal Sign')
                self.isKok = True
            except:
                self.input_area.setText('A Problem Showed Up')
        elif sender.text() == '%':
            try:
                self.num1 = float(self.input_area.text())
                self.clear()
                self.isKal = True
            except:
                self.input_area.setText('A Problem Showed Up')
        elif sender.text() == 'x!':
            try:
                self.num1 = float(self.input_area.text())
                self.clear()
                self.input_area.setText('Enter Equal Sign')
                self.isfaktor = True
            except:
                self.input_area.setText('A Problem Showed Up')
app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())



