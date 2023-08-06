
S = input("Introduce la palabra: ").strip()
S_length = len(S) # DEFINIMOS EL TAMAÑO DE LA PALABRA
player1, player2 = 0,0

for i in range(S_length):
    if S[i] in "AEIOU": # CONDICIONAMOS LOS VALORES DENTRO DEL IF
        player1 += S_length - i #SUMAMOS LAS VECES QUE APARECEN LAS VOCALES
    else:
        player2 += S_length - i #SUMAMOS LAS VECES QUE APARECEN LAS CONSONANATES
             
#Elegimos cual de los sigientes jugadores es el ganador  
if player1 > player2:
    print ("Kevin", player1)
elif player1 < player2:
    print ("Stuart", player2)
else:
    print ("Draw")