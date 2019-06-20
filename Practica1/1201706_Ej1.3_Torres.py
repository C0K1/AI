"""
Torres Aragón Juan Jorge IA 2019-1
3. Escribid una función que reciba una tupla compuesta 
por caracteres, y devuelva una lista con los caracteres 
en mayúsculas. Debéis recorrer la tupla carácter a carácter 
para realizar la conversión. Para convertir un carácter a 
mayúscula podéis usar el método upper(). Por ejemplo ’a’.upper() nos devuelve ’A’.
"""
print("1201706 Torres Aragón Juan Jorge IA 2019-1")
L=["a","b","c","d","e"]
C=[]
def mayusculas(L):
    print("Normal "+str(L))
    for elem in L:
        C.append(elem.upper())
    print("Mayusculas "+str(C))
mayusculas(L)