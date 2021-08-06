import sys
from PyQt5.QtWidgets import QApplication, QWidget
from Ada.ui.login import *


class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.show()

    def buttonHandle(self):
        self.ui.btnShowPass.clicked.connect(self.showPassword)

    def showPassword(self):
        pass


app = QApplication(sys.argv)
w = Form()
sys.exit(app.exec_())
