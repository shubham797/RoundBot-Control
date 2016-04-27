
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
*  actuator_control_1_1.py : <br />
   ```
   a = Motor_Control([7,8,24,25])  # initialize the class with control PIN numbers 
   
   a.rotate_left_fixed()	# function self explained
   a.rotate_right_fixed()
   a.straight_backward()
   a.straight_forward()
   
   del a
   
   ```
  

### Contribution guidelines ###

* You are free to contribute, but first create an issue specifying the problem/suggestion.

### Who do I talk to? ###

* Repo owner or admin ::
  Shubham Singh (admin)


