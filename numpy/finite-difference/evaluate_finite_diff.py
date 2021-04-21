
import numpy as np

def eval():
    dx = 0.2
    X = np.arange(0,np.pi/2.0, step = dx)
    size = X.shape[0]
    df = (np.sin(X+dx)-np.sin(X-dx))/(2*dx)
    #print(np.sum((df-np.cos(X))**2))
