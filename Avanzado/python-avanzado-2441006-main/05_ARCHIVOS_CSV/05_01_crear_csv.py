import csv
import os

ruta = "csv_vacio.csv"
ruta_absoluta = "D:\\Usuario_Ollin\\Documents\\CV_Ollin\\Curso_Python\\Avanzado\\python-avanzado-2441006-main\\05_ARCHIVOS_CSV\\csv_vacio.csv"
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv")

print(ruta_absoluta)
print(ruta_absoluta_os)


archivo_abierto =open(ruta,"w")
#archivo_abierto = open(ruta_absoluta, "w")
#archivo_abierto = open(ruta_absoluta_os, "w")
writer = csv.writer(archivo_abierto, delimiter=",")
archivo_abierto.close()
