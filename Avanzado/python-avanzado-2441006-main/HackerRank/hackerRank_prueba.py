listaNumeros = []
n=int (input("Por favor, introduzca un número: "))
listaNumeros.append(n)
decision=input("¿Desea añadir mas numeros?: ")

while decision == "s" or decision == "S":
    n=int (input("Por favor, introduzca un número: "))
    listaNumeros.append(n)
    decision=input("¿Desea añadir mas numeros?: ")

print(f"Los números introducidos por el usuario son {listaNumeros}")
input("Por favor, presione una tecla para salir.")
