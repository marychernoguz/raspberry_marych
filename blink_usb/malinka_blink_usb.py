import serial
import sys
import time

try:
    ser = serial.Serial("COM5", 9600)
except:
    sys.exit("Error connecting device")

# ===========blinking================
print('Set the blink interval in seconds:')
t = float(input())
while (True):
    ser.write(b"e")
    time.sleep(t)
    ser.write(b"d")
    time.sleep(t)

print(ser.read(4))

# ==========reading bytes============
# english letter - 1 bytes
# text = 'abcd'
# ser.write((text).encode())
# print(ser.read(4).decode())

ser.close()