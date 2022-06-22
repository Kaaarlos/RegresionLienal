from nbformat import read
from pylab import *
import pandas as pd
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv ("dataset_RegresionLineal.txt", sep = ",")

x=df.iloc[:,0:1]
y=df.iloc[:,[1]]
convergencia = []
m=np.size(y)

xt = np.array(x)
yt = np.array(y)

J=0
a0=0;
a1=0;
beta=0.023;
iterMax=600;
iter=1;

plot(x, y,'ro')
h=a0+a1*xt;
plot (x,h, 'grey')

aux = h - yt
aux = aux**2
J=(1/(2*m))*aux.sum()
while iter<iterMax:
    a0=a0-beta*((1/m))*sum(np.sum(h-yt))
    supl = np.array(h-yt)
    supl = supl * xt
    a1=a1-beta*((1/m)* np.sum(supl))
    h=a0+a1*x
    J=(1/(2*m))*sum((h.sum(axis=1)-y.sum(axis=1))**2);
    aux = h - yt
    convergencia.append(J)
    iter=iter+1
plot(x,h,'g')
print("El resultado de a1 es  =",a1)
print("El resultado de a0 es  =", a0)
print("El resultado de J es =",J)

print("PRUEBA")
datoEntrada = 9.7687; 
hDatoEntrada = a0 + (a1 * datoEntrada); 
print("x = ",datoEntrada)
print("Salida correcta",yt[83])
print("prediccion h",hDatoEntrada)
