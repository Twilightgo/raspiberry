import matplotlib.pyplot as plt
import numpy as np

a=np.random.randn(10000)
plt.hist(a,bins=100,normed=1,facecolor="red",edgecolor="black",alpha=0.7)
plt.title("hist")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

