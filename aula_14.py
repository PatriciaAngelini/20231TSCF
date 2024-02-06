#Exceções
# é a interrupção do fluxo normal de execução de um algoritmo
# acontece quando há um ERRO em tempo de EXECUÇÃO do programa

#programa base
titulo = 'Programa que calcula a media de compra no supermercado'
print(f'{titulo:^50}')

valor = float(input('Entre com o valor total da sua compra:'))
qtd_itens = int(input('Entre com a qtde total de itens:'))

preco_medio = valor/qtd_itens
print(f'O preço medio das compras é R${preco_medio:.2f}')
#fim do programa base

#programa resolvendo a exceção sem bloco try except
titulo = 'Programa que calcula a media de compra no supermercado'
print(f'{titulo:^50}')

valor = float(input('Entre com o valor total da sua compra:'))
qtd_itens = int(input('Entre com a qtde total de itens:'))

if qtd_itens > 0:
    preco_medio = valor/qtd_itens
    print(f'O preço medio das compras é R${preco_medio:.2f}')

fim do programa base

#programa com 1o nivel de tratamento de execoes
titulo = 'Programa que calcula a media de compra no supermercado'
print(f'{titulo:^50}')

try:
    valor = float(input('Entre com o valor total da sua compra:'))
    qtd_itens = int(input('Entre com a qtde total de itens:'))

    preco_medio = valor/qtd_itens
    print(f'O preço medio das compras é R${preco_medio:.2f}')
except:
    print('Houve uma exceção')


#programa com 2o nivel de tratamento de excecoes - tratando uma a uma
titulo = 'Programa que calcula a media de compra no supermercado'
print(f'{titulo:^50}')

try:
    valor = float(input('Entre com o valor total da sua compra:'))
    qtd_itens = int(input('Entre com a qtde total de itens:'))

    preco_medio = valor/qtd_itens
    print(f'O preço medio das compras é R${preco_medio:.2f}')
except ZeroDivisionError:
    print('Houve uma divisao por zero. Entre com uma quantidade diferente de zero')
except ValueError:
    print('Entre com um valor valido')


#programa com 3o nivel de tratamento de excecoes - tratando uma a uma + excecao generica
titulo = 'Programa que calcula a media de compra no supermercado'
print(f'{titulo:^50}')

try:
    valor = float(input('Entre com o valor total da sua compra:'))
    qtd_itens = int(input('Entre com a qtde total de itens:'))

    preco_medio = valor/qtd_itens
    print(f'O preço medio das compras é R${preco_medio:.2f}')
except ZeroDivisionError:
    print('Houve uma divisao por zero. Entre com uma quantidade diferente de zero')
except ValueError:
    print('Entre com um valor valido')
except Exception as e:
    print(f'Houve uma exceção:{e.__class__.__name__}:{e}')

#programa com 4o nivel de tratamento de excecoes
# - tratando uma a uma + excecao generica
# usando o bloco else e o bloco finally

titulo = 'Programa que calcula a media de compra no supermercado'
print(f'{titulo:^50}')

try:
    preco_medio = 0.0
    valor = float(input('Entre com o valor total da sua compra:'))
    qtd_itens = int(input('Entre com a qtde total de itens:'))

    preco_medio = valor/qtd_itens

except ZeroDivisionError:
    print('Houve uma divisao por zero. Entre com uma quantidade diferente de zero')
except ValueError:
    print('Entre com um valor valido')
except Exception as e:
    print(f'Houve uma exceção:{e.__class__.__name__}:{e}')
else: #o bloco else só é executado quando nao há nenhum tipo de exceção
    if preco_medio > 10:
        resp = input('Voce gostaria de participar do programa de pontos?:').lower()
        if resp in ('s', 'sim'):
            print('Obrigada por participar')
finally: #o bloco finally é executado sempre!
    print(f'O preço medio das compras é R${preco_medio:.2f}')

#programa com 5o nivel de tratamento de excecoes
# - tratando uma a uma + excecao generica
# usando o bloco else e o bloco finally
# COM LANCAMENTO / CRIACAO de exceões
titulo = 'Programa que calcula a media de compra no supermercado'
print(f'{titulo:^50}')

class NumeroNegativo(Exception):
    pass
try:
    preco_medio = 0.0
    valor = float(input('Entre com o valor total da sua compra:'))
    qtd_itens = int(input('Entre com a qtde total de itens:'))

    if valor < 0 or qtd_itens < 0:
        raise NumeroNegativo('Voce entrou com o numero negativo')

    preco_medio = valor/qtd_itens

except ZeroDivisionError:
    print('Houve uma divisao por zero. Entre com uma quantidade diferente de zero')
except ValueError:
    print('Entre com um valor valido')
except Exception as e:
    print(f'Houve uma exceção:{e.__class__.__name__}:{e}')
else: #o bloco else só é executado quando nao há nenhum tipo de exceção
    if preco_medio > 10:
        resp = input('Voce gostaria de participar do programa de pontos?:').lower()
        if resp in ('s', 'sim'):
            print('Obrigada por participar')
finally: #o bloco finally é executado sempre!
    print(f'O preço medio das compras é R${preco_medio:.2f}')

#programa com 6o nivel com lancamento mas sem tratamento

titulo = 'Programa que calcula a media de compra no supermercado'
print(f'{titulo:^50}')

class NumeroNegativo(Exception):
    pass

preco_medio = 0.0
valor = float(input('Entre com o valor total da sua compra:'))
qtd_itens = int(input('Entre com a qtde total de itens:'))

if valor < 0 or qtd_itens < 0:
    raise NumeroNegativo('Voce entrou com o numero negativo')

preco_medio = valor/qtd_itens

print(f'O preço medio das compras é R${preco_medio:.2f}')


Elabore um algoritmo que leia dois números e imprima qual é maior, qual é
menor; Se eles forem iguais lance uma exceção e termine o programa;
#Gustavo

class NumerosIguaisException(Exception):
    pass
try:
    x1 = float(input('Digite o valor um: '))
    x2 = float(input('Digite o valor dois: '))
    if x1 > x2:
        print(f'O número {x1} é maior que o número {x2}')
    elif x1 < x2:
        print(f'O número {x2} é maior que o número {x1}')
    else:
        raise NumerosIguaisException('Você entrou com dois números iguais')
except ValueError as v:
    print('Por favor, digite valores numéricos válidos.')
except NumerosIguaisException as e:
    print(e)
except Exception as e:
    print(f'Houve um erro: {e}')

#outra possibilidade da professora
class NumerosIguaisException(Exception):
    pass
try:
    x1 = float(input('Digite o valor um: '))
    x2 = float(input('Digite o valor dois: '))
    if x1 > x2:
        print(f'O número {x1} é maior que o número {x2}')
    elif x1 < x2:
        print(f'O número {x2} é maior que o número {x1}')
    else:
        #raise NumerosIguaisException('Você entrou com dois números iguais')
        raise ValueError ('Entre com numeros diferentes')
except ValueError as v:
    #print('Por favor, digite valores numéricos válidos.')
    print(v)
except NumerosIguaisException as e:
    print(e)
except Exception as e:
    print(f'Houve um erro: {e}')


# Elabore um algoritmo que leia as 5 primeiras letras do alfabeto (ou A, ou B, ou C,
# ou D) e o e imprima um nome de fruta que comece com essa letra. Caso seja
# digitado um uma outra letra, deverá ser lançada uma exceção;

#1 versao
class FrutaInvalida(Exception):
    pass

fruta = input('Entre com uma letra A, B, C ou D: ').lower()

try:
    if fruta == 'a':
        print('Abacaxi')
    elif fruta == 'b':
        print('Banana')
    elif fruta == 'c':
        print('Caqui')
    elif fruta == 'd':
        print('Damasco')
    elif fruta == 'e':
        print('Embauba')
    else:
        raise FrutaInvalida('Entre com uma letra de A a E')
except Exception as e:
    print(f'Houve uma exceção, informe seu dev: {e.__class__.__name__}:{e}')

#2 versao
try:
    frutasDic = {'a':'Abacaxi', 'b':'Banana', 'c':'Caqui', 'd':'Damasco', 'e':'Embauba'}
    letra = input('Entre com uma letra A, B, C ou D: ').lower()
    minhaFruta = frutasDic[letra]
    print(f'Minha Fruta é {minhaFruta}')
except KeyError:
    print('Entre com uma letra de A a E')
except Exception as e:
    print(f'Houve uma exceção, informe seu dev: {e.__class__.__name__}:{e}')


#Gustavo
# EXERCICIO 2 - Elabore um algoritmo que leia as 5 primeiras letras do alfabeto (ou A ou B, ou C, ou D)
# e imprima um nome de fruta que comece com essa letra. Caso seja digitado uma outra letra,
# deverá ser lançada uma exceção
entrada = 'A'
class LetraErradaException(Exception):
    pass
while entrada == 'A' or 'B' or 'C' or 'D' or 'E': #in ('A', 'B')
    try:
        entrada = str(input('Digite as 5 primeiras letras do alfabeto: ')).upper()
        if entrada == 'A':
            print('Amora')
        elif entrada == 'B':
            print('Banana')
        elif entrada == 'C':
            print('Cacau')
        elif entrada == 'D':
            print('Damasco')
        elif entrada == 'E':
            print('Embu')
        else:
            raise LetraErradaException('Você entrou com valores incorretos e fora das 5 primeiras letras do alfabeto')
    except:
        print('Ta errado meu amigo(a)')
        break


# Para vários tributos, a base de cálculo é o salário mínimo. Elabore um algoritmo
# que leia o valor do salário mínimo e o valor do salário de uma pessoa. Calcular e
# imprimir quantos salários mínimos essa pessoa ganha; Lance tratamentos de
# exceção condizentes

titulo = 'Programa que calcula a quantidade de salarios minimos'
print(f'{titulo:^50}')

class NumeroNegativo(Exception):
    pass
try:
    salario_minimo = 1550
    qtd_salario_minimo = 0.0
    salario = float(input('Entre com o valor bruto do salario:'))
    salario_informado = float(input('O salario minimo atual está em R$1550,00. Se quiser informe outro valor:'))

    if salario_informado != salario_minimo:
        salario_minimo = salario_informado

    if salario < 0 or salario_minimo < 0:
        raise NumeroNegativo('Voce entrou com o numero negativo')

    qtd_salario_minimo = salario/salario_minimo

except ZeroDivisionError:
    print('Houve uma divisao por zero. Entre com uma quantidade diferente de zero')
except ValueError:
    print('Entre com um valor valido')
except Exception as e:
    print(f'Houve uma exceção:{e.__class__.__name__}:{e}')
finally: #o bloco finally é executado sempre!
    print(f'O preço medio das compras é R${qtd_salario_minimo:.2f}')
