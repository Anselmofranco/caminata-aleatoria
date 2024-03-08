#caminata aleatoria de un cuerpo

import random as rnd
import matplotlib.pyplot as plt
import numpy as np

caminata= np.zeros(200)



for i in range (1,200):
    nro=rnd.random()    
    if nro>0.5:
        caminata[i]=caminata[i-1]+1
    else:
        caminata[i]=caminata[i-1]-1
        
plt.plot(caminata)