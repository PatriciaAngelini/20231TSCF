titulo = "Pares de 1 a 600"
print(f'{titulo:^60}')

#for i in range(601): #aqui considera o zero. incorreto.
for i in range(1, 601, 1):
    if i % 2 == 0:
        print(i)


numero = input('Entre um numero')
print(f'{numero[::-1]}')

numero = int(input('Entre um numero '))


digito4 = numero // 1000
print("d",digito4)
numero = numero % 1000
print("num", numero)

digito3 = numero // 100
print("d",digito3)
numero = numero % 100
print("num",numero)


digito2 = numero // 10
print("d",digito2)
numero = numero % 10
print("num",numero)

numero_invertido = str(numero) + str(digito2) + str(digito3) + str(digito4)
print(numero_invertido)

#Yell
num = int(input("Digite o seu número: "))
#i = 0
num_invertido = ''
while num > 0:
    num_invertido = num_invertido + str(num % 10)
    print("num_inv", num_invertido)
    num = num // 10
    print("num", num)
#    i =+ 1
print(num_invertido)

#Arthur
nm = int(input('Digite um número de 4 digitos: '))
x = ''
while nm > 0:
  a = nm % 10
  b = nm // 10
  x = x + str(a)
  nm = b
print(f"o número invertido é {x}")

#Mayara
estado = input('Digite aqui a SIGLA do seu estado: ').upper()
if estado == 'SP':
    print('Paulista')
elif estado == 'MG':
    print('Mineiro')
elif estado == 'RJ':
    print('Fluminense')
elif estado == 'AC':
    print('Acreano')
elif estado == 'AL':
    print('Alagoano')
elif estado == 'AP':
    print('Amapaense')
elif estado == 'AM':
    print('Amazonense')
elif estado == 'BA':
    print('Baiano')
elif estado == 'CE':
    print('Cearense')
elif estado == 'DF':
    print('Brasiliense')
elif estado == 'ES':
    print('Capixaba, espírito-santense')
elif estado == 'GO':
    print('Goiano')
elif estado == 'MA':
    print('Maranhense')
elif estado == 'MT':
    print('Mato Grossense')
elif estado == 'MS':
    print('Sul-mato-grossense')
elif estado == 'PA':
    print('Paraense')
elif estado == 'PB':
    print('Paraibano')
elif estado == 'PR':
    print('Paranaense')
elif estado == 'PE':
    print('Pernambucano')
elif estado == 'PI':
    print('Piauiense')
elif estado == 'RN':
    print('Potiguar')
elif estado == 'RS':
    print('Gaúcho')
elif estado == 'RO':
    print('Rondoniano')
elif estado == 'RR':
    print('Roraimense')
elif estado == 'SC':
    print('Catarinense')
elif estado == 'SE':
    print('Sergipano')
elif estado == 'TO':
    print('Tocantinense')
else:
    print('Estado Inválido')

#Lucas
print("Estados")
estado = input("Qual é a sigla do seu estado? (RJ, SP, MG, BA, CE...) ").upper()
if estado == "RJ":
    print("Carioca")
elif estado == "SP":
    print("Paulista")
elif estado == "MG":
    print("Mineiro")
elif estado == "":
    print("Baiano")
elif estado == "":
    print("Cearense")
else:
    print("Outros estados")


titulo = 'Terca Parte'
print(f'{titulo:^30}')
for i in range(10):
    print(float(input("Entre com um numero "))/3)

#Victor

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
n4 = int(input('Informe o quarto número: '))
n5 = int(input('Informe o quinto número: '))
n6 = int(input('Informe o sexto número: '))
n7 = int(input('Informe o sétimo número: '))
n8 = int(input('Informe o oitavo número: '))
n9 = int(input('Informe o nono número: '))
n10 = int(input('Informe o décimo número: '))
conjunto = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
novo_conjunto = []
for num in conjunto:
    novo_conjunto.append(num/3)
print(novo_conjunto)

titulo = "x elevado a y".capitalize()
print(f'{titulo:^60}')
x = int(input("Entre com um numero "))
y = int(input("Entre com um numero "))
if x < 1 or y < 2:
    print("Numeros Invalidos")
else:
    total = 1
    for i in range(y):
        total = total * x
    print("O numero", x, "elevado a", y, "é igual a", total)

# #Gustavo
print("***********************")
print("*****exponenciação*****")
print("***********************")
x = int(input("DIgite o valor de x: "))
y = int(input("Digite o valor de y: "))
potencia = 1
if x > 1 and y >=2:
    for count in range (1,y+1):
        potencia *= x

        resultado = potencia
    print(f"O resultado da exponenciação é:{x}^{y}={resultado}")
else:
    print(f"Numero invalido! \nDigite um numero inteiro onde x e maior que 1 e y e maior ou igual a 2")


#Comportamento do For
# y = int(input("Digite o valor de y: "))
# for count in range (y):
#     print("for:", count)
#     count += 1
#     print("count meu:", count)
#
# for count in range (1,y+1):
#     print("for ajustado:", count)


#Adriano
titulo = "x elevado a y ".capitalize()
print(f'{titulo:^40}')
x = float(input("Digite o numero maior que 1: "))
y = int(input("Digite um numero maior ou igual a 2: "))
resultado = 1
for i in range(y):
    resultado  *= x
print("O numero", x, "elevado a", y, "é igual a", resultado)


print("Ordenacao 3 numeros")
a = int(input("Entre com um numero"))
b = int(input("Entre com um numero"))
c = int(input("Entre com um numero"))
print(a, b, c)
if a > b:
    aux = a
    a = b
    b = aux

if a > c:
    aux = a
    a = c
    c = aux

if b > c:
    aux = b
    b = c
    c = aux

print(a, b, c)


print("Temporizador")
minutos = int(input("Entre com os minutos:"))
segundos = 0
print(f"{minutos:02d}:{segundos:02d}")
while minutos > 0:
    segundos = 59
    minutos = minutos - 1
    while segundos >= 0:
        print(f"{minutos:02d}:{segundos:02d}")
        segundos = segundos - 1