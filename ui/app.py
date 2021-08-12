import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QStyleFactory, QMainWindow, QWidget
from PyQt5.uic import loadUi
import sqlite3
from datetime import datetime
from PyQt5 import *
from PyQt5.QtCore import QTimer
from ui.function import *

Db = sqlite3.connect('database.sql', check_same_thread=False)
cursor = Db.cursor()


class edit(QWidget):
    def __init__(self):
        super(edit, self).__init__()
        loadUi('editstudent.ui', self)
        self.value = 0
        self.showdetails()
        self.buttonhandler()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.progress)

    def buttonhandler(self):
        self.regbtn.clicked.connect(self.updateuser)

    def progress(self):
        self.value = self.value + 5
        if self.value <= 100:
            self.progressBar.setValue(self.value)
            self.lblmsg.setText('updating....')
        else:
            self.timer.stop()
            self.lblmsg.setText('')
            self.progressBar.setValue(0)
            self.value = 0
            self.close()

    def showdetails(self):
        sql = f"""select * from users where username = '{self.username}'"""
        result = cursor.execute(sql).fetchall()[0]
        self.txtfullname.setText(result[1])
        self.txtusername.setText(result[2])
        self.txtfaculty.setText(result[7])
        self.txtdepartment.setText(result[8])
        self.txtemail.setText(result[4])

    def updateuser(self):
        fullname = self.txtfullname.text()
        username = self.txtusername.text()
        faculty = self.txtfaculty.text()
        department = self.txtdepartment.text()
        email = self.txtemail.text()

        array = [fullname, faculty, department]

        try:
            if checkempty(array):
                msg = 'please fill all available fields!'
            else:
                sql = f"""Update users set fullname = '{fullname}',faculty = '{faculty}',department = '{department}' where username = '{self.username}'"""
                cursor.execute(sql)
                Db.commit()
                print('successful')
                self.timer.start(50)
                cleartext([self.txtfullname, self.txtfaculty, self.txtdepartment])
        except Exception as err:
            print(err)


class user(QMainWindow):
    Db = sqlite3.connect('database.sql', check_same_thread=False)
    cursor = Db.cursor()

    def __init__(self):
        super(user, self).__init__()
        loadUi('untitled.ui', self)
        self.btnhandle()
        self.loaddetails()
        self.w = ''

    def btnhandle(self):
        self.editbtn.clicked.connect(self.showedit)

    def showedit(self):
        edit.username = self.username
        self.w = edit()
        self.w.show()

    def loaddetails(self):
        sql = f"""select * from users where username = '{self.username}'"""
        result = self.cursor.execute(sql).fetchall()[0]

        print(result[1])
        self.txtname.setText(result[1])
        self.txtusername.setText(result[2])
        self.txtemail.setText(result[4])
        self.txtphoneno.setText(result[5])
        self.txtfaculty.setText(result[1])
        self.txtdepartment.setText(result[1])


class login(QDialog):
    Db = sqlite3.connect('database.sql', check_same_thread=False)
    cursor = Db.cursor()

    def __init__(self):
        super(login, self).__init__()
        loadUi('login.ui', self)

        self.setWindowTitle('login form')
        self.showpass()
        self.show()
        self.buttonhandle()
        self.w = ''

    def buttonhandle(self):
        self.showpassword.clicked.connect(self.showpass)
        self.regbtn.clicked.connect(self.register)
        self.loginbtn.clicked.connect(self.log)

    def showpass(self):
        if self.txtpassword.echoMode() == 0:
            self.txtpassword.setEchoMode(2)
        else:
            self.txtpassword.setEchoMode(0)

    def register(self):
        print('hello')
        try:
            fullname = self.txtfullname.text()
            username = self.txtusername.text()
            password = self.txtpassword.text()
            confirm = self.txtconfirmpasswod.text()
            email = self.txtemail.text()
            # print(email)
            usertype = self.cmbusertype.currentText()
            now = datetime.now()

            if not fullname or not username or not password or not confirm or not email:
                msg = "You need to fill all the fields"
            elif len(password) < 5:
                msg = 'Password too short'
            elif password != confirm:
                msg = 'Password Mismatch'
            else:
                # password = ci.encrypt(password)
                password = sa.encrypt(password)
                sql = f""" INSERT INTO users (fullname, username, password, email, usertype, regDate) values ('{fullname}','{username}','{password}','{email}','{usertype}','{now}')"""
                self.cursor.execute(sql)
                self.Db.commit()



        except Exception as err:
            msg = str(err)


    def log(self):
        username = self.loginusername.text()
        password = self.loginpassword.text()
        sql = f"""SELECT password FROM users where username is '{username}'"""

        result = self.cursor.execute(sql).fetchone()
        print(result)

        try:
            if not username or not password:
                msg = 'imcomplete fields fill all fields!'
            elif not result:
                msg = 'incorrect password'
            # elif ci.verify(password, result[0]):
            elif sa.verify(password, result[0]):
                user.username= username
                msg = 'your logged in'
                self.w = user()
                self.w.show()
                self.hide()

            else:
                msg = 'your password is incorrect'
        except Exception as err:
            msg = str(err)

        self.msg1.setText(msg)
        return username


app = QApplication(sys.argv)
win = login()
print(QStyleFactory.keys())
sys.exit(app.exec_())
