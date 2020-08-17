import numpy as np
a=np.array([[4,5,6,7,8,8]])
b=np.array([[12,13,45,6,77],[33,65,77,87,99]])


c=np.vstack((a,b))
print(c)
d=np.array([5,8,4,9]).reshape(2,2)
print(d)
print(np.hstack((b,d)))
