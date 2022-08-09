from random import random

x = int(random() * 10) #Numero aleatorio

print("Adivinhe um numero entre 1 e 10")
y = int(input())

while y != x:
    if y < x:
        y = int(input("Tente novamente, muito baixo\n"))
    elif y > x:
        y = int(input("Tente novamente, muito acima\n"))
    
print("Parabens! voce acertou")
quit()