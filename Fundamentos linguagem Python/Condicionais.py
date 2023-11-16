#Estruturas condicionais 

#Exemplo 01

idade = 20

if idade >= 18: 
    print('Você é maior de idade.')
else: 
    print('Você é menor de idade.')

#Exemplo 02

media = float(input('Informe a media do estudante. '))

if media >= 7:
    print(' Parabéns, VOcê foi aprovado! ')
elif media >= 5:
    print('Recuperação')
else:
    print('Você foi reproravado(a). ')

#Exemplo 03

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovado!')
else:
    print('Reprovado!')

