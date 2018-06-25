# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelloUi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import math


import GlobalConfig
import tello
import  numpy as np

PI=3.14
global drone
drone=0
class TelloController:

    def fly(self,point,isDebug):
        global  drone
        step,total=0,len(point)-1
        print("预计飞行[%d]次航程"%total)
        startDirection=np.polyadd([0,0],[0,1])
        if (len(point) > 0):
            lastPoint = point[0]
            for i in range(len(point)):
                step+=1
                p=point[i]
                if p == lastPoint:
                    begin = True
                    if(not isDebug):
                        drone=tello.Tello("192.168.10.2",8888)
                        drone.takeoff()
                        drone.move_up(1)
                    startVector=startDirection
                    toVector=np.polysub(point[i+1],p)
                    rotate =self.cal_rotate(startVector,toVector)
                    distance=self.cal_distance(toVector)
                    cw_or_ccw =self.cal_cw_or_ccw(startVector,toVector)
                elif p == point[len(point) - 1]:
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
                distance=distance*GlobalConfig.ratio()
                if not  isDebug:
                    if cw_or_ccw>0:
                        #顺时针
                        drone.rotate_cw(rotate)
                    else:
                        #逆时针
                        drone.rotate_ccw(rotate)
                    drone.move_forward(distance)
                    time.sleep(5)
                print("[warning]actual fly distance:%f" % distance)

        else:
            print('no point error')




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
