prova1 = float(input('Digite a nota da prova 1: '))
prova2 = float(input('Digite a nota da prova 2: '))

media = (prova1 + prova2) / 2

if media >= 6:
    print('Parabéns')
    print('Você foi aprovado!')
    print(media)
elif media >= 4:
    print('Você está de recuperação.')
    print(media)
else: 
    print('Você foi reprovado.')
    print(media)