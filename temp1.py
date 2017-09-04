import numpy as np
import pylab as pl
# Crea un vector (arreglo) con los valores del eje X
x = [1,2,3,4,5]
# Crea un vector (arreglo) con los valores en el eje Y para cada valor en el eje X
y = [1,4,9,16,25]
# Grafica el vector x contra el vector y
pl.plot(x,y)
#Guarda la grafica en el formato png
pl.savefig('temp1.png')
