import sys
from PyQt5 import QtWidgets
import sqlite3
import time

# connecting to sqlite3 database and creating table

con = sqlite3.connect('login.db')  # creating connection object
cursor = con.cursor()  # creating cursor object
cursor.execute('create table if not exists people(username text, password text)')  # creating table
con.commit()


class Window(QtWidgets.QWidget):  # creating window class from QWidget
    def __init__(self):  # init func
        super().__init__()  # using QWidget's init values
        self.ui()  # calling ui func which has ui objects

    def ui(self):
        self.setGeometry(1600, 300, 1000, 600)  # setting place and size for the window
        self.setWindowTitle('Welcome to Registering place...')  # setting window title
        self.setStyleSheet('background: lightgray')
        # now its time to work on ui
        # gonna create 2 parts... 1 for register and 1 for logining
        # if u register its gonna save it to database
        # and u can login if u have ut acount on databse
        # im gonna search it by username
        # if username exist the program will chech the username
        self.register_username = QtWidgets.QLineEdit()
        self.register_password = QtWidgets.QLineEdit()
        self.login_username = QtWidgets.QLineEdit()
        self.login_password = QtWidgets.QLineEdit()
        # creating input opjects
        self.register_tag = QtWidgets.QLabel('Register')
        self.register_username_tag = QtWidgets.QLabel('Username: ')
        self.register_password_tag = QtWidgets.QLabel('Password:  ')
        self.login_tag = QtWidgets.QLabel('Login')
        self.login_username_tag = QtWidgets.QLabel('Username: ')
        self.login_password_tag = QtWidgets.QLabel('Password:  ')
        self.register_status = QtWidgets.QLabel('')
        self.login_status = QtWidgets.QLabel('')
        self.register_status.setStyleSheet('color: red')
        self.login_status.setStyleSheet('color: red')
        # creating labels
        self.login_button = QtWidgets.QPushButton('Login')
        self.register_button = QtWidgets.QPushButton('Register')
        self.login_button.setStyleSheet('background: white;'
                                       'color: blue;')
        self.register_button.setStyleSheet('background: white;'
                                          'color: blue;')
        # creating buttons
        h_box1 = QtWidgets.QHBoxLayout()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box3 = QtWidgets.QHBoxLayout()
        h_box4 = QtWidgets.QHBoxLayout()
        h_box5 = QtWidgets.QHBoxLayout()
        # creating horzinontal layouts
        h_box1.addWidget(self.register_username_tag)
        h_box1.addWidget(self.register_username)  # usinh horizontal boxes
        h_box1.addStretch()
        h_box2.addWidget(self.register_password_tag)
        h_box2.addWidget(self.register_password)
        h_box2.addStretch()
        h_box3.addWidget(self.login_username_tag)
        h_box3.addWidget(self.login_username)
        h_box3.addStretch()
        h_box4.addWidget(self.login_password_tag)
        h_box4.addWidget(self.login_password)
        h_box4.addStretch()
        v_box1 = QtWidgets.QVBoxLayout()
        v_box1.addWidget(self.register_tag)
        v_box1.addLayout(h_box1)
        v_box1.addLayout(h_box2)
        v_box1.addWidget(self.register_button)  # adding h_box's to v_boxs
        v_box1.addWidget(self.register_status)
        v_box1.addStretch()
        v_box2 = QtWidgets.QVBoxLayout()
        v_box2.addWidget(self.login_tag)
        v_box2.addLayout(h_box3)
        v_box2.addLayout(h_box4)
        v_box2.addWidget(self.login_button)
        v_box2.addWidget(self.login_status)
        v_box2.addStretch()
        h_box5.addLayout(v_box1)
        h_box5.addStretch()  # and finally adding all of them to final 1 h_box
        h_box5.addLayout(v_box2)
        self.setLayout(h_box5)
        self.register_button.clicked.connect(self.click)
        self.login_button.clicked.connect(self.click)  # connecting buttons to func
        self.show()

    def click(self):
        sender = self.sender()  # getting info of the sender
        if sender.text() == 'Register':
            try:
                if len(self.register_username.text()) == 0 or len(self.register_password.text()) == 0: #control
                    raise ValueError
                else:
                    cursor.execute('insert into people values(?,?)',
                                   (self.register_username.text(), self.register_password.text())) #inserting values to database
                    con.commit()
                    self.register_status.setText('Registering successful...')
                    self.register_username.clear() #clearing input boxes
                    self.register_password.clear()
            except:
                self.register_status.setText('There is a problem!')
                self.register_username.clear()
                self.register_password.clear()
        else:
            try:
                cursor.execute('select * from people where username = ?', (self.login_username.text(),))
                username_password = cursor.fetchall() #getting info of spesific username and commiting them to a list
                password = username_password[0][1]
                if self.login_password.text() == password:
                    self.login_status.setText('Successful to Login...')
                    self.login_password.clear()
                    self.login_username.clear()
                else:
                    self.login_status.setText('Wrong Password...')
                    self.login_password.clear()
                    self.login_username.clear()
            except:
                self.login_status.setText('There is a problem!')
                self.login_password.clear()
                self.login_username.clear()
app = QtWidgets.QApplication(sys.argv)#creating application
window = Window() #calling __init__ func
sys.exit((app.exec_())) 
