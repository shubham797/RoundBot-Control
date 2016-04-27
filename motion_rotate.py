from time import sleep
import time
import os
import RPi.GPIO as GPIO
import socket

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346                # Reserve a port for your service.
s.bind(('192.168.43.105', port))        # Bind to the port

print 'Server Started'
s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)				#Left Motor Backward
GPIO.setup(8, GPIO.OUT)				#Left Motor Forward
GPIO.setup(24, GPIO.OUT)			#Right Motor Forward
GPIO.setup(25, GPIO.OUT)

left_wheel_f = GPIO.PWM(8,100)
left_wheel_b = GPIO.PWM(7,100)
right_wheel_f = GPIO.PWM(24,100)
right_wheel_b = GPIO.PWM(25,100)

#left_wheel_f.start(100)
#right_wheel_f.start(100)
boolean_op = False

try:
    while True:
        data = c.recv(50)
        dat = data.split("_")
        dataX = int(dat[0])
        dataY = float(dat[1])
        print dataX,dataY
        '''
                considering the value of dataY lies between -1 to 1
        '''
        
        max_power = 100.0 * dataY
        max_power = int(max_power)

	if max_power <= 0:
	    sign = False
	else:
	    sign = True

        if max_power < 80 and max_power >= 0:
            max_power = 80
	elif max_power > -80 and max_power < 0:
	    max_power = 80
	elif max_power < 0:
	    max_power = max_power * -1

        '''
                considering the case when the -100 starts from left side to 100
                dataX takes the value from the -25 to 25
        '''
        if dataX >= 0:
            max_power_l = max_power
            max_power_r = max_power * (100 - dataX)/100
        elif dataX < 0:
            max_power_r = max_power
            max_power_l = max_power * (100 + dataX)/100

        max_power_l = int(max_power_l)
        max_power_r = int(max_power_r)

        print max_power_l, max_power_r
        
        if sign:
            if boolean_op:
                left_wheel_f.ChangeDutyCycle(max_power_l)
                right_wheel_f.ChangeDutyCycle(max_power_r)
            else:
                left_wheel_b.stop()
                right_wheel_b.stop()
                left_wheel_f.start(max_power_l)
                right_wheel_f.start(max_power_r)
                boolean_op = True
        else:
            if boolean_op:
                # stops Forward
                left_wheel_f.stop()
                right_wheel_f.stop()
                left_wheel_b.start(max_power_l)
                right_wheel_b.start(max_power_r)
                boolean_op = False
            else:
                left_wheel_b.ChangeDutyCycle(max_power_l)
                right_wheel_b.ChangeDutyCycle(max_power_r)
        
        time.sleep(1)
    c.close()
except KeyboardInterrupt:
	GPIO.cleanup()
	c.close()
