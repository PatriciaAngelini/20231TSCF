print("Tabuada")

numero = int(input("Entre com o numero da tabuada a ser exibido: "))

for i in (1,2,3,4,5,6,7,8,9,10):
    tabuada = numero * i
    print(numero, "X", i, "=", tabuada)

#para resolver geracao de numeros nós temos a classe range, que nos ajuda quando
#temos uma "lista" de numeros a ser gerado

print("Tabuada com o range")
for i in range(10):
    tabuada = numero * i
    print(numero, "X", i, "=", tabuada)

print("Tabuada com o range ajustado")
#o range é um gerador de intervalo aberto, ou seja
#se passarmos 1 parametro, ele gera os numeros a partiro do zero até esse numero - 1
#exemplo range(10) = (0,1,2,3,4,5,6,7,8,9)
#se passarmos 2 parametros, o primeiro parametro é de onde ele começa e o segundo
#parametro continua sendo o numero -1
#exemplo range(1, 10) = (1,2,3,4,5,6,7,8,9)
#Para gerar os numeros de 1 a 10 devemos fazer range (1, 11)
for i in range(1,11):
    tabuada = numero * i
    print(numero, "X", i, "=", tabuada)


print("Jogo do PIM")
numero = int(input("Até que numero você gostaria de jogar o PIM? "))

for i in range(1, numero + 1, 1):
    if i % 4 == 0:
        print("PIM")
    else:
        print(f"\t{i}")

print("\n\"fim\"")
print('\n"fim"')


print("Divisivel 5")
n1 = int(input("Entre com o primeiro numero "))
n2 = int(input("Entre com o segundo numero "))

for i in range(n1, n2 + 1):
    if i % 5 == 0:
        print(i)

#Esta solucao nao é correta pois eu nao consigo garantir que o
#primeiro numero seja divisivel por 5

# for i in range(n1, n2 + 1, 5):
#     print(i)


#Victor

print('Contagem regressiva de 60s')
lista = []
for i in range(1,61):
    lista.append(i)
for n in lista:
    print(lista[-n])

#Gustavo
print("******************")
print("*****Contagem*****")
print("******************")
for i in range (60,-1,-1):
    print(i)


print("Divisivel 5")
n1 = int(input("Entre com o primeiro numero "))
n2 = int(input("Entre com o segundo numero "))
divisor = int(input("Entre com o divisor "))

for i in range(n1, n2 + 1):
    if i % divisor == 0:
        print(i)

#Arthur

nm = int(input('Digite um número:'))
print(f'Os números entre 1 e 100 divisiveis por {nm} são: ')
for i in range(1, 101):
    div = i % nm
    if div == 0:
        print(i)


#gustavo Santana
print("Contagem Regressiva While")
i = 61
while i >= 1:
    i -= 1
    print(i)

i = 60
while i > 0:
    print(i)
    i -= 1

# #Pequena introducão as F Strings
#F Strings são a maneira mais moderna de formatar uma string em Python.
# Elas aceitam praticamente todos os tipos de argumentos dentro dela
#

titulo = 'Contagem Regressiva While'
print(titulo)
print(f'{titulo}')
print(f'O titulo é: {titulo}')
print(f'{titulo:^80}')

#
#
novo_titulo = 'oVo TitULO'.upper()
print(novo_titulo)
print(f'{titulo.lower():^60}')
print(f'{titulo:>80}')
fim = 'Este é o fim do titulo '
print('{}   -    {}**{}'.format(titulo, novo_titulo, fim))
print ('\n\n')
titulo = 'Contagem Regressiva While'
novo_titulo = 'NoVo TitULO'
print('titulo: %s'%titulo)
print('titulo: %s %s'%(titulo, novo_titulo))
# #

# Fibo
# 0 1 1 2 3 5 8 13 21
# se eu pedisse para imprimir 4 termos teria que imprimir
# 0 1 1 2
# se eu pedisse 6 termos
# 0 1 1 2 3 5

# a = 0
# b = 1

# soma = a + b (1)
# a = b  (1)
# b = soma (1)

# soma = a + b (2)
# a = b (1)
# b = soma (2)

# soma = a + b (1 + 2 = 3)
# a = b (2)
# b = soma (3)

#Adriano

n = int(input("Digite um numero inteiro:"))
if n <= 0:
    print("O numero deve ser maior que zero")
else:
    a, b, i = 0, 1, 1
    if n == 1:
        print(f'O {n}º termo Fibonacci é {a}')
    else:
        while i < n - 1:
            a,b = b,a + b
            i += 1
        print(f'O {n}º termo Fibonacci é {b}')

#professora
termo = int(input("Qtos termos de Fibo vc quer saber? "))
a, b = 0, 1
if termo <= 0:
    print("Os termos tem que ser maior que zero")
elif termo > 1:
    print(a)
    print(b)
    i = 2
    while i < termo:
        fibo = a + b
        print(fibo)
        a = b
        b = fibo
        i += 1
else:
    print(a)