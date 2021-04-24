from random import choice

class Forca:
    def __init__(self):
        self.__palabras = ('Mateo', 'Pedro', 'Andres', 'Santiago', 'Bartolome', 'Juan', 'Santiago', 'Judas', 'Tome', 'Felipe', 'Simon')
        self.lista = list(self.__palabras)
        self.selected_word = choice(self.lista)
        self.tentativas = 0
        self.chutes = []
        
        
    def palabras(self):
        return self.__palabras
        
    def menu(self):
        while True:
            print('=='*30)
            print(f'{"La palabra abajo es el nombre de un apostol de Jesus":^60}')
            print(f'{"Vamos descobrir cual es?":^60}')
            print('=='*30)
            opcion = input("Elija la opcion:\n(1) Jugar\n(2) Salir\nElija tu opcion: ")
            if opcion == '2':
                break
            elif opcion == '1':
                self.juego()
            else:
                print('Opcion invalida')
                continue
        print('Finalizado')
        exit()
        
    def juego(self):
        self.selected_word = self.selected_word.lower()
        self.chutes = list("_"*len(self.selected_word))
        for w in self.chutes:
            print(w, end=" ")
        print()
        while self.tentativas <= 5:
            guess = str(input("Digite a letra que voce acha que está na palavra: "))
            for n, i in enumerate(self.selected_word):
                if guess == i:
                    print(f"Acertou o {i} nas posicao: {n}")
                    self.chutes[n] = guess
            if guess not in self.selected_word:
                self.tentativas += 1
                print(f'"{guess}" no esta en la pababra. Tenes {5 - self.tentativas} restantes')
                
            for w in self.chutes:
                print(w, end=" ")
            print()
            
            if not '_' in self.chutes:
                print('Parabes!! Voce acertou a palavra!!!')
                print('Quer jogar outra vez?')
                self.menu()
        print('Voce perdeu!\nQuer tentar outra vez?')
        self.menu()
                
            
forca = Forca()
forca.menu()
