import numpy as np
def sigmoid(x):
    return 1.0/(1+np.exp(-x))
a=int(input("Enter a integer"))
print(sigmoid(a))
