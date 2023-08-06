print("Programa que calcula la suma, reta y multiplicacion de dos numeros")
print("solo realiza la operacion si los numero se encuentran en el siguiente rango")
print("1<=n<=10^10") 
a=int(input("Introduzca el primer valor: "))
b=int(input("Introduzca el segundo valor: "))

if 1<=a<=10**10:
    if 1<=b<=10**10:
        print(a+b)
        print(a-b)
        print(a*b)

