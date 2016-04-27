import sys
from time import sleep
import RPi.GPIO as GPIO
import time
import os
import math
import numpy as np

class Motor_Control:
    '''
    Basic Class for the Motor control in RoundBot.
        7 -- Left Backward
        8 -- Left Forward
        24 -- Right Forward
        25 -- Right Backward
    '''
    pin = np.array(4)
    PIN = False
    PWM = False
    boolean_op = False
    res = []
    
    def setup_pin(self,pin):
        if len(pin) == 4 and Motor_Control.PIN == False:
            try:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pin[0], GPIO.OUT)			#Left Motor Backward
                GPIO.setup(pin[1], GPIO.OUT)			#Left Motor Forward
                GPIO.setup(pin[2], GPIO.OUT)		        #Right Motor Forward
                GPIO.setup(pin[3], GPIO.OUT)                    #Right Motor Backward
                Motor_Control.PIN = True
                return True
            except:
                print "Unexpected error:", sys.exc_info()[0]
                return False
        else :
            return False

    def set_PWM(self,pin,freq):
        if freq > 0 and freq < 200 and Motor_Control.PIN == True and Motor_Control.PWM == False:
            try:
                left_f = GPIO.PWM(pin[1],freq)
                left_b = GPIO.PWM(pin[0],freq)
                right_f = GPIO.PWM(pin[2],freq)
                right_b = GPIO.PWM(pin[3],freq)
                Motor_Control.PWM = True
                return [left_f, left_b, right_f, right_b]
            except :
                print "Unexpected error:", sys.exc_info()[0]
                return [0]
        else :
            print "Frequency Out of Range"
            return [0]

    def map_input(corr_param):
        f = 2**corr_param
        if f > 30 :
            return 30
        return f
        

    
    def control_motion_pwm(self,corr_param,corr_direc):
        if Motor_Control.PWM == True and len(Motor_Control.res) == 4 :
            if corr_param > MAX_VAL:
                vel_diff = 30
            else:
                vel_diff = self.map_input(corr_param)

            if Motor_Control.boolean_op:
                if corr_direc > 0:
                    Motor_Control.res[0].ChangeDutyCycle(max_vel - vel_diff)
                    Motor_Control.res[2].ChangeDutyCycle(max_vel)
                else:
                    Motor_Control.res[0].ChangeDutyCycle(max_vel)
                    Motor_Control.res[2].ChangeDutyCycle(max_vel - vel_diff)
            else:
                if corr_direc > 0:
                    Motor_Control.res[0].start(max_vel - vel_diff)
                    Motor_Control.res[2].start(max_vel)
                else:
                    Motor_Control.res[0].start(max_vel)
                    Motor_Control.res[2].start(max_vel - vel_diff)
                Motor_Control.boolean_op = True
        else:
            print 'PWM is not Initialized'
            
    def stop_motion_pwm(self):
        if Motor_Control.PWM == True and len(Motor_Control.res) == 4 :
            Motor_Control.res[0].stop()
            Motor_Control.res[1].stop()
            Motor_Control.res[2].stop()
            Motor_Control.res[3].stop()
        else :
            print 'PWM is not Initialized'
        
    def rotate_left_fixed(self):
        p = np.array(4)
        p = Motor_Control.pin[:]
        
        GPIO.output(p[0],False)
        GPIO.output(p[1],False)
        GPIO.output(p[2],True)
        GPIO.output(p[3],False)

        inp = raw_input("Press Any key to stop ")
        GPIO.output(p[2],False)

    def rotate_right_fixed(self):
        p = np.array(4)
        p = Motor_Control.pin[:]
        
        GPIO.output(p[0],False)
        GPIO.output(p[1],True)
        GPIO.output(p[2],False)
        GPIO.output(p[3],False)

        inp = raw_input("Press Any key to stop ")
        GPIO.output(p[1],False)

    def straight_forward(self):
        p = np.array(4)
        p = Motor_Control.pin[:]
        
        GPIO.output(p[0],False)
        GPIO.output(p[1],True)
        GPIO.output(p[2],True)
        GPIO.output(p[3],False)

        inp = raw_input("Press Any key to stop ")
        GPIO.output(p[1],False)
        GPIO.output(p[2],False)         

    def straight_backward(self):
        p = np.array(4)
        p = Motor_Control.pin[:]
        
        GPIO.output(p[0],True)
        GPIO.output(p[1],False)
        GPIO.output(p[2],False)
        GPIO.output(p[3],True)

        inp = raw_input("Press Any key to stop ")
        GPIO.output(p[0],False)
        GPIO.output(p[3],False)         
        
    def __del__(self):
        class_name = self.__class__.__name__
        GPIO.cleanup()
        print class_name, "instance destroyed"
        
    def __init__(self,p):
        print "Initialized Class Motor_Control"
        Motor_Control.pin = p
        if self.setup_pin(Motor_Control.pin):
            res = self.set_PWM(Motor_Control.pin,100)
            print len(res)
            print "SuccessFully Initialized"
        else:
            print "Error in Initializing"

a = Motor_Control([7,8,24,25])
a.rotate_left_fixed()
#a.rotate_right_fixed()
#a.straight_backward()
#a.straight_forward()
del a
