import numpy as np
print(type(np.arange(15)))
a = list(range(3))

b = np.array(a).reshape(3, 1)
print(b)
