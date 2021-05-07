import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

K = 2
#step = 1/1000
#x = np.arange(-2, 2+step, step)

#def norm_dist(x:np.ndarray, mu:float, sigma:float) -> np.ndarray:
#  return np.exp(-np.square(x-mu)/(2*sigma))/(np.sqrt(2*np.pi)*sigma)

a=np.random.rand(K, 1000000)-0.5
plt.hist(np.sum(a, axis=0), bins=1000, normed=True)
#plt.plot(x, norm_dist(x, 0, 1))
plt.show()