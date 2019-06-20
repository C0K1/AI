"""
Torres Aragón Juan Jorge IA 2019-1
5. Escribid una función que, dada una lista de números, 
devuelva una lista con sólo los elementos en posición par.
"""
print("1201706 Torres Aragón Juan Jorge IA 2019-1")
Lista1 = {1,2,3,4,5,6,7,8,9}
def par_impar_funcion(Arreglo):
        for e in Arreglo:
            if e %2 == 0:
                print(str(e)+" Es numero par\n")
            else:
                print(str(e)+" Es numero impar.\n")

par_impar_funcion(Lista1)
