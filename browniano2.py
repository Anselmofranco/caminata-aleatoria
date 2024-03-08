#caminata aleatoria de varios sistemas 

import random as rnd
import matplotlib.pyplot as plt
import numpy as np

n=10000
x= np.zeros((n,10))
#y= np.zeros((n,10))


for j in range (10):
    
    for i in range (1,n):
        v_x=rnd.random()-0.5
        #v_y=rnd.random()-0.5
        x[i,j]=x[i-1,j]+v_x    
        #y[i,j]=y[i-1,j]+v_y
        #if (x[i,j]**2+y[i,j]**2>=100):
        #    print(i)
         #   break

plt.plot(x[0:4500])#,y[0:4500])