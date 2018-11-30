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
     elif readingL == 1:
	  RPL.servoWrite(L,1500)
def right():
     if readingL == 0:
          RPL.servoWrite(R,1590)
     elif readingL == 1:
	  RPL.servoWrite(R,1500)
def both():
     RPL.servoWrite(L,1590)
     RPL.servoWrite(R,1410)
def none():
     RPL.servoWrite(L,1500)
     RPL.servoWrite(R,1500)
while x == 1:
     readingL = RPL.digitalRead(LS)
     readingR = RPL.digitalRead(RS)
     if readingL == 0 and readingR == 0:
          both()
     elif readingL == 1 and readingR == 1:
          none()
     else:
          left()
          right()
