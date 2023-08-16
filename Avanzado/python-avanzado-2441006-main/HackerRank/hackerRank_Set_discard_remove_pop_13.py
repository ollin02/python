#programa que aplica las funciones .pop() .discard() .remove() 
n=int(input("introduce el número de elementos del arreglo: "))
print("Introduce los elementos del arreglos separados por un espacio: ")
s=set(map(int,input().split()))
x=int(input("introduce el número de comandos a realizar: "))

print("Escribe cualquiera de estas palabras pop, remove y discard para llevar acabo las función: ")
for i in range(x):
    y=input().split()
    if y[0]=='pop':
        s.pop()
    elif y[0]=='remove':
        s.remove(int(y[1]))
    elif y[0]=='discard':
        s.discard(int(y[1]))
    
print(sum(s))
