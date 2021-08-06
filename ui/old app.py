import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class login(QDialog):
    def __init__(self):
        super(login, self).__init__()
        loadUi('login.ui')
        self.show()

    # def button

app = QApplication(sys.argv)
window = login()
sys.exit(app.exec_())
