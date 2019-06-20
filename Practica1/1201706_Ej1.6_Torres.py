"""
Torres Aragón Juan Jorge IA 2019-1
6. Extended la función anterior para que, dada una 
lista y unos índices, nos devuelva la lista resultado 
de coger sólo los elementos indicados por los índices. 
Por ejemplo si tenemos la lista [1,2,3,4,5,6] y los 
índices [0,1,3] debería devolver la lista [1,2,4]
"""
print("1201706 Torres Aragón Juan Jorge IA 2019-1")
Lista1 = [1,2,3,4,5,6,7]
Indice = [0,1,3]
def Posiciones(Arreglo,posicion):
    C = []
    for e in range(len(Arreglo)):
        for x in posicion:
            if x==e:
                C.append(Arreglo[x])
                break
    print(C)
                
Posiciones(Lista1,Indice)
