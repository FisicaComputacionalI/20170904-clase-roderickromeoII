import numpy as np
import pylab as pl
# Crea un vector (arreglo) con los valores del eje X
x = [13,14,15,16,17,18,19,20,21]
# Crea un vector (arreglo) con los valores en el eje Y para cada valor en el eje X
y = [1,1,2,2,2,4,3,4,1]
#Con esta isntruccion colocamos un titulo al eje Y de la grafica. 
pl.ylabel('Novias y mascotas')
pl.xlabel('tiempo')
# Grafica el vector x contra el vector y
pl.plot(x,y)
#Guarda la grafica en el formato png
pl.savefig('temp1.png')
