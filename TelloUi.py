# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelloUi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QImage, QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QPushButton

import GlobalConfig
from TQLabel import TQLable


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        width,length=110,50
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(56)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMouseTracking(True)
        Dialog.setFocusPolicy(QtCore.Qt.TabFocus)
        #布局
        self.addLayout(Dialog)

        self.addImg()
        self.addShowImgLabel(Dialog, length, width)

        #global
        GlobalConfig.setX(self.img.size().width())
        GlobalConfig.setY(self.img.size().height())
        #pushbtn
        self.addPushBtn(Dialog, length, width)
        #veticalLayout
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.label)
        #slot and signal
        self.configSlotAndSignal(Dialog)

    def addImg(self):
        self.img = QImage(GlobalConfig.getImgUrl())

    def addLayout(self, Dialog):
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")

    def addShowImgLabel(self, Dialog, length, width):
        # label
        self.label = TQLable(Dialog)
        self.label.setObjectName("label")
        # img

        self.label.resize(self.img.size())
        self.label.setStyleSheet("color:white")
        Dialog.resize(self.img.size().width(), self.img.size().height() + length)
        # 初始绘制图片
        self.clearPoint()

    def addPushBtn(self, Dialog, length, width):
        self.pushButton = QPushButton(QIcon("icon/fly.png"),"开始飞行",Dialog)
        self.pushButton.setObjectName("pushBtn")
        self.pushButton.setStyleSheet("QPushButton{background-color:rgb(0,200,250);\
                                       color: white;   border-radius: 10px;  border: 2px groove gray;\
                                       border-style: outset;}"
                                      "QPushButton{text-align : right;}"
                                      "QPushButton:hover{background-color:white; color: black;}"
                                      "QPushButton:pressed{background-color:rgb(85, 170, 255);\
                                       border-style: inset; }")
        self.pushButton.setEnabled(True)
        #self.pushButton.setContentsMargins(2, 1, 2, 1)
        # 字体格式
        font = self.pushBtnFont()
        self.pushButton.setFont(font)
       # self.pushButton.setText("fly")
        self.pushButton.setFixedSize(width,length)
        self.pushButton.setGeometry(self.img.size().width()-width, self.img.size().height(),
                                    self.img.size().width()-width,
                                    self.img.size().height() + length)

    def configSlotAndSignal(self, Dialog):
        self.retranslateUi(Dialog)
        # signal and slot
        self.pushButton.clicked['bool'].connect(self.label.beginFly)
        self.pushButton.clicked['bool'].connect(self.clearPoint)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def pushBtnFont(self):
        font = QFont()
        font.setFamily("宋体")
        font.setPixelSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setPointSize(20)
        font.setStyle(QFont.StyleItalic)
        font.setWeight(QFont.Light)
        return font

    def clearPoint(self):
        self.label.setPixmap(QPixmap.fromImage(self.img))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "艾佳生活飞行控制器"))


