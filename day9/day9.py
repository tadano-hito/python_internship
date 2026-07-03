import numpy as np
import time

py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

print(type(py_list))
print(type(np_array))

print(py_list * 2)  
print(np_array * 2)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
identity = np.identity(4)
arange = np.arange(0, 20, 2)
linspace = np.linspace(0, 10, 5)

print('1D array:', arr1)
print('2D array:\n', arr2)
print('zeros:\n', zeros)
print('ones:\n', ones)
print('identity:\n', identity)
print('arange:', arange)
print('linspace:', linspace)

x = range(100000)
y = range(100000, 200000)
start = time.time()
c = [(a+b) for a, b in zip(x, y)]
print('Python time:', time.time() - start)

a = np.arange(100000)
b = np.arange(100000, 200000)
start = time.time()
c = a + b
print('NumPy time:', time.time() - start)