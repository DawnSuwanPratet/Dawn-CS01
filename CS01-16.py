import numpy as np
from numpy import random

arr = random.randint(100, size = (5, 10))
newarr = np.sort(arr %5 == 0)
overnewarr = np.sort(newarr)

print(overnewarr)