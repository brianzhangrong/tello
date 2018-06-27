#!/usr/local/bin
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelloUi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import traceback

import tello
import time

takeoffRestTime=5
setSpeedRestTime=5
global drone
def  main():
    global  drone
    global  takeoffRestTime
    global  setSpeedRestTime
    x=""
    help()
    while(1):
        try:
            x = input("input command:")
            if(x=="takeoff"):#起飞
                drone.takeoff()
                time.sleep(takeoffRestTime)
            elif (x=="land"):#降落
                drone.land()
            elif x=="command":
                drone.send_command("command")
            elif(x.startswith("s")):
                speed = getParameter(x)
                drone.set_speed(speed)
                time.sleep(setSpeedRestTime)
            elif(x.startswith("connect")):
                drone=tello.Tello("192.168.10.2", 8888,False,.9,"192.168.10.1",8889)
            elif(x.startswith("f")):
                distance= getParameter(x)
                drone.move_forward(distance)
            elif (x.startswith("b")):
                distance = getParameter(x)
                drone.move_backward(distance)
            elif (x.startswith("l")):
                distance = getParameter(x)
                drone.move_left(distance)
            elif (x.startswith("r")):
                distance = getParameter(x)
                drone.move_right(distance)
            elif (x.startswith("u")):
                distance = getParameter(x)
                drone.move_up(distance)
            elif (x.startswith("d")):
                distance = getParameter(x)
                drone.move_down(distance)
            elif(x.startswith("ccw")):
                ccw = getParameter(x)
                drone.rotate_ccw(ccw)
            elif (x.startswith("cw")):
                cw = getParameter(x)
                drone.rotate_cw(cw)
            elif(x.startswith("p")):
                flip = getParameter(x)
                drone.flip(flip)
            elif (x.startswith("q")):
                drone.land()
                break
            elif(x.startswith('h')):
                help()
            else:
                print("unSupport Command")
        except BaseException as e:
            msg = traceback.format_exc()
            print(msg)
            print("执行命令失败:%s"%x)
            continue


def help():
    print("""
                       命令              |      描述                      |      案例
                     --------------------------------------------------------------------------------------------------------
                     connect--              (*)连接 第一步使用                  e.g:connect 192.168.10.2:8888
                     help(h)--                帮助                             e.g:help
                     d--move down             下移                             e.g: d  10
                     u--move up               上移                             e.g: u  10
                     l--move left             左移                             e.g: l  10
                     r--move right            右移                             e.g: r  10
                     f--move forward          前移                             e.g: f  10
                     b--move backward         后移                             e.g: b  10
                     takeoff--                起飞                             e.g: takeoff 
                     land--                   降落                             e.g: land  
                     s--                      设置速度                          e.g: s  10
                     cw--                     顺时针旋转                        e.g: cw  10
                     ccw--                    逆时针旋转                        e.g: ccw  10
                     p--                      'l', 'r', 'f', 'b'               e.g: p  l
                                             'lb', 'lf', 'rb','rf'
                     quit--                   land并退出程序                    e.g: q
                     """)


def getParameter(x):
    ipPort = x.split(" ").pop(1)
    return ipPort


if __name__ == '__main__':
    main()
