#Conversão de tipo 

idade = '26'
numero1 = '10'
numero2 = '20'

#dessa forma ele irá concatenar o resultado, o tipo de dado está como str
print(numero1 + numero2)

#Exemplo do modo correto
#O resultado sera 26 mais a class será str como resolver?
print(idade, type(idade))

#Modo de conversão de tipo
idade_inteira = int(idade)
print(idade_inteira, type(idade_inteira))

#exemplo pratico
#Nesse caso para realizar essa operação antes do comando input coloque a função do tipo de dado
#No caso coloque para altura float

altura = float (input('Favor insira sua altura: '))
print(altura, type(altura))
