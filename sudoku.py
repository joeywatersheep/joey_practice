import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui()
    def ui(self):
        self.setWindowTitle('Sudoku')
        self.setStyleSheet('background: lightgray')
        self.setGeometry(1600, 300, 0, 0)
        self.a1 = QtWidgets.QLineEdit()
        self.a1.setMaxLength(1)
        self.a2 = QtWidgets.QLineEdit()
        self.a2.setMaxLength(1)
        self.a3 = QtWidgets.QLineEdit()
        self.a3.setMaxLength(1)
        self.a4 = QtWidgets.QLineEdit()
        self.a4.setMaxLength(1)
        self.a5 = QtWidgets.QLineEdit()
        self.a5.setMaxLength(1)
        self.a6 = QtWidgets.QLineEdit()
        self.a6.setMaxLength(1)
        self.a7 = QtWidgets.QLineEdit()
        self.a7.setMaxLength(1)
        self.a8 = QtWidgets.QLineEdit()
        self.a8.setMaxLength(1)
        self.a9 = QtWidgets.QLineEdit()
        self.a9.setMaxLength(1)
        self.clear = QtWidgets.QPushButton('Clear')
        self.commit = QtWidgets.QPushButton('Commit')
        self.text = QtWidgets.QLabel('')
        h_box1 = QtWidgets.QHBoxLayout()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box3 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.a1)
        h_box1.addWidget(self.a2)
        h_box1.addWidget(self.a3)

        h_box2.addWidget(self.a4)
        h_box2.addWidget(self.a5)
        h_box2.addWidget(self.a6)

        h_box3.addWidget(self.a7)
        h_box3.addWidget(self.a8)
        h_box3.addWidget(self.a9)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addWidget(self.clear)
        v_box.addWidget(self.commit)
        v_box.addWidget(self.text)
        self.setLayout(v_box)
        self.clear.clicked.connect(self.button)
        self.commit.clicked.connect(self.button)
        self.show()
    def button(self):
        sender = self.sender()
        if sender.text() == 'Clear':
            self.a1.clear()
            self.a2.clear()
            self.a3.clear()
            self.a4.clear()
            self.a5.clear()
            self.a6.clear()
            self.a7.clear()
            self.a8.clear()
            self.a9.clear()
        elif sender.text() == 'Commit':
            try:
                list1 = [[int(self.a1.text()), int(self.a2.text()), int(self.a3.text())],
                         [int(self.a4.text()), int(self.a5.text()), int(self.a6.text())],
                         [int(self.a7.text()), int(self.a8.text()), int(self.a9.text())]]
            except:
                print('Hata C')
            try:
                if self.main_p(list1):
                    self.text.setText('Correct')
                else:
                    self.text.setText('Wrong')
            except:
                print('Hata D')
    def sorgu(self, a1, a2, a3):
        try:
            if a1 != a2 and a1 != a3 and a2 != a3:
                return True
            else:
                return False
        except:
            print('Hata A')
    def main_p(self, list):
        try:
            list5 = []
            for i in range(3):
                list3 = []
                list4 = []
                for j in range(3):
                    list3.append(list[i][j])
                    list4.append(list[j][i])
                s1 = self.sorgu(list3[0], list3[1], list3[2])
                s2 = self.sorgu(list4[0], list4[1], list4[2])
                list5.append(s1)
                list5.append(s2)
            for i in list5:
                if i:
                    continue
                else:
                    return False
            return True
        except:
            print('Hata B')
app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
