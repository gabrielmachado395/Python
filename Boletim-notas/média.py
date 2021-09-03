#Um sistema que irá calcular duas notas de um aluno e formar uma média 
#No fim dirá se ele passou de ano, se ele ficou de recuperação ou se ele reprovou.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 5.0:
    print('Que pena, você foi reprovado.')

elif m <= 5.0 or m <= 6.9:
    print('Você está de recuperação, se esforçe.')

elif m >= 7.0:
    print('Parabéns, você foi aprovado.')
