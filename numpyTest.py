import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import personTest

print(personTest.Person("John Doe", 30, "USA"))

a = np.array([[1, 2, 3],[4, 5, 6]])
print(a.shape)

print("--------------------")

testDataFrame = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(testDataFrame)

print("--------------------")
'''
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
'''
x = np.arange(0, 6*math.pi, 0.1)
y = np.tan(x)
fig, ax = plt.subplots()
ax.plot(x, y)

plt.xlim(0, 6*math.pi)
plt.ylim(-10, 10)

plt.show()