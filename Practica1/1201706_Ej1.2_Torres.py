"""
Torres Aragón Juan Jorge IA 2019-1
2. Escribid una función que, dado un número entero N, 
devuelva una lista con todos los números primos hasta N. 
Para solucionar el ejercicio debéis crear una función auxiliar 
que indique si un determinado número es primo (retornando un valor booleano).
"""
print("1201706 Torres Aragón Juan Jorge IA 2019-1")
Num = 5

def numPrimo(Num):
    for i in range (2,Num-1):
        if(Num % i == 0):
            print(str(Num)+" No es primo")
            return
    print(str(Num)+" Si es primo.")

numPrimo(Num)