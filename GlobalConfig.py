#!/usr/local/bin
#-*- coding:UTF-8 -**
import math
#飞机起始位置向下
global imgUrl,imgx,imgy,realx,realy
imgUrl="/Users/zhangrong/Downloads/pic/0001.jpg"

imgx=377 #图中户型x(像素值)
imgy=629 #图中户型y（像素值）

realx=46.1 #实际户型x（米）
realy=77.1 #实际户型y（米）

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
    print("x=%s"%xx)
    x=xx
def getY():
    global y
    return y
def setY(yy):
    global y
    y=yy
    print("y=%s"%yy)
def ratio():
    return  realx/imgx

width=2550+8400*4+8800+1150
height=1150+6400+8400*6+9200+9400+550
print ("%d"%width)
print ("%d"%height)
ratio1=377/629
ratio2=46.1/77.1
print("%f"%ratio1)
print("%f"%ratio2)


