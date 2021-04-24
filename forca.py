from random import choice
import re
frase = "La promesa que La promesa que Jesus hace en el texto de hoy significa que debemos ser fieles ante cualquier problema. Aguantar ahora nos hace mas fuertes para cuando llegue la gran tribulacion El verdadero valor depende de confiar en Jehova igual que sucede con el aguante Que podemos hacer para confiar mas en el Leer la Biblia todos los dias y reflexionar en como salvo Dios a sus siervos en el pasado"
lista_de_palabras = set(frase.split(" "))
lista = list(lista_de_palabras)
selected_word = choice(lista)
tentativas = 0
chutes = list("_"*len(selected_word))
for w in chutes:
    print(w, end=" ")
print()
while tentativas < 10:
    guess = str(input("Digite a letra que voce acha que está na palavra: "))
    for n, i in enumerate(selected_word):
        if guess == i:
            print(f"Acertou o {i} nas posicao: {n}")
            chutes[n] = guess
        for w in chutes:
            print(w, end=" ")
        print()



