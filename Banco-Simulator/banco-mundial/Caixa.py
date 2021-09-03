#Um simulador de caixa eletrônico onde o programa pergunta o valor que irá ser sacado.
#No fim dirá quantas notas de 50, 20, 10, 1 serão necessárias.

print('=-=' * 11)
print('{:^30}'.format('Banco Mundial'))
print('=-=' * 11)

valor = int(input('Qual o valor você deseja sacar? R$'))

total = valor
ced = 50
total_ced = 0

while True:
    if total >= ced:
        total -= ced
        total_ced += 1

    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R${ced}')

        elif ced == 50:
            ced = 20

        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 1
        total_ced = 0

        if total == 0:
            break
