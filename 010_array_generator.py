# a = range(10)
#
# for i in a:
#     print(i)
#
# b = ['a', 'b', 'c', 'd']
#
# for i,j in enumerate(b):
#     print(i,j)
#
import numpy as np
# g = 0.01*np.ones((4,6))
# g = np.zeros(3)
# h = np.linspace(0,5,11)insert 11 value between 0-10
# o = np.arange(1,10,2)insert value starts from 1 to 10 with step value is 2
# size = g.shape
x = np.arange(0,361,10)
y = np.sin(x*np.pi/180)
# print(x,y)
import matplotlib.pyplot as plt
plt.plot(x, y)



