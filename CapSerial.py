import serial
ser = serial.Serial(port='/dev/cu.usbmodem1414201', baudrate=9600)
caps = []
length =400
for i in range(length):
    value = int(ser.readline().strip())
    cap = (value - 12288)/40960.*4
    caps.append(cap)

import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.arange(length - 100), caps[100:])
plt.xlabel('Sample Sequence')
plt.ylabel('Capacitance (pF)')
plt.show()
