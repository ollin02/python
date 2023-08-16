#programa que cuenta el numero total de elementos de un vector que no estene repetidos

#n=int(input("Introduce el numero total de elementos del arreglo: "))
#c=set()
#for i in range(n): 
#    a=input() 
#    c.add(a) 
#    print(len(c))

print(len(set(input() for c in range(int(input("Introduce el numero total de elementos del arreglo: "))))))