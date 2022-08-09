from random import random

x = int(random() * 10) #Numero aleatorio

print("Vamos jogar um jogo, voce consegue adivinhar o numero que estou pensando ?\nDigite o numero que voce acha que estou pensando:")
y = int(input())

while y != x:
    if y < x:
        y = int(input("Tente novamente, muito baixo\n"))
    elif y > x:
        y = int(input("Tente novamente, muito acima\n"))
    
print("Parabens! voce acertou")
quit()