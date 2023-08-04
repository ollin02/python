# forma corta y elegante de generar uan lista en python
"""
lista = [ expresion(elemento) for elemento in objeto_iterable if condición ]
lista = [ expresion(condición) for elemento in objeto_iterable ]
"""

def calcular_cuadrado(numero):
    return numero**2


def es_par(numero):
    return numero % 2 == 0


lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#sintaxis antigüa
lista_cuadrados=[]
for num in lista_num:
    cuadrados = num**2
    lista_cuadrados.append(cuadrados)

print("Cilco for: ", lista_cuadrados)
#fin del metoso antigüo

#nueva forma con listcomprehension
lista_cuadrados = [calcular_cuadrado(num) for num in lista_num]
print("List comprehension: ",lista_cuadrados)

#calcula los cuadrado de los numeros pares
lista_cuadrados_pares = [calcular_cuadrado(num) for num in lista_num if es_par(num)]
print("Cuadrados pares: ",lista_cuadrados_pares)

#verifica si es par o impar y pone un cero cuanso el numerp es impar
lista_resultados = [calcular_cuadrado(num) if es_par(num) else 0 for num in lista_num]
print("Cudrados pares, cero a los impares: ",lista_resultados)