from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from gırısekran import Ui_MainWindow
from pencere_python_main import menuLibrary
import time
import sqlite3

class mainLogin(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui2 = menuLibrary()

        self.ui.giris_buton.clicked.connect(self.login_slot)
        self.logıncentral()

        _translate = QtCore.QCoreApplication.translate
        self.ui.giris_buton.setShortcut(_translate("MainWindow2", "Return"))




        self.ui.kullanci_ad.setPlaceholderText("Username")
        self.ui.kullanici_sifre.setPlaceholderText("Password")


        self.ui2.baglanti_olustur()
        #self.ui.loginscreen = Ui_MainWindow()


    def logıncentral(self):



        if self.ui.giris_buton.clicked.connect(self.login_slot):

            self.boolen = True


        else:
            boolen = False




    def about_slot(self, setupUi):
        QMessageBox.about(self,"İletişim","Bu Programı <b>Batuhan Bağ</b> hazırlamıştır"
                                         "<br><br>"
                                         "<b>Batuhan Bağ İletişim:</b>"
                                         "<br>"
                                         "<a href=\"mailto:batuhannbagg@gmail.com\">batuhannbagg@gmail.com</a>"
                                        "</font>"
                                            )
    def login_slot(self):
        name = self.ui.kullanci_ad.text()
        password = self.ui.kullanici_sifre.text()

        self.ui2.cursor.execute("Select Username,Password FROM USERS")

        userinfo = self.ui2.cursor.fetchall()
        

        if name == userinfo[0][0] and password == userinfo[0][1]\
                or name == userinfo [1][0] and password == userinfo[1][1]:
            self.ui2.show()
            time.sleep(1)
        else:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("Try Again")
            message_box.setText("User or Password Wrong")

            message_box.exec_()








app = QApplication([])
window = mainLogin()
window.showMaximized()
app.exec_()


