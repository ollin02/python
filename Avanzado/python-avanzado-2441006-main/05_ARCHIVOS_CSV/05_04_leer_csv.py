import csv

print("")
print("Con encavezados")
with open("datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)

print("")
print("Sin encavzados")
with open("datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    next(reader)
    for fila in reader:
        print(fila)

print("")
print("Con colunas")
with open("datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    columnas = next(reader)
    print("Columnas", columnas)
    for fila in reader:
        print(fila)

print("")
print("Solo una Columna")
with open("datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    columnas = next(reader)
    print("Columnas", columnas)
    for fila in reader:
        print(fila[0])

print("")
print("Como si fuera un dicionario")
with open("datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila)

print("")
print("Imprimiendo con la llave")
with open("datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila["nombre"])