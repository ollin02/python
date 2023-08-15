#Programa que recibe una cadena de letras
#que se subdivide en nuevas cadenas y encuentras
#las letras que son semejantes y hace nuevos elementos
def merge_the_tools(string,k):
    s=string
    l=[]
    for i in range(len(s)//k):
        if s==0:
            break
        for j in range(k):
            if s[j] not in l:
                l.append(s[j])
        s=s[k:]
        print("".join(l))
        l.clear()
        



string, k=input("Introduze la cadena: "), int(input("tamaño de la subcadena: "))
print("tamaño de la cadena introducida: ", len(string))
print("tamaño de la subcadena: ",k)
merge_the_tools(string,k)

