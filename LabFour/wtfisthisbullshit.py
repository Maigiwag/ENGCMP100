
import scipy.io as io
import numpy as np
import matplotlib.pyplot
tsp = io.loadmat('tspData.mat',squeeze_me=True)
tsp = np.ndarray.tolist(tsp['tsp'])
cock = tsp[1][10]
for i in range(len(cock)):
    print(f"x{i}: {cock[i][0]}")
    print(f"y{i}: {cock[i][1]}")

