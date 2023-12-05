from numpy import *
from numpy.linalg import *
a = array([[1.0, 2.0], [3.0, 4.0]])
print(a)
print(111111111111)
print(a.transpose())
print(222222222222)
print(inv(a)) # inverse

print(3333333333333333333333)
u = eye(5, k=2) # k is the position where we need 1
print(u)
j = array([[0.0, -1.0], [1.0, 0.0]])
print(dot(j, j))

y = array([[5.], [7.]])
print(solve(a, y)) # solveur d’équations linéaires

print(eig(j))


