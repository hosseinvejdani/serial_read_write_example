import serial
from time import sleep

port = '/dev/ttyUSB0'
baud = 9600
lastime = 0

# open a serial connection using the variables above
ser = serial.Serial(port=port, baudrate=baud)
# wait for a moment before doing anything else
sleep(0.2)

message = b'salam'
ser.write(message)
print(f'----- tx = {message}')

rx = ser.read_until(size=len(message))
print(f'----- rx = {rx}')