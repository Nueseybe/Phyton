import requests
import sys, datetime, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import psycopg2
import hashlib
import binascii
from psycopg2 import sql

class MoneyExchanger(QtWidgets.QMainWindow):
    def __init__(self,*args, **kwargs) :
        super(MoneyExchanger,self).__init__()
        loadUi("main.ui",self)
        self.B_search.clicked.connect(self.ExchangeScreen)
        self.currentday = QDateTime.currentDateTime()
        self.ca_date.setDateTime(self.currentday)
    def ExchangeScreen(self):
        
        self.la_error.clear()
        self.la_first.clear()
        self.la_second.clear()
        self.money_code = self.c_first.currentText()
        #print(self.money_code)
        self.rate =self.c_second.currentText()
        #print(self.rate)
        #date = select_date.split("/")
        date1 = self.ca_date.date().toString("yyyy-MM-dd")
        self.date = date1.split("-")
        #print(self.date)
        url = f"https://v6.exchangerate-api.com/v6/b7af4957b142f323a4b710df/history/{self.money_code}/{self.date[0]}/{self.date[1]}/{self.date[2]}"
        try: 
            response = requests.get (url)
            result = response.json()["conversion_rates"][self.rate]
            #print(result)
            self.la_first.setText("1 {}".format (self.money_code))
            self.la_second.setText("{} on {}/{}/{}   ".format(result,self.date[2],self.date[1],self.date[0]))
            #self.la_error.setText(f"On {self.date[2]}/{self.date[1]}/{self.date[0]}   ")
        except:
            self.la_error.setText("On {}/{}/{} no information about {}   ".format(self.date[2],self.date[1],self.date[0],self.rate))
         

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoneyExchanger()
    widget = QStackedWidget()
    widget.addWidget(window)
    widget.setFixedHeight(750)
    widget.setFixedWidth(1000)
    widget.show()
    try:
        sys.exit(app.exec_())

    except:
        print("Closing")
