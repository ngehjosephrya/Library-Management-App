from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MySQLdb
from PyQt5.uic import loadUiType
import datetime

from Mainwindow import MainApp



login,_ = loadUiType('template/login.ui')


class Login(QWidget , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_Login)
        style = open('themes/darkblue.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Handel_Login(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='' , db='library')
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[1] and password == row[3]:
                print('user match')
                self.window2 = MainApp()
                self.window2.show()
                self.close()
            else:
                self.label.setText('Make Sure You Enterd Your Username And Password Correctly')


