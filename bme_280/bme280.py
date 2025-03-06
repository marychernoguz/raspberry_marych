import serial
import sys
import time

try:
    ser = serial.Serial("COM5", 115200)
except:
    sys.exit("Error connecting device")

file = open("bme280.txt", "w")

t = 0
while (t <= 30):
    ser.write("a".encode('ascii'))
    data = ser.read(23).decode('utf-8')[:-1]
    # p = ser.read(8).decode('utf-8')[:-1]
    # t = ser.read(7).decode('utf-8')[:-1]
    print(data)
          # , p, t)
    file.write(data)
    t += 1

ser.close()
file.close()
