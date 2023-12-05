import numpy as np
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print("*******************************")
arr = np.array([1, 2, 3])
for x in arr:
    print(x)
print("*******************************")

arr = np.array([[[1, 2, 3],
[4, 5, 6]],
[[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)


print(f"np.arange(0, 11,2): {np.arange(0, 11,2)}")

print(f"np.zeros((3,3,3)): {np.zeros((3,3,3))}")
print(f"np.linspace(0,10,5): {np.linspace(0,10,5)}")
