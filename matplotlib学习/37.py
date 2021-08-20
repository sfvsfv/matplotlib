# coding=gbk
"""
作者：川川
时间：2021/8/21
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()