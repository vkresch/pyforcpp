import numpy as np
import ctypes

def doadd(a, b):
    np.random.seed(0)  # seed for reproducibility

    x1 = np.random.randint(10, size=6)  # One-dimensional array
    x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
    x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array
    print(x1, x2, x3)
    return a+b

def dosub(a, b):
    return a-b

class Test:
    pass