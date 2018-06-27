# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelloUi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import math
import traceback

import GlobalConfig
import tello
import  numpy as np
import time

PI=3.14
global drone
drone=tello.Tello("192.168.10.2", 8888, False, .9, "192.168.10.1", 8889)
'''
    tello的控制类
'''
class TelloController:
    '''
    根据打点计算飞行路线
    '''
    def fly(self,point,isDebug):
        global  drone
        end=False#是否截止点
        step,total=0,len(point)-1 #计算飞行步数，当前步数
        print("预计飞行[%d]次航程"%total)
        #起始向量，飞机头向下
        startDirection=np.polyadd([0,0],[0,1])
        if (len(point) > 0):
            lastPoint = point[0]
            for i in range(len(point)):
                step+=1
                p=point[i]
                if p == lastPoint:
                    #第一步 飞机起飞，上升1m，连接ssid
                    begin = True
                    if(not isDebug):
                        if drone is None:
                            self.connect()
                        self.takeOff()
                        self.moveUp()
                    startVector=startDirection
                    toVector=np.polysub(point[i+1],p)
                    rotate =self.cal_rotate(startVector,toVector)
                    distance=self.cal_distance(toVector)
                    cw_or_ccw =self.cal_cw_or_ccw(startVector,toVector)
                elif p == point[len(point) - 1]:
                    #最后一步，降落
                    end = True
                    toVector=startDirection
                    startVector=np.polysub(p,point[i-1])
                    rotate =self.cal_rotate(startVector,toVector)
                    cw_or_ccw = self.cal_cw_or_ccw(startVector,toVector)
                    distance=0
                else:
                    startVector = np.polysub(p, lastPoint)
                    toVector = np.polysub(point[i + 1], p)
                    rotate=self.cal_rotate(startVector, toVector)
                    distance=self.cal_distance(toVector)
                    cw_or_ccw = self.cal_cw_or_ccw(startVector,toVector)
                    pass
                lastPoint=p
                print("[warning]第%d次航程"%step)
                if cw_or_ccw>0:
                    print("[warning]顺时针旋转:%f"%rotate)
                else:
                    print("[warning]逆时针旋转:%f"%rotate)
                print("[warning]fly distance:%d,ratio:%f"%(distance,GlobalConfig.ratio()))
                #实际飞行距离=像素坐标距离*比例尺
                distance=distance*GlobalConfig.ratio()
                print("[warning]actual fly distance:%f" % distance)
                #debug模式不飞行
                if not  isDebug:
                    if cw_or_ccw>0:
                        #顺时针
                        self.rotateCw( rotate)
                    else:
                        #逆时针
                        self.rotateCcw( rotate)
                    #前行
                    self.move_forward(distance)
                    if end:
                        self.land()


        else:
            #没有打点
            print('no point error')
    '''
    连接ssid
    '''
    def connect(self):
        global drone
        try:
            drone = tello.Tello("192.168.10.2", 8888, False, .9, "192.168.10.1", 8889)
            time.sleep(5)
            print("connect to tello")
        except BaseException as e:
            msg = traceback.format_exc()
            print(msg)
    '''
    降落
    '''
    def land(self):
        global drone
        while True:
            try:
                drone.land()
                print("[sucess]landing.....")
                break
            except BaseException as e:
                msg = traceback.format_exc()
                print(msg)
    '''
    逆时针旋转
    '''
    def rotateCcw(self,  rotate):
        global drone
        try:
            drone.rotate_ccw(rotate)
            time.sleep(3)
        except BaseException as e:
            msg = traceback.format_exc()
            print(msg)
            drone.land()
    '''
    顺时针旋转
    '''
    def rotateCw(self, rotate):
        global drone
        try:
            drone.rotate_cw(rotate)
            time.sleep(3)
        except BaseException as e:
            msg = traceback.format_exc()
            print(msg)
    '''
    上升
    '''
    def moveUp(self):
        global drone
        try:
            drone.move_up(0.5)
            time.sleep(3)
        except BaseException as e:
            msg = traceback.format_exc()
            print(msg)
    '''
    起步
    '''
    def takeOff(self):
        global drone
        try:
            drone.takeoff()
            time.sleep(3)
        except BaseException as e:
            msg = traceback.format_exc()
            print(msg)
    '''
    前行，单步最长4米
    '''
    def move_forward(self,distance):
        global drone
        if(distance>4):
            loop = distance//4
            if drone is not None:
                for i in range(loop):
                    self.makeSureForwardMoved(4)
            distance-=4*loop
            print("move forward:4")
        if(distance>0):
            if drone is not None:
                self.makeSureForwardMoved(distance)
            print("move forward:%f"%distance)
        if drone is not None:
            time.sleep(5)
    '''
    确保一定前行distance
    '''
    def makeSureForwardMoved(self,distance):
        global drone
        try:
            drone.move_forward(distance)
            time.sleep(3)
        except BaseException as e:
            msg = traceback.format_exc()
            print(msg)

    def cal_distance(self,toVector):
        return math.sqrt(toVector[0]*toVector[0]+toVector[1]*toVector[1])


    def cal_cw_or_ccw(self,startVector,toVector):
        return startVector[0]*toVector[1]-startVector[1]*toVector[0]
    '''
    60位格式化输出
    '''
    def cal_rotate(self, startVector,toVector):
        arcos = 1.0* np.dot(startVector, toVector) / (1.0*
                    math.sqrt(startVector[0] * startVector[0] + startVector[1] * startVector[1]) * math.sqrt(
                toVector[0] * toVector[0] + toVector[1] * toVector[1]))
        rotate = math.acos(arcos)*180/PI
        print("############################################################")
        print("#cal rotate:%22s-->%22s#"%(repr(startVector),repr(toVector)))
        print("#dot:%54s#"%repr( np.dot(startVector, toVector)))
        print("#startVector:%46f#"%math.sqrt(startVector[0] * startVector[0] + startVector[1] * startVector[1]))
        print("#toVector:%49f#"%math.sqrt( toVector[0] * toVector[0] + toVector[1] * toVector[1]))
        print("#acos:%53f#"%arcos)
        print("#rotate:%51f#"%rotate)
        print("############################################################")
        return rotate

    # def calc_angle(self,x_point_s, y_point_s, x_point_e, y_point_e):
    #     angle = 0
    #     y_se = y_point_e - y_point_s;
    #     x_se = x_point_e - x_point_s;
    #     if x_se == 0 and y_se > 0:
    #         angle = 360
    #     if x_se == 0 and y_se < 0:
    #         angle = 180
    #     if y_se == 0 and x_se > 0:
    #         angle = 90
    #     if y_se == 0 and x_se < 0:
    #         angle = 270
    #     if x_se > 0 and y_se > 0:
    #         angle = math.atan(x_se / y_se) * 180 / math.pi
    #     elif x_se < 0 and y_se > 0:
    #         angle = 360 + math.atan(x_se / y_se) * 180 / math.pi
    #     elif x_se < 0 and y_se < 0:
    #         angle = 180 + math.atan(x_se / y_se) * 180 / math.pi
    #     elif x_se > 0 and y_se < 0:
    #         angle = 180 + math.atan(x_se / y_se) * 180 / math.pi
    #     return angle
