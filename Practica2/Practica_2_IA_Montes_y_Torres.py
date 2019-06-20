#!/usr/bin/env python
# coding: utf-8

# # Práctica 2
# 1238689 Montes Garay Lilyan Victoria
# 
# 1201706 Torres Aragón Juan Jorge

# **Ejercicio 1:**
# 
# Utilizar las bibliotecas de numpy y matplotlib para resolver el siguiente problema propuesto.
# Evaluar la siguiente función Gaussiana, en 50 puntos en un rango de x en [-10,10], para
# cada uno de los siguientes valores de m (media) y s (desviación) .

# In[1]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# In[ ]:


x = [np.linspace(-10,10,50)]


# In[ ]:


m = [0.5,1,1.5,2,0.5,1,1.5,2]
s = [1,2,3,4,4,3,2,1]


# In[ ]:


def gauss(x,m,s):
    y=[]
    for i in range (0,7):
        y.append((1/np.sqrt(2* np.pi*s[i]))**(-(((x[i]-m[i])/s[i])**2)/2))
    return y


# In[ ]:


y = gauss(x,m,s)
print(y)


# In[ ]:


for i in range (0,7):
    
    y = ((1/np.sqrt(2* np.pi*s[i]))**(-(((x-m[i])/s[i])**2)/2))
    
    fig, ax = plt.subplots()
    ax.plot(x, y)

    title1 = 'm = ', m[i] , 's = ', s[i]
    ax.set(xlabel='x', ylabel='y',
           title = title1)
    ax.grid()

    fig.savefig("test.png")
    plt.show()


# **Ejercicio 2:**
# 
# Utilizar las bibliotecas de numpy y matplotlib para resolver el siguiente problema propuesto.
# Realizar un programa que emplee la fórmula general para resolución de ecuaciones de
# segundo grado, de la forma ax2 + bx + c = 0 . Solicitar al usuario los valores para a , b y c ,
# el programa debe mostrar la solución calculada. Graficar la función con los parámetros
# capturados así como indicar con puntos las raíces calculadas, así como etiquetas en la
# gráfica mostrando el valor numérico de éstas.

# 

# In[ ]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# In[ ]:


p = np.zeros([3])


# In[ ]:


p[0] = float(input("a: "))
p[1] = float(input("b: "))
p[2] = float(input("c: "))


# In[ ]:


x1, x2 = np.roots(p)

print (np.roots(p))
x = np.arange(-10,10, 1)
y = p[0]*(x**2) + p[1]*x + p[2]

fig, ax = plt.subplots()

function, = ax.plot(x, y)

root1, = ax.plot(x1,0,"ro")
root2, = ax.plot(x2,0,"ro")


ax.set(xlabel='x', ylabel='y',
title='RAICES')
ax.grid()

fig.savefig("test.png")
plt.show()


# **Ejercicio 3:**
# 
# Realizar una demostración de la diferenciación numérica con las siguientes funciones,
# discretizando a 50 puntos, usando h=0.01 :
# 
# f(x) = ex e n x = [− 5, 5]
# 
# f(x) = e−2x en 2 x = [− 5, 5]
# 
# f(x) = cos x en x = [− 2π, 2π]
# 
# f(x) = Ln x en x = [1, 10]
# 

# In[ ]:


#Ejercicio 3
import numpy as np
import matplotlib.pyplot as plt
def dif(x, h=0.0001, f=np.sin):
  return (f(x+h)-f(x-h))/(2*h)

#3.1
x = np.linspace(-5,5,50)
y= np.exp(x) # Función Original
dy_num = dif(x,h=.01,f=np.exp) # Derivada con función
dy = np.exp(x) # Derivada Analitica
e = dy-dy_num # Error

ea = np.absolute(dy-dy_num)# Error Absoluto
er = ea/dy # Error Relativo
ep = er*100 # Error Porcentual

print("Error",e)
print("Error Absoluto",ea)
print("Error Porcentual",ep)
print("Error Relativo",er)

fig,ax =plt.subplots()
fig.suptitle('e^x en x de [-5,5]')

line1, =ax.plot(x,y,'g o', label='e^x')
line2, =ax.plot(x,dif(x,h=.01,f=np.exp),'r',label='Derivada')
line3, =ax.plot(x,dy,'b .',label='Analítica')
plt.grid()
ax.legend()
plt.show()

#3.2
x = np.linspace(-5,5,50)
y= np.exp(-2*(x**2)) # Función Original
dy_num = dif(x,h=.01,f=np.exp) # Derivada con función
dy = -4*x*np.exp(-2*(x**2)) # Derivada Analitica
e = dy-dy_num # Error

ea = np.absolute(dy-dy_num)# Error Absoluto
er = ea/dy # Error Relativo
ep = er*100 # Error Porcentual

print("Error",e)
print("Error Absoluto",ea)
print("Error Porcentual",ep)
print("Error Relativo",er)

fig,ax =plt.subplots()
fig.suptitle('e^-2(x^2) en x de [-5,5]')

line1, =ax.plot(x,y,'g o', label='e^-2(x^2)')
line2, =ax.plot(x,dif(x,h=.01,f=np.exp),'r',label='Derivada')
line3, =ax.plot(x,dy,'b .',label='Analítica')
plt.grid()
ax.legend()
plt.show()

#3.3
pi = np.pi
x = np.linspace(-2*pi,2*pi,50)
y= np.cos(x) # Función Original
dy_num = dif(x,h=.01,f=np.cos) # Derivada con función
dy = -1*np.sin(x) # Derivada Analitica
e = dy-dy_num # Error

ea = np.absolute(dy-dy_num)# Error Absoluto
er = ea/dy # Error Relativo
ep = er*100 # Error Porcentual

print("Error",e)
print("Error Absoluto",ea)
print("Error Porcentual",ep)
print("Error Relativo",er)

fig,ax =plt.subplots()
fig.suptitle('cos(x) en x de [-2pi,2pi]')

line1, =ax.plot(x,y,'g o', label='cos(x)')
line2, =ax.plot(x,dif(x,h=.01,f=np.cos),'r',label='Derivada')
line3, =ax.plot(x,dy,'b .',label='Analítica')
plt.grid()
ax.legend()
plt.show()


#3.4
x = np.linspace(1,10,50)
y= np.log(x) # Función Original
dy_num = dif(x,h=.01,f=np.log) # Derivada con función
dy = 1/x # Derivada Analitica
e = dy-dy_num # Error

ea = np.absolute(dy-dy_num)# Error Absoluto
er = ea/dy # Error Relativo
ep = er*100 # Error Porcentual

print("Error",e)
print("Error Absoluto",ea)
print("Error Porcentual",ep)
print("Error Relativo",er)

fig,ax =plt.subplots()
fig.suptitle('ln(x) en x de [1,10]')

line1, =ax.plot(x,y,'g o', label='ln(x)')
line2, =ax.plot(x,dif(x,h=.01,f=np.log),'r',label='Derivada')
line3, =ax.plot(x,dy,'b .',label='Analítica')
plt.grid()
ax.legend()
plt.show()

np.dot


# **Ejercicio 4:**
# 
# Utilizar las bibliotecas de numpy para resolver el siguiente problema propuesto. Crear una función en python que recibe dos parámetros, el primero de ellos indica las dimensiones de la matriz que se genera, siendo el segundo parámetro el rango de los valores que se generan aleatoriamente en la matriz. La función recibe los siguientes parámetros:
# 
# *   Tupla de dos elementos. Indicando dimensiones de la matriz a generar.
# *   Tupla de dos elementos. Indicando el mínimo y máximo de los valores de cada uno de los elementos de la matriz.
# 
# *Ejercicio 4.1*
# 
# Crear dos matrices que con tamaño compatible para realizar la operación de multiplicación y mostrar los resultados en consola.
# 
# 
# *Ejercicio 4.2*
# 
# Crear dos matrices con las mismas dimensiones y realizar la multiplicación elemento por elemento (Hadamard).
# 
# 
# 
# 
# 
# 

# In[ ]:


#Ejercicio 4:

import numpy as np

def matrices(columnas,reenglones,minimo,maximo):
  E=[]
  M=[]
  for i in range(0,reenglones):
    for j in range(0,columnas):
      a = np.random.randint(minimo,maximo)
      E.append(a)
    M.append(E)
    E=[]
  print("Matriz generada= "+str(M))
  return(M)
#4.1 MxN*N*M
print("4.1 MxN*N*M")
A=matrices(3,2,1,10)
B=matrices(2,3,1,5)
C=np.matmul(A,B)
print("Resultado MxN*NxM\n"+str(C))


#4.2 Hadamard
print("4.2 Hadamard")
A=matrices(3,3,1,10)
B=matrices(3,3,1,5)
C=np.multiply(A,B)
print("Resultado Hadamard\n"+str(C))

