from random import randint
num_palpite = 1

num = int(input('''Eu pensei em um número de 1 à 10. 
Tente adivinhar qual eu pensei: '''))

num_sorteio = randint(1, 10)

if num == num_sorteio:
    print('Parabéns, você acertou de primeira.')

while num != num_sorteio:
    palpite = int(input('''Que pena, você errou!\nTente novamente: '''))
    num_palpite += 1

    if palpite == num_sorteio:
        print('PARABÉNS, VOCÊ ACERTOU!!!\nForam necessárias {} tentativas até você acertar.'
              .format(num_palpite))
        break
