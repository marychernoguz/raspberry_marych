import numpy as np
import matplotlib.pyplot as plt


file = open("hello_adc.txt", "r")
data = file.read()
file.close()
data = data.split('\n\n')[:-1]
data = [float(data[i]) for i in range(len(data))]
print(data)

time = np.linspace(0, len(data))

plt.plot(time, data)
plt.show()