#funcio map retorna un objeto de tipo map es un iterador 
def calcular_cuadrado(numero):
    return numero**2


lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = [] # esto sirve para utilizar el cilo for linea 7 a la 13

for num in lista_num:
    cuadrado = calcular_cuadrado(num)
    lista_cuadrados.append(cuadrado)#aqui agregamos el numero a la lista de cuadrados
                                    #.append(nombre, tipo) es un metodo que sirve para agregar al gun 
                                    #elemento a una lista

print(lista_cuadrados)

map_cuadrados = list(map(calcular_cuadrado, lista_num)) # con la funcion map se simplifica la sintaxis
print(map_cuadrados)
