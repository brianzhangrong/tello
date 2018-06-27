# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelloUi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import blue as blue
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QPen, QColor, QImage
from PyQt5.QtWidgets import QLabel
import GlobalConfig
import TelloController

global point
point=[]
lineColor =QColor(255, 0, 255)
pointColor=QColor(0, 0, 255)
pen=QPen()
'''
    标定打点类
'''
class TQLable(QLabel):

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        super().mousePressEvent(ev)
        self.showHistoryPoint(ev)
        self.repaint()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        global pen
        painter = QPainter(self)
        painter.setPen(pen)
        img = QImage(GlobalConfig.getImgUrl())
        painter.drawImage(QPoint(0, 0), img)
        self.drawLineByClickPoint(painter)

    def drawLineByClickPoint(self,painter):
        if(len(point)!=0):
            lastPoint=point[0]
            self.drawOnePoint(lastPoint, painter)
            for p in point:
                self.drawOnePoint(p, painter)
                self.drawOneLine(lastPoint, p, painter)
                lastPoint = p

    def drawOneLine(self, lastPoint, p, painter):
        pen.setWidth(3)
        pen.setColor(lineColor)
        painter.drawLine(lastPoint[0], lastPoint[1], p[0], p[1])

    def drawOnePoint(self, lastPoint, painter):
        pen.setWidth(5)
        pen.setWidthF(5)
        pen.setColor(pointColor)
        painter.drawArc(lastPoint[0],lastPoint[1],0,0,360,16)
        #painter.drawPoint(lastPoint[0], lastPoint[1])

    def showHistoryPoint(self,ev):
        global point
        point.append([ev.x(), ev.y()])

    def beginFly(self):
        global point
        print ("************fly directions****************"+repr(point))

        controller =TelloController.TelloController()

        controller.fly(point,False)
        #after fly release point
        point=[]