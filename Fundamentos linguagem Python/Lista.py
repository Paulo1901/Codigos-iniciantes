# Lista

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# com lista 

notas = [7.9, 9.7, 8.2]


# criando listas

lista = []
lista = list()
lista = []

#indexação e slices (tatiamento)

lista = [10, 'Paulo', 3.14159, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

lista.append

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

#interações com FOR 
# utilizando os proprios elementos da lista

for elemento in lista: 
    print(elemento)
    
# utiliazando os indices

print('Comprimento da lista', len(lista))

for i in range(len(lista)):
    print(lista[i])
    
# Metados funções

lista = [1, 3, 12, 8, 2]

print('Antes do append: ', lista)

lista.append(3)

print('Dopois do append: ', lista)

lista.insert(2, 10)

print('Depois do insert: ', lista)

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Depois do extend: ', lista)

lista.pop()

print('Lista após o pop: ', lista)

lista.pop(0)

print('Lista após do pop: ', lista)

lista.remove(3)

print('Depois do remove: ', lista)

print('Quantidade de 2 na lista: ', lista.count(2))
print('Qual o indice do elmento 12: ', lista.index(12))

lista.sort()

print('Com o comando sort: ', lista)

lista.sort(reverse=True)

print('Com o comando reverse: ', lista)


print('Verificar quantos elementos tem na lista: ', len(lista))
print('Verificar a soma dos valores da lista: ', sum(lista))
print('Verifique o valor maximo da lista', max(lista))
print('Verifca o menor valor da lista: ', min(lista))




