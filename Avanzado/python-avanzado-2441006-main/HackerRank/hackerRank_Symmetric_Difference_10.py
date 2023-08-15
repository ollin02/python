#programa que dado dos conjuntos de enteros,y, imprime su diferencia simétrica en orden ascendente. 
#El término diferencia simétrica indica aquellos valores que existen en M o N pero no existen en ambos.
int(input("Introduzca el tamaño del primer arreglo: "))
m=set(map(int,input().split()))
int(input("Introduzca el tamaño del segundo arreglo: "))
n=set(map(int,input().split()))

print()
if m.union(n) == n.union(m) and m.intersection(n) == n.intersection(m):
    a=sorted(m.union(n)-m.intersection(n))
    for i in a:
        print (i)
