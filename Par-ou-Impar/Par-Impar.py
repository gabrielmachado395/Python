from random import randint
contador = 0
jogador = 0

print('-' * 22)
print('Vamos jogar Par ou Impar.')
print('-' * 22)

while True:
    sistema = randint(1, 10)
    jogador = int(input('Digite um número: '))
    par_impar = int(input('[1] Par\n[2] Impar\nQual você escolhe? '))

    if par_impar == 1:
        if (sistema + jogador) % 2 == 0:
            print('Parabéns, você ganhou.\nVamos jogar de novo...')
            contador += 1

        else:
            print('Que pena, você perdeu.')
            break

    if par_impar == 2:
        if (sistema + jogador) % 3 == 0:
            print('Parabéns, você ganhou.\nVamos jogar de novo...')
            contador += 1

        else:
            print('Que pena, você perdeu.')
            break

    elif par_impar != 1 != 2:
        print('Alternativa inválida. Tente novamente.')

print(f'Você teve {contador} vitorias.')