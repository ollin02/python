lista_nombres = ["Paco", "Emilio", "Javier", "Ana"]

for nombre in lista_nombres: 
    print(nombre)
    if nombre == "Javier": #Si encuentra a Javier termina el ciclo
        break #rompe el ciclo
else:
    print("Ciclo terminado")
