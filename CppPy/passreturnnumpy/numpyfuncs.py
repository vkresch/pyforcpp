import numpy as np

def add_arrays(a, b):
    return np.add(a, b)

def ret_numpy():
    return np.random.random_sample((2, 2))

if __name__ == "__main__":
    data1 = np.random.random_sample((2, 2))
    data2 = np.random.random_sample((2, 2))
    print(add_arrays(data1, data2))

