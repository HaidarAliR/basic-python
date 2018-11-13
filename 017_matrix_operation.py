import numpy as np
x = np.genfromtxt('matrix1.txt')
y = np.genfromtxt('matrix2.txt')
z = np.genfromtxt('matrix3.txt')

# result = np.mat(x) + np.mat(y)

# #maatrix multiplication
# result = np.mat(x) * np.mat(y)

# #elementwise multiplication
# result = np.multiply(np.mat(x),np.mat(y))
# result = np.multiply(np.mat(x),np.mat(y))

# #matrix inversion (Gauss)

# from numpy.linalg import inv
# result = inv(np.mat(z))
U,s,V = np.linalg.svd(z,full_matrices=True)
# print(x)
# print(10*'=')
# print(y)
# print(10*'=')
# print(s.shape)
# print(U.shape)
# print(V.shape)
#
# so=[]
# for i in range(1):
#     if s[i] > 0:
#         so.append(1/s[i])
#     else:
#         so.append(0)
# print(so)
# a=np.zeros((2,2))
# so=np.array(so)
#
# a[0][0]=so[0]
# print(a)
# print(a.shape)

# result = (np.mat(V)) * np.mat(a))*np.mat(np.transpose(U))

# levenberg inverse
I=np.eye(2)

J=np.mat(np.transpose(z))*np.mat(z))+0.001*I

result = inv(np.mat(J))*np.mat(np.transpose(z))
print (result)





# #
