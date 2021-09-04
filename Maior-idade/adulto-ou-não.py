#O desafio  é um programa em que o computador irá dizer se o usuário é maior de idade ou não de acordo com seu ano de nascimento.
#Nesse programa usamos a partir de 21 anos para se considerar maior de idade.


from datetime import date
ma = 0
me = 0

for maior in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(maior)))
    ano = date.today().year
    idade = ano - nasc

    if idade >= 21:
        ma += 1

    else:
        me += 1

print('Existem nesse grupo {} pessoas maiores de idade e {} menores de idade.'.format(ma, me))
