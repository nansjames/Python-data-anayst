import numpy as np
a= np.array([[2, 3 , 4],[5 ,5 ,5]])

print(f"a.ndim: {a.ndim}")

print(f"np.arange(4): {np.arange(4)}")

print(f"np.arange(4).reshape(2,2): {np.arange(4).reshape(2,2)}")

print(f"np.sin(a): {np.sin(a)}")

a = np.array([[1],[ 2]])
b = np.array([[1,1,1],[1,1,1]])
print(f"np.add(a, b): {np.add(a, b)}")
print(f"a*b: {a*b}")

a = np.random.random((2,3))
print(f"a: {a}")
print(f"a.sum(): {a.sum()}")

print(f"a.min(): {a.min()}")

print(f"a.max(axis=0): {a.max(axis=0)}")

print(f"a.min(axis=1): {a.min(axis=1)}")




