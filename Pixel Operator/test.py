import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

a = []
a = np.append(a, [1,2])
a = np.array([1,2,3])
b = [1,1]
c = (a, b)
print(a.shape)
print(np.sum(a, keepdims=True).shape)

