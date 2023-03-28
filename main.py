# Projeto simples em python, jogo adivinhação //  visto no canal "Lilizok4 ASMR" # noqa

from random import randint

seu_nome = input('Olá, qual o seu nome? ')
print(
    f'Okay! {seu_nome}, tente adivinhar qual numero irei escolher! de 1 à 10.')
numero_descoberto = randint(1, 10)
numero_tentativas = 3

for tentativa in range(1, numero_tentativas + 1):
    numero_chutado = int(input('Escolha um número de 1 à 10: '))

    if numero_chutado == numero_descoberto:
        print(
            f'Parabéns !!!, você conseguiu acertar em {tentativa} tentativas!')
        break
      
    elif numero_chutado > numero_descoberto:
        print(
            'VOCÊ ERROU!!! tente um número menor!')
        print(
            f'Você tem {numero_tentativas - tentativa} tentativas...'
        )
    else:
        print(
            'VOCÊ ERROU!!! tente um número maior!')
        print(
            f'Você tem {numero_tentativas - tentativa} tentativas...'
        )

if numero_tentativas : 3
print(f"infelizente você perdeu, o número era {numero_descoberto}.")