#%%

from matplotlib import pyplot as plt
import numpy as np

my_file = open("sequence.txt", "r")

data = list()

for line in my_file.readlines():
    num = line.rstrip("\n").split(", ")[1]
    data.append(float(num))

my_file.close()

my_file = open("random.txt", "r")

data2 = list()

for line in my_file.readlines():
    num = line.rstrip("\n").split(", ")[1]
    data2.append(float(num))

my_file.close()

x = list(range(24, 101))

plt.plot(x, data, label = "sequence")
plt.plot(x, data2, label = "random")
plt.legend()
plt.show()

#%%