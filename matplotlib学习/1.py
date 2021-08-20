#coding=gbk
"""
作者：川川
时间：2021/8/21
"""
import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([0, 6])#x数组
print(xpoints)
ypoints = np.array([0, 250])#y数组
print(ypoints)

plt.plot(xpoints, ypoints)
plt.show()