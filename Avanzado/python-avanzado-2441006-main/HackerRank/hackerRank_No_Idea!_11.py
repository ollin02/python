# Hay una matriz de n enteros. También hay 2 conjuntos disjuntos, A y B, cada uno de los cuales contiene m enteros. 
#Te gustan todos los números enteros del conjunto A y no te gustan todos los números enteros del conjunto B.
# Tu felicidad inicial es 0. Para cada i entero en la matriz, si pertenezco A, sumas 1 a tu felicidad. 
#Si i pertenece a B, sumas -1 a tu felicidad. De lo contrario, tu felicidad no cambia. Salida de su felicidad final al final.
#Nota: Como A y B son conjuntos, no tienen elementos repetidos. Sin embargo, la matriz puede contener elementos duplicados.

#Formato de entrada
#La primera línea contiene números enteros n y m separados por un espacio.
#La segunda línea contiene n enteros, los elementos de la matriz.
#Las líneas tercera y cuarta contienen m enteros, A y B, respectivamente.

#Formato de salida

#Salida de un solo entero, su felicidad total.

#print('Introduce n y m separados por un espacio: ') 
n,m =map(int,input().split())
#print('Introduce los n enteros de la matriz: ')
v=list(map(int,input().split()))
#print('Introduce m enteros de la matriz A: ')
A = set(map(int , input().split()))
#print('Introduce m enteros de la matriz B: ')
B = set(map(int , input().split()))
#print('Su felicidad Total es: ')
print(sum((i in A)-(i in B) for i in v))

       