# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
import sys
# import mysql.connector as con
from src.main_app import MainApp

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()