lista_num = [1, 2, 3, 4, 1, 2, 5, 6, 8]

set_pares = {num for num in lista_num if num % 2==0}# las llaves nos indicas que es un set o diccionarios
print(set_pares)# Los sets no contienen valores repetidos

vocales = "aeiou"
                #{llave:valor}
diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}#Diccionario se definen llaves y valor
#.lower() nos convierte un texto en minusculas
#.upper() nos convierte un texto  en mayusculas
#vocal.lower() es la llave
#vocal.upper() es el valor
print(diccionario)