from random import random

x = int(random() * 10) #Numero aleatorio

print("Vamos jogar um jogo, voce consegue adivinhar o numero que estou pensando ?\nDigite o numero que voce acha que estou pensando:")
y = int(input())

while y > x:
    y = int(input("Diminua!\n"))
while y < x:
    y = int(input("Aumente!\n"))
if y == x :
    print("Parabens! você acertou!")
quit()