#Um simlador de supermercado onde o programa irá cadastrar os produtos e no fim irá mostrar:
#O total da compra, quantos produtos custam mais de R$1000 e o nome do produto mais barato.

maior_mil = 0
nome_barato = 'menor'
total = 0

while True:
    print('=-' * 21)
    produto = input('Qual o nome do produto? ')
    valor = float(input('Qual o preço do produto? R$'))
    cont = int(input('[1] Sim\n[2] Não\nDeseja continuar? '))

    while valor > 0:
        total += valor
        break

    while valor > 1000:
        maior_mil += 1
        break

    while valor > 0:
        nome_barato = produto

        while produto < nome_barato:
            produto = nome_barato
        break

    if cont == 1:
        print('Vamos continuar então...'.title())

    else:
        break

print('-=' * 21)
print(f'''O total dessa compra foi de {total}.
{maior_mil} produtos custam mais de R$1000.
E o nome do produto mais barato é {nome_barato}.''')
print('-=' * 21)

print('FIM DO PROGRAMA.')