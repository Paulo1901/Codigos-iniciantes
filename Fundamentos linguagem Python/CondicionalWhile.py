numero_sorteado = 15

numero_escolido = int(input('Informe um numero de 1 a 20: '))

while numero_escolido != numero_sorteado:
    print('Você errou, tente novamente!')

    numero_escolido = int(input('Informe um numero de 1 a 20: '))
 
print('Parabéns você acertou!')

#Exemplo 02 estrutura contadora

contador = 0

while contador < 10: 
    print(contador)
    contador =  contador + 1