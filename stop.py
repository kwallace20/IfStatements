import RoboPiLib as RPL
import setup

motors = [0,1]
for off in motors:
	RPL.servoWrite(off,1500)
	print('pin %s is disabled' % (off))