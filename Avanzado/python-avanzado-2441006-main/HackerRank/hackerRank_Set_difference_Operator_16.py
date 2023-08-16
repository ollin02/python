#programa que une dos cadenas y genera una nueva con la diferencia etre ellas y 
#cuenta el numero de valores que tiene la nueva cadena
n=int(input("Escribe el número de personas inscritas al periodico ingles: "))
print("Ingrese el numero de lista de los estudiantes inscritos: ")
k=set(map(int, input().split()))
m=int(input("Escribe el número de personas inscritas al periodico frances: "))
print("Ingrese el numero de lista de los estudiantes inscritos: ")
l=set(map(int,input().split()))

print(f"número total de personas: ",len(k-l))