#!/usr/local/bin
#-*- coding:UTF-8 -**
import math
#飞机起始位置向下
global imgUrl
imgUrl="/Users/zhangrong/Downloads/pic/timg.jpeg"

x=0
y=0
def getImgUrl():
    global  imgUrl
    return imgUrl
def setImgUrl(url):
    global imgUrl
    imgUrl = url
def getX():
    global  x
    return x
def setX(xx):
    global  x
    x=xx
def getY():
    global y
    return y
def setY(yy):
    global y
    y=yy
def ratio():
    return getY() if getX()>getY() else getY()#math.sqrt(getX()*getX()+getY()*getY())


