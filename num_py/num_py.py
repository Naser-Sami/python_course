import numpy as np

# np.zeros((5, 5))
# print(np.zeros((5, 5)))
# print(type(np.zeros((5, 5))))
#
# print(np.ones((5, 5)))
#
# print(np.linspace(0, 10, 50))
# x = np.linspace(10, 100, 14)
# print(x)
#
# print(np.eye(4))
#
# print(np.random.rand(2))
# print(np.random.rand(2,4))
#
# print(np.random.randn(2))
# print(np.random.randn(5, 5))

# print(np.random.randint(1, 100))
# print(np.random.randint(1, 100, 10))

arr = np.arange(25)
# print(arr)
#
ranarr = np.random.randint(0, 50, 10)
# print(ranarr)

# print(arr.reshape(5, 5))

# print(ranarr.argmax())  # return index
# print(ranarr.argmin())  # return index
# print(ranarr.max())
# print(ranarr.min())

# Vector
# print(arr.shape)
# print(ranarr.shape)

# Notice the two sets of brackets
# print(arr.reshape(1, 25))
# print(arr.reshape(1, 25).shape)
#
# print(arr.reshape(25, 1))
# print(arr.reshape(25, 1).shape)

print(arr.dtype)
print(ranarr.dtype)

arr = [ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18]
var = arr + arr
print(var)

