#função inicial

#Criando um função do zero

def saudacao():
    print('Saja Bem vind(a)! ')
    print('É um prazer ter você fazendo parte desse curso!')

saudacao()

def saudação(nome, curso='Python'):
    print(f'Saja Bem vind(a) {nome}!')
    print(f'É um prazer ter você fazendo parte desse curso de: {curso}!')

saudação('Paulo', 'Pythom')
saudação('Andreia', 'Programação')
saudação('Aline')
saudação('Alex', 'C++')

def soma(num1, num2):
    return num1 + num2
resultado = soma(5, 7)

print('O resultado da soma é: ', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    
resultado = calculadora(10, 20)

print(resultado)
