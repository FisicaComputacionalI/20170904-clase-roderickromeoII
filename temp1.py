import numpy as np
import pylab as pl
# Crea un vector (arreglo) con los valores del eje X
x = [2009,2010,2011,2012,2013,2014,2015,2016,2017]
# Crea un vector (arreglo) con los valores en el eje Y para cada valor en el eje X
y = [1,1,2,2,2,4,3,4,1]
#Con esta isntruccion colocamos un titulo al eje Y de la grafica. 
pl.ylabel('Novias y mascotas')
pl.xlabel('anios')
# Grafica el vector x contra el vector y
pl.axis ([2005,2020, 0,5])
pl.plot(x,y, 'ro')
#Guarda la grafica en el formato png
pl.savefig('temp1.png')
pl.show()
