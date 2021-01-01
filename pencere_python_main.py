from PyQt5.QtWidgets import *
from pencere_python import Ui_MainWindow2
from PyQt5.QtGui import QIntValidator
import sqlite3

class menuLibrary(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self)

        self.ui2.action_about.triggered.connect(self.about_slot)

        self.ui2.lineEdit_code.setPlaceholderText("Enter Book Code")
        self.ui2.lineEdit_bookname.setPlaceholderText("Enter Book Name")
        self.ui2.lineEdit_writer.setPlaceholderText("Enter Writter")
        self.ui2.lineEdit_type.setPlaceholderText("Enter Type")
        self.ui2.lineEdit_edition.setPlaceholderText("Enter Edition")

        self.ui2.lineEdit_edition.setValidator(QIntValidator(0, 99, self))


        self.ui2.lineEdit_booknamequery.setPlaceholderText("Enter Book Name")



        self.ui2.lineEdit_regusername.setPlaceholderText("Enter Username")
        self.ui2.lineEdit_regpassword.setPlaceholderText("Enter Password")

        self.ui2.lineEdit_regpassword.setEchoMode(QLineEdit.Password)


        self.ui2.page_homepage.index   = 0
        self.ui2.page_bookadd.index    = 1
        self.ui2.page_useradd.index    = 2
        #self.ui2.page_userlist.index   = 4

        self.ui2.pushButton_bookadd.clicked.connect(self.books_add)
        self.ui2.pushButton_bookadd.clicked.connect(self.info_slot)
        self.ui2.pushButton_bookadd.clicked.connect(self.line_clear_slot)


        self.ui2.pushButton_2.clicked.connect(self.user_add)
        self.ui2.pushButton_2.clicked.connect(self.info_slot2)
        self.ui2.pushButton_2.clicked.connect(self.line_clear_slot2)
        self.ui2.pushButton_2.setShortcut("Return")


        self.ui2.pushButton_namequery.clicked.connect(self.query_slot)




        self.ui2.actionAdd_Book.triggered.connect(self.go_add_book)
        self.ui2.actionBook_List.triggered.connect(self.go_homepage)
        self.ui2.actionAdd_User.triggered.connect(self.go_add_user)
        #self.ui2.actionUser_List.triggered.connect(self.go_user_list)

        self.go_homepage()

        self.baglanti_olustur()




    def go_homepage(self):
        self.ui2.stackedWidget.setCurrentIndex(self.ui2.page_homepage.index)
    def go_add_book(self):
        self.ui2.stackedWidget.setCurrentIndex(self.ui2.page_bookadd.index)

    def go_add_user(self):
        self.ui2.stackedWidget.setCurrentIndex(self.ui2.page_useradd.index)
    def go_user_list(self):
        self.ui2.stackedWidget.setCurrentIndex(self.ui2.page_userlist.index)

    def baglanti_olustur(self):


        self.con = sqlite3.connect("Library.db")

        self.cursor = self.con.cursor()


        query = "CREATE TABLE IF NOT EXISTS BOOKS (BookCode TEXT,BookName TEXT,Writer TEXT,Type TEXT,Edition INT)"
        query2 = "CREATE TABLE IF NOT EXISTS USERS (Username TEXT,Password TEXT)"
        self.cursor.execute(query)
        self.cursor.execute(query2)

        self.con.commit()



    def about_slot(self, setupUi):
        QMessageBox.about(self,"Information","This program is coded by <b>Batuhan Bağ</b>"
                                         "<br><br>"
                                         "<b>Batuhan Bağ Contact:</b>"
                                         "<br>"
                                         "<a href=\"mailto:batuhannbagg@gmail.com\">batuhannbagg@gmail.com</a>"
                                        "</font>"




                                            )
    def info_slot(self):

        QMessageBox.about(self,"Book Add","<b> Book Insertion Successful</b>")

    def info_slot2(self):
        QMessageBox.information(self, "User Added","<b> User Insertion Successful</b>")


    def line_clear_slot(self):

        self.ui2.lineEdit_code.clear()
        self.ui2.lineEdit_bookname.clear()
        self.ui2.lineEdit_writer.clear()
        self.ui2.lineEdit_type.clear()
        self.ui2.lineEdit_edition.clear()
        self.ui2.lineEdit_regpassword.clear()
        self.ui2.lineEdit_regpassword.clear()

    def line_clear_slot2(self):
        self.ui2.lineEdit_regusername.clear()
        self.ui2.lineEdit_regpassword.clear()

    def books_add(self):

        bookcode = self.ui2.lineEdit_code.text()
        bookname = self.ui2.lineEdit_bookname.text()
        writer = self.ui2.lineEdit_writer.text()
        type = self.ui2.lineEdit_type.text()
        edition = self.ui2.lineEdit_edition.text()

        query = "INSERT INTO BOOKS VALUES (?,?,?,?,?)"

        self.cursor.execute(query,(bookcode,bookname,writer,type,edition))


        self.con.commit()

    def user_add(self):
        username = self.ui2.lineEdit_regusername.text()
        password = self.ui2.lineEdit_regpassword.text()


        query2 = "INSERT INTO USERS VALUES (?,?)"

        self.cursor.execute(query2,(username,password))

        self.con.commit()






    def query_slot(self):

        #self.ui2.lineEdit_info.setEnabled(True)
        booknamee = self.ui2.lineEdit_booknamequery.text()

        self.cursor.execute("select * from BOOKS where BookName ='(booknamee)'")

        bookss = self.cursor.fetchall()

        if (len(bookss) == 0):

            QMessageBox.critical(self,"Error","Books Not Defined")
        else:
            self.ui2.textEdit.setText(bookss)

            self.con.commit()





