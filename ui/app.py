import sys
from PyQt5.QtWidgets import QApplication,QDialog,QLineEdit,QPushButton,QStyleFactory,QMainWindow,QWidget
from PyQt5.uic import loadUi
import sqlite3
from datetime import datetime
from ui.function import *

Db = sqlite3.connect('database.sql', check_same_thread=False)
cursor = Db.cursor()
class edit(QWidget):
    def __init__(self):
        super(edit ,self).__init__()
        loadUi('editstudent.ui', self)






class user(QMainWindow):
    Db = sqlite3.connect('database.sql', check_same_thread=False)
    cursor = Db.cursor()
    def __init__(self):
        super(user, self).__init__()
        loadUi('untitled.ui',self)
        self.btnhandle()
        self.loaddetails()
        self.w = edit()

    def btnhandle(self):
        self.editbtn.clicked.connect(self.showedit)


    def showedit(self):
        self.w.show()


    def loaddetails(self):
        sql = f"""select * from users where username = 'tess'"""
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
        self.w = user()


    def buttonhandle(self):
        self.showpassword.clicked.connect(self.showpass)
        self.regbtn.clicked.connect(self.register)
        self.loginbtn.clicked.connect(self.log)

    def showpass(self):
        if self.txtpassword.echoMode()== 0:
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
            elif len(password)<5:
                msg = 'Password too short'
            elif password != confirm:
                msg = 'Password Mismatch'
            else:
                # password = ci.encrypt(password)
                password = sa.encrypt(password)
                sql = f""" INSERT INTO users (fullname, username, password, email, usertype, regDate) values ('{fullname}','{username}',"{password}",'{email}','{usertype}','{now}')"""
                self.cursor.execute(sql)
                self.Db.commit()


        except Exception as err:
            msg = str(err)

        self.msgbox.setText(msg)



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
                msg = 'your logged in'
                self.w.show()
                self.hide()

            else:
                msg = 'your password is incorrect'
        except Exception as err:
           msg =  str(err)

        self.msg1.setText(msg)
        return username


app = QApplication(sys.argv)
win = login()
print(QStyleFactory.keys())
sys.exit(app.exec_())