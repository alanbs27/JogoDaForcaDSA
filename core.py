#Projeto 1 - Desenvolvimento de Game em linguagem python - versão 1

#Import
import random
from os import system, name

#Função para limpar a tela a cada execução
def limpa_tela():

    # windows
    if name == 'nt':
        _= system('cls')

    # Mac ou Linux
    else:
        _= system('clear')

def game():

    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    #Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #Escolhe as palavras aleatórias
    palavra = random.choice(palavras)

    letras_descobertas = ["_" for letra in palavra]

    chances = 6

    letras_erradas = []

    #loop enquanto o numero de chances for maior do que zero
    while chances > 0:

        #print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        #tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        #condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break

    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

limpa_tela()
game()