
# RoundBot-Control README #

This README documents whatever steps are necessary to get application up and running.

### What is this repository for? ###

* Quick summary :: 
  This is the implementation of GPIO library of Python to control Raspberry PI based Round-Bot.
  It contains some of the Basic functions in one Class, for better control.
  Also has functions so that it can be used with wi-fi module.
* Version  ::
  Version -- 1.00

### How do I get set up? ###

* Summary of set up ::
	Raspberry PI,
	Python installed with GPIO library,

### Running the Code ###
*  **actuator_control_1_1.py** : <br />
   ```
   a = Motor_Control([7,8,24,25])  # initialize the class with control PIN numbers 
   
   a.rotate_left_fixed()	# function self explained
   a.rotate_right_fixed()
   a.straight_backward()
   a.straight_forward()
   
   del a			# Destroying the instance of class
   
   ```
* **motion-rotate.py** : <br />
  To control any raspberry pi based differential wheel robot, remotely using wi-fi module, use this module to connect and control the robot.<br />
  The server port and IP can be defined within first 9-10 lines of code. After that use any socket to connect and pass the control signals. <br />
  Two input signals has to be given in format : <br /><br /> ~~ dataX_dataY ~~ <br /><br />
- [ ] *dataX* - controls direction, varies from -25 to 25
- [ ] *dataY* - controls power, varies from -1 to 1 <br />
  ```
  sudo python motion_rotate.py
  
  ```
* **input_control.py** :<br />
  Similar to motion_rotate.py but uses actuator_1_1 class for controlling.<br />

### Contribution guidelines ###

* You are free to contribute, but first create an issue specifying the problem/suggestion.

### Who do I talk to? ###

* Repo owner or admin ::
  Shubham Singh (admin)


