#!/usr/local/bin
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelloUi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5.QtGui import QMovie

import TelloUi

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = TelloUi.Ui_Dialog()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())