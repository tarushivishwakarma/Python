import matplotlib
import numpy as np
import matplotlib.pyplot as plt
# a=1
# b=2
# c=3
# d=4
# x=np.array([0,1,2,3,4])
# # y=a*x+b
# # y=a*x*x+b*x+c
# y=a*x*x*x+b*x*x+c*x+d
# plt.title("Cubical Equation")
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.plot(x,y)
# plt.grid()
# plt.show()

# x=np.array([1,2,3,4])
# y=np.array([100,150,75,120])
# plt.plot(x,y,'o')
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.title('Data Sale')
# plt.grid()
# plt.show()

# x=np.array([10,15,20,25])
# y=np.array([1,2,3,4])
# plt.plot(x,y,linestyle="dotted")
# plt.show()

x=np.array([1,3,5,7])
y=np.array([2,4,6,8])
plt.title('CASE1')
plt.subplot(2,2,2)
plt.plot(x,y)

x1=np.array([0,1,3,4,5])
y1=np.array([0,1,0,1,0])
plt.title('CASE2')
plt.subplot(2,2,3)
plt.plot(x1,y1)

x2=np.array([1,2,3,4])
y2=np.array([100,150,75,120])
plt.title('CASE3')
plt.subplot(2,2,4)
plt.plot(x2,y2)

x3=np.array([10,15,20,25])
y3=np.array([1,2,3,4])
plt.title('CASE4')
plt.subplot(2,2,1)
plt.plot(x3,y3)

plt.suptitle('WHOLE_DATA')
# plt.plot(x1,y1,marker='*',linestyle='dashed',color='red',linewidth=3)
# plt.grid()
plt.show()