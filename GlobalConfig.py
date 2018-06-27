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
#img地址
def getImgUrl():
    global  imgUrl
    return imgUrl
def setImgUrl(url):
    global imgUrl
    imgUrl = url
#imgx的像素点
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
#imgy的长度像素点
def setY(yy):
    global y
    y=yy
    print("y=%s"%yy)
#比例尺  用realy/imgy也可以，看哪个精度更准确
def ratio():
    return  realx/imgx
#实际户型宽
width=2550+8400*4+8800+1150
#实际户型长
height=1150+6400+8400*6+9200+9400+550
print ("实际户型宽:%d"%width)
print ("实际户型长:%d"%height)
ratio1=377/629
ratio2=46.1/77.1
#比例尺宽误差
print("比例尺宽误差:%f"%ratio1)
#比例尺长误差
print("比例尺长误差:%f"%ratio2)



