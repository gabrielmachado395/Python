#Um sistema que pergunta ao usuário qual o seu sexo.
#Caso o usuário digitar errado o programa irá continuar até uma resposta válida.

sexo = input('''[M]
[F]
Digite seu sexo: ''').strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    sexo = input('Opção invalida. Tente novamente: ').upper()

if sexo == 'M':
    print('Bem-Vindo.')

elif sexo == 'F':
    print('Bem-Vinda')