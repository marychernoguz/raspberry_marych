import serial
import sys

try:
    ser = serial.Serial("COM5", 115200)
    print('coonected')
except:
    sys.exit("Error connecting device")

# ser.close()
# ser.open()
# while True:
#     data = ser.readline()
#     print(data.decode())

try:
    ser.write('check'.encode('utf-8'))
    print('start reading')
    x = ser.read(4).decode('utf-8')
    print('end reading')
except:
    x = 0
print(x)

ser.close()