import sys  # To bring in the operating system
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit  # To introduce the Qapplication and QDialog
from PyQt5.uic import loadUi  # is used to run the UI designed


class Login(QDialog):  # Login inherits every form element from the QDialog import
    def __init__(self):  # A function that runs immediately the code is ran
        super(Login, self).__init__()
        loadUi('ui/login.ui', self)

        self.buttonHandle()
        self.setWindowTitle('My new window title')
        self.show()

    def buttonHandle(self):
        self.btnShowPass.clicked.connect(self.showPassword)

    def showPassword(self):
        if self.txtPassword.echoMode() == 0:
            self.txtPassword.setEchoMode(2)
        else:
            self.txtPassword.setEchoMode(0)



def closeApp():
    sys.exit()

app = QApplication(sys.argv)
win = Login()  # First form to run
sys.exit(app.exec_())  # Prevents the app from closing after we run the python script
