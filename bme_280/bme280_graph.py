import numpy as np
import matplotlib.pyplot as plt


file = open("bme280.txt", "r")
data = file.read()
file.close()

data = data.split('\n\n')[:-1]
data_h = [float(data[i]) for i in range(0, len(data)-2, 3)]
data_p = [float(data[i]) for i in range(1, len(data)-1, 3)]
data_t = [float(data[i]) for i in range(2, len(data), 3)]

time_h = range(0, len(data_h))
time_p = range(0, len(data_p))
time_t = range(0, len(data_t))

plt.subplots_adjust(wspace= 0.5, hspace=0.5)

plt.subplot(2, 2, 1)
plt.plot([time_h[i] for i in range(len(time_h))], data_h, label = 'humidity')
plt.xlabel("time, ms")
plt.ylabel("humidity, %")

plt.subplot(2, 2, 2)
plt.plot([time_p[i] for i in range(len(time_p))], data_p, label = 'pressure')
plt.xlabel("time, ms")
plt.ylabel("pressure, Pa")

plt.subplot(2, 2, 3)
plt.plot([time_t[i] for i in range(len(time_t))], data_t, label = 'temperature')
plt.xlabel("time, ms")
plt.ylabel("temperature, C")

# plt.legend()
plt.show()

