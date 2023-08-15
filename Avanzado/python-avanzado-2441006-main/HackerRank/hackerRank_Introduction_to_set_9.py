#Programa que calcula el promedio de una cadena
def average(array):
    return(sum(set(array))/len(set(array)))

n=int(input("introduzca el tamaño de la cadena y la cadena: "))
arr=list(map(int,input().split()))
result=average(arr)
print(result)