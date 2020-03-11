import matplotlib.pyplot as plt
import numpy as np

#画图
x=np.linspace(0,10,100)
#print(x)
y=np.sin(x)
z=np.cos(x**2)
plt.figure(figsize=(8,4))
plt.plot(x,y,color="red",label="$sin(x)$",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("V")
plt.title("pytho basis -- matplotlib")
plt.ylim(-1.2,1.2)
plt.legend(loc=1)
plt.show()

