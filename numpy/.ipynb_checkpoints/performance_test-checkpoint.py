# brute force using a for loop
import numpy as np
def brute_force_version(N):
    arr = np.arange(N)
    dif = np.zeros(N-1, int)
    for i in range(1, len(arr)):
        dif[i-1] = arr[i] - arr[i-1]

def vectorized_version(N):
    # vectorised operation
    arr = np.arange(N)
    dif = arr[1:] - arr[:-1]
   
if __name__ == '__main__':
    values = [10,100,1000,10000,100000]
    for value in values:
        brute_force_version(value)
        vectorized_version(value)
    