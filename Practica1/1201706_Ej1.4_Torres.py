"""
Torres Aragón Juan Jorge IA 2019-1
4. Convertid el texto ’ejemplo’ en una lista que contenga 
sus 7 caracteres. Después convertidlo en una tupla y usando 
la función del ejercicio anterior obtened una lista con el 
texto en mayúsculas.
"""
print("1201706 Torres Aragón Juan Jorge IA 2019-1")
E="ejemplo"
C=[]
D=[]
def separacion(L):
    i = len(L)
    for e in range(0,i):
        D.append(L[e])
    print("Nueva cadena: "+str(D))
def mayusculas(L):
    print("Normal "+str(L))
    for elem in L:
        C.append(elem.upper())
    print("Mayusculas "+str(C))
separacion(E)
mayusculas(D)