#A ideia aqui é fazer um programa que calcula sequências cíclicas
print("Opa, tudo bom meu caro ?\nVamos fazer umas sequências cíclicas ?\nSimbora então!")
word = input("Primeiro me diga qual será a palavra de hoje:\n")
arr = list(word) #Cria um array com a palavra
num = len(arr) #Aqui é a quantidade de letras

quantity = int(input("Qual a posição da letra desejada ?\n"))
#Aqui pegamos o resto da divisão entre a posição e a quantidade de letras, dando a posição da letra
position = quantity % num
letter = arr[position]

print("A letra que se encontra na posição " + str(quantity) + " é: " + str(letter))