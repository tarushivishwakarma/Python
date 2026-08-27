import numpy as np
matrix1=np.array([[1,2,4,5],[5,6,7,8],[3,6,7,9]])
print(matrix1)
print(id(matrix1))

#copy
# cmatrix1=matrix1
# print(cmatrix1)
# print(id(cmatrix1))
# cmatrix1.shape=4,3
# print(matrix1)

#view
vm2=matrix1.view()
print(vm2)
print(id(vm2))

# rs=0
# for i in matrix1:
#     for j in i:
#         rs+=j
#     print (rs)

# print(matrix1.max())
# print(matrix1.min())
# print(matrix1.sum())
# print(matrix1.transpose())
# print(matrix1*2)

# for i in np.nditer(matrix1):
#     print(i,end=" ")

# a=10
# b=20
# print(np.bitwise_and(a,b))

# m=np.array([[[1,2],[3,4]],[[6,7],[8,9]]])
# print(m)

# for i in np.nditer(m):
#     print(i,end=" ")
# l=m.max()
# print(l)
# print(m.min())
# print(m.max())

