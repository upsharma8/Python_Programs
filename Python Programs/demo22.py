#pip install numpy
import numpy as np
print(np.__version__)

n=np.array([[2,3,4,5,6],[5,6,8,8,4],
            [2,3,4,5,6],[2,3,4,5,6]])
print(n)
print(n.shape)
print(n.size)
print(n.ndim)
print(np.max(n))
print(np.min(n))
print(np.mean(n))
print(np.sum(n))
print(np.std(n))
print(np.argmax(n))
print(np.argmin(n))
print(n[1:3,2:5])


