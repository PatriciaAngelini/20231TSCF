print('Decompondo valores ou Dando o troco')
# valor inicial 96,84
saldo = 96.84
# a ideia é decompor o valor
if saldo > 50:
    qtd_notas_50 = saldo // 50
    print('Qtde de notas de 50:', qtd_notas_50)
    resto = saldo % 50
    print(f'O resto é {resto}')
    saldo = resto

if saldo > 20:
    qtd_notas_20 = saldo // 20
    print('Qtde de notas de 20:', qtd_notas_20)
    resto = saldo % 20
    print(f'O resto é {resto}')
    saldo = resto

# o if para verificacao se o saldo é maior que o valor da nota, nao é necessario
qtd_notas_10 = saldo // 10
print('Qtde de notas de 10:', qtd_notas_10)
resto = saldo % 10
print(f'O resto é {resto}')
saldo = resto

qtd_notas_5 = saldo // 5
print('Qtde de notas de 5:', qtd_notas_5)
saldo = saldo % 5


print('Qtde de notas de 2:', saldo // 2)
saldo = saldo % 2

print('Qtde de moedas de 1:', saldo // 1)
saldo = saldo % 1

#como podemos ver tem um erro de precisao nesse saldo, fazendo com que as casas decimais fiquem enormes
print(f'O resto é {saldo}')

#para corrigir esse erro de precisao, utilizamos a funcao round, que arredonda e limita o numero de casas
saldo = round(saldo, 2)
print(f'O resto é {saldo}')

#testando se a divisao inteira consegue trabalhar com casas decimais.
#consegue sim
print('Qtde de moedas de 0.50:', saldo // 0.50)

#
# se a divisao inteira nao conseguisse trabalhar com casas decimais, bastaria
# transformar minhas moedas em inteiro multiplicando por 100
# saldo = saldo * 100
# print(saldo)
saldo = round(saldo % 0.50, 2)

print('Qtde de moedas de 0.25:', saldo // 0.25)
saldo = round(saldo % 0.25, 2)

print('Qtde de moedas de 0.10:', saldo // 0.10)
saldo = round(saldo % 0.10, 2)

print('Qtde de moedas de 0.05:', saldo // 0.05)
saldo = round(saldo % 0.05, 2)

print('Qtde de moedas de 0.01:', saldo // 0.01)
saldo = round(saldo % 0.01, 2)


#Versao do Gustavo
dinheiro = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
valor_troco = float(input('Qual o valor do troco? '))
for nota in dinheiro:
    while valor_troco >= nota:
        qtd_nota = valor_troco // nota
        print(f"Dar",qtd_nota, "nota de ",nota)
        valor_troco -= nota * qtd_nota

#versao Gustavo modificada
dinheiro = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
valor_troco = float(input('Qual o valor do troco? '))
for nota in dinheiro:
    qtd_nota = valor_troco // nota
    if nota < 2:
        mensagem = f"Dar {qtd_nota} moedas de {nota}"
    else:
        mensagem = f"Dar {qtd_nota} notas de {nota}"
    print(mensagem)
    valor_troco -= nota * qtd_nota

#Versao do Lucas
def saque(valor):
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]
    resultado = []
    for nota in notas:
        qnt_notas = valor // nota
        if qnt_notas > 0:
            resultado.append(f"{int(qnt_notas)} nota(s) de R$ {nota:.2f}")
            valor -= qnt_notas * nota
    for moeda in moedas:
        qnt_moedas = valor // moeda
        if qnt_moedas > 0:
            resultado.append(f"{int(qnt_moedas)} moeda(s) de R$ {moeda:.2f}")
            valor -= qnt_moedas * moeda
    return resultado
while True:
    sacar = float(input("Digite o valor que deseja sacar: R$ "))
    if sacar >= 0:
        resultado = saque(sacar)
        print(f"\nValor a sacar: R$ {sacar}")
        print("\nQuantidade de cédulas e moedas necessárias:")
        for item in resultado:
            print(item)
        break
    else:
        print("ERRO!\nO valor do saque deve ser maior ou igual a zero.")


a = 10
b = 9
c = 8
print(a, b, c)
# apesar de ser natural, essa abordagem fica complicada
# conforme aumenta a quantidade de numeros a ser ordenada
# if a > b:
#     #print(b)
#     if b > c:
#         print(c)
# else:
#     print(a)

# o principio entao é manter a ordem de impressao das variaveis sempre: a, b, c
# e para isso precisamos trocar a ordem dos numeros
if a > b:
    aux = a #10
    a = b #9
    b = aux #10
    print('parcial ab', a, b, c)

if a > c:
    aux = a #9
    a = c #8
    c = aux #9
    print('parcial ac', a, b, c)

if b > c:
    aux = b #10
    b = c #9
    c = aux #10
    print('parcial bc', a, b, c)

print(a, b, c)
