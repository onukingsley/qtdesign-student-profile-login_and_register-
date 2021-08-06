import sys, sqlite3  # To bring in the operating system
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QMainWindow, QWidget  # To introduce the Qapplication and QDialog
from PyQt5.uic import loadUi  # is used to run the UI designed
from datetime import datetime

from functions import *

DB = sqlite3.connect('database.sql', check_same_thread=False)
cursor = DB.cursor()

class studentEdit(QWidget):
    def __init__(self):
        super(studentEdit, self).__init__()
        loadUi('ui/studentEditProfile.ui', self)
        # self.show()
        self.w = showtest()
        self.pushButton.clicked.connect(self.showi)

    def showi(self):
        self.w.show()


class showtest(QWidget):
    def __init__(self):
        super(showtest, self).__init__()
        loadUi('ui/test.ui', self)


class User(QMainWindow):
    def __init__(self):
        try:
            super(User, self).__init__()
            loadUi('ui/student.ui', self)
            self.username = 'kosi'
            # self.w = studentEdit()
            self.w = studentEdit()


            self.loadInfo()
            self.buttonHandle()
            self.show()
        except Exception as err:
            print(err)

    def buttonHandle(self):
        self.actionClose.triggered.connect(closeApp)
        self.btnEdit.clicked.connect(self.editProfile)

    def editProfile(self):
        print('hello')
        self.w.show()

    def loadInfo(self):
        sql = f"""SELECT * FROM users WHERE username = '{self.username}'"""
        result = cursor.execute(sql).fetchall()[0]
        self.lblName.setText(result[1])
        self.lblUser.setText(result[2])
        self.lblEmail.setText(result[4])
        self.lblRegDate.setText(result[6])
        print(result[6])
        self.lblPhone.setText(result[7])
        self.lblReg.setText(result[8])
        self.lblFalc.setText(result[9])
        self.lblDept.setText(result[10])


class Login(QDialog):  # Login inherits every form element from the QDialog import
    def __init__(self):  # A function that runs immediately the code is ran
        super(Login, self).__init__()
        loadUi('ui/login.ui', self)

        self.w = None
        self.buttonHandle()
        self.setWindowTitle('My new window title')
        self.show()


    def buttonHandle(self):
        self.btnShowPass.clicked.connect(self.showPassword)
        self.btnRegister.clicked.connect(self.register)
        self.btnLogin.clicked.connect(self.login)

    def showPassword(self):
        if self.txtPassword.echoMode() == 0:
            self.txtPassword.setEchoMode(2)
        else:
            self.txtPassword.setEchoMode(0)

    def showUser(self):
        # self.w = User()
        # self.w.show()
        # self.hide()
        pass

    def register(self):
        # from PyQt5.QtWidgets import QComboBox
        # h = QComboBox()
        # h.item
        try:
            fullname = self.txtFullname.text()
            username = self.txtUser.text()
            passwd = self.txtPassword.text()
            confirm = self.txtConfirm.text()
            email = self.txtEmail.text()
            usertype = self.cmbUserType.currentText()
            noww = datetime.now()

            if not fullname or not username or not passwd or not email:
                msg = "You need to fill all the fields"
            elif len(passwd) < 5:
                msg = "Your password is too short"
            elif passwd != confirm:
                msg = "Password Mismatch"
            else:
                passwd = Sun.encrypt(passwd)
                sql = f"""INSERT INTO users (fullname, username, password, email, usertype, regdate) 
                VALUES ('{fullname}','{username}', "{passwd}", '{email}', '{usertype}', '{noww}')"""
                cursor.execute(sql)
                DB.commit()
                msg = "You have registered"
                self.lblMsg.setStyleSheet('color: green')
        except Exception as err:
            msg = str(err)
            self.lblMsg.setStyleSheet("color: red")

        self.lblMsg.setText(msg)

    def login(self):
        username = self.txtLoginUser.text()
        passwd = self.txtLoginPass.text()
        sql = f"""SELECT password from users WHERE username = '{username}'"""
        result = cursor.execute(sql).fetchone()

        try:
            if not username or not passwd:
                msg = "No empty fields allowed!"
            elif not result:
                msg = "Invalid Password"
            else:
                if Sun.verify(passwd, result[0]):
                    print('logged')
                    print('after logged')
                else:
                    msg = "Your password is incorrect"
        except Exception as err:
            print(err)
            msg = str(err)

        self.lblLoginMsg.setText(msg)


def closeApp():
    print('hello')
    sys.exit()


app = QApplication(sys.argv)
win = User()  # First form to run
sys.exit(app.exec_())  # Prevents the app from closing after we run the python script
