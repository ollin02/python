#programa que une dos cadenas y cuanta el tamaño de la cadena nueva
n=int(input("Escribe el número de personas inscritas al periodico ingles: "))
print("Ingrese el numero de lista de los estudiantes inscritos: ")
k=set(map(int, input().split()))
m=int(input("Escribe el número de personas inscritas al periodico frances: "))
print("Ingrese el numero de lista de los estudiantes inscritos: ")
l=set(map(int,input().split()))

print(f"número total de personas: ",len(k.union(l)))