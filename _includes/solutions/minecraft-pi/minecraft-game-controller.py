import serial
from time import sleep

# *** THE NEXT LINE MIGHT NEED TO BE CHANGED ***
PORT = "/dev/ttyACM1"
##
BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

while True:
    data = s.readline().decode('UTF-8')
    data_list = data.rstrip().split(' ')
    try:
        x, y, z, a, b = data_list

		# print out the values ?
		# do something with these values
		# use x, y, z to move the player?

    except:
        pass

s.close()

