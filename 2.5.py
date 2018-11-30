import RoboPiLib as RPL
import setup
x = 1
L = Pin 
R = Pin
LS = Pin
RS = Pin
RPL.pinMode(LS,RPL.INPUT)
RPL.pinMode(RS,RPL.INPUT)

def left():
     if readingL == 0:
          RPL.servoWrite(L,1410)
     Elif readingL == 1:
	  RPL.servoWrite(L,1500)
def right():
     if readingL == 0:
          RPL.servoWrite(R,1590)
     Elif readingL == 1:
	  RPL.servoWrite(R,1500)
def both():
     RPL.servoWrite(L,1590)
     RPL.servoWrite(R,1410)

