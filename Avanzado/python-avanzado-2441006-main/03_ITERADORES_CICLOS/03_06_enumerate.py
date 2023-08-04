"""
enumerate(iterable, start=0) start es donde iniciara el elemento iterable, puede empezar con el numero que quieras
"""

nombres = ["Paco", "Emilio", "Javier", "Ana"]
nombres_enumerados = enumerate(nombres, start=5)
print(list(nombres_enumerados)) #se pone la función list para que aparesca en formato de lista en la imprecion 
                                #tambien se pone porque al imprimirlo aparece como un objeto de tipo enumerate al hacer la impreción
                                #imprime como una dupla
for indice, elemento in enumerate(nombres):
    print(indice, elemento) 

for indice, elemento in enumerate(nombres):# prueba
    print(indice+5, elemento)