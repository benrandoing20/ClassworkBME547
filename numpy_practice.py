import numpy as np
import matplotlib.pyplot as plt

array_from_list = np.array([0, 2, 3, 0])
print(type(array_from_list)) # create nd array
print(array_from_list)

print(array_from_list+5)

a = np.zeros(10)
print(a)

b = np.ones(12)
print(b)

time = np.arange(0, 10, 0.1)
print(time)

y = np.sin(time)
print(y)

plt.plot(time, y)
plt.show()