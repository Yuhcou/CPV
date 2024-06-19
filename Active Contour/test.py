import numpy as np


shape = (400, 600)

s = np.linspace(0, 2 * np.pi, 11)
r = shape[0] / 2 + 100 * np.sin(s)  # 100 * 3 for scaling
c = shape[1] / 2 + 100 * np.cos(s)  # 100 * 3 for scaling
init = np.array([r, c])

print(s)
print()
print(r)
print()pp
print(c)
print()
print(init)