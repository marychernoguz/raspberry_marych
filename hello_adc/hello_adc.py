import serial
import sys
import time

try:
    ser = serial.Serial("COM5", 115200)
except:
    sys.exit("Error connecting device")

file = open("hello_adc.txt", "w")

t = 0
while (t < 50):
    ser.write("a".encode('ascii'))
    x = ser.read(11).decode('utf-8')[:-1]
    print(x)
    file.write(x)
    t += 1
ser.close()
file.close()
