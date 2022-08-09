print("Opa, tudo bom meu caro ?\nVamos fazer umas sequências cíclicas ?\nSimbora então!")
word = input("Primeiro me diga qual será a palavra de hoje:\n")
arr = list(word)
num = len(arr)

quantity = int(input("Qual a posição da letra desejada ?\n"))

position = quantity % num
letter = arr[position]

print("A letra que se encontra na posição " + str(quantity) + " é: " + str(letter))