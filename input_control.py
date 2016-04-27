import sys
from time import sleep
import actuator_control_1_1 as act
import socket
import time
import os
import math
import numpy as np

def Establish_Connection(host,port):
    s = socket.socket()         # Create a socket object
    s.bind((host, port))        # use host if u know about the IP address or manually give the IP address

    print 'Server Started'
    s.listen(5)                 # Waiting for client
    c, addr = s.accept()        # Establish connection with client.
    print 'Got connection from', addr
    return c

def Input_Parsing(data):
    dat = data.split("_")       # Define logic of the Input
    dataX = float(dat[0])
    dataY = int(dat[1])
    return dataX, dataY

def main():
    controller = act.Motor_Control([7,8,24,25])
    conn = Establish_Connection('192.168.43.173',12345)

    try:
        while True:
            data = conn.recv(20)
            print data
            data_para, data_dir = Input_Parsing(data)
            controller.control_motion_pwm(data_para,data_dir)

            time.sleep(1)       # time in seconds
    except KeyboardInterrupt:
        conn.close()

main()
