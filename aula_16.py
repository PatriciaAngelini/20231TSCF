#Funcoes

#sao pedacos de codigo, divididos para organizar o projeto
#reaproveitamento
#especializacao
#separacao do escopo (em outras linguagens + estruturadas)

#em python a nomenclatura é tudo junto e misturado
#mas usualmente chamamos
#PROCEDURE ou PROCEDIMENTO o trecho de codigo q nao retorna valor
#FUNCTION ou FUNCAO aquilo que retorna valor

#normalmente na organizacao do codigo definimos (def) as funcoes
#no começo do nosso arquivo .py, para entao usar no restante do programa
#porque?
#pq o python precisa conhecer o nome da funcao antes de usar

#aqui definimos o que a funcao vai fazer
#na realidade temos o PROCEDIMENTO OlaMundo, pois ele não retorna valor
#ele apenas executa uma ação (a de imprimir)
def OlaMundo ():
    print('Ola Mundo')
#aqui estamos fazendo uso da funcao
OlaMundo()

def Soma2():
    #o escopo da variavel xpto é um escopo local,
    # ou seja essa variavel foi definida dentro da funcao
    xpto=1+2
    print(xpto)
Soma2()

#variavel global
x=100
def fImpressao():
    #o python enxerga a variavel global
    print(x)

fImpressao()

#a passagem de parametros é uma boa pratica,
# já que com isso nao modificamos/usamos as variaveis globais

def fImpressao2(p1):
    print(p1)

fImpressao2(150)

#parametros default
#parametros default sao aqueles q se eu nao passar um valor na hora da execucao
#ele tem um valor padrao que é utilizado
#para eu especificar um valor padrao,
# basta passar uma igualdade na definicao da funcao
print('\n')
def fSomaPadrao(p1, p2=100):
    soma = p1 + p2
    print(soma)

fSomaPadrao(10, 5)
fSomaPadrao(8)

#transformando em funcao, ou seja retornando valor
print('\n')
def fSomaPadraoRetorno(p1, p2=100):
    soma = p1 + p2
    return(soma)

print(fSomaPadraoRetorno(3,4))

#quando a gente tem um numero de parametros,
# precisamos passar todos parametros
# a nao ser quando tenhamos default
def fSoma3(p1, p2, p3):
    soma = p1+p2+p3
    return (soma)

#isso nao é possivel
#print(fSoma3(1,1))

#tb nao consiguimos espeficar parametros default no "meio"
#pq eles sao posicionais
#isso nao é possivel
# def fSoma3default(p1, p2 = 4, p3):
#     soma = p1+p2+p3
#     return (soma)

#parametros default somente no final
def fSoma3default(p1, p2 = 4, p3 = 8):
    soma = p1+p2+p3
    return (soma)
print(f'\n{fSoma3default(45)}')

#muitas vezes precisamos definir uma funcao com numero de parametros variavel
#isso é python é possivel, bastando especificar o parametro com o simbolo de *
#a partir dai o python vai tratar esse parametro como uma colecao

def fSomaLote(*p):
    soma = 0
    for elemento in p:
        soma += elemento
    return (soma)

print('\n\n')
print(fSomaLote(1))
print(fSomaLote(1, 3))
print(fSomaLote(1, 8, 234, 2, 56, 4))

#crie uma funcao que entra com numero de parametros variaveis em multiplica

#Cria uma função que entra com numero de parametros variaveis e multiplica
#Gustavo
def fMultLote(*p):
    multiplicacao = 1
    for elemento in p:
        multiplicacao *= elemento
    return (multiplicacao)
print(fMultLote(2,8,7))

def fSomaLote(*p):
    multiplica = 1
    for elemento in p:
        multiplica *= elemento
    return (multiplica)
print(fSomaLote(1,5, 8))

#o python permite que especifiquemos uma funcao com numero de parametros variavel
#colocando numa estrutura chave/valor (internamente é um dicionario)

def fApresentacao (**p):
    print(f'Ola amigo {p["primeiro"]}')
    print(f'Ola amigo {p["segundo"]}')

fApresentacao(primeiro='Gustavo', segundo='Adriano')

#Map
#calculando desconto de 20%
def fDesconto(valor, desconto = 0.2):
    if desconto > 1:
        desconto = desconto / 100
    return(valor - valor * desconto)

print('Descontos')
print(fDesconto(45))
print(fDesconto(45, 10))

#suponha que eu tenha uma lista de precos e queira aplicar
# 20% de desconto em toda lista
print('Lista de precos com desconto')
listaPrecos = [23, 12, 55, 8, 120]
for elemento in listaPrecos:
    print(fDesconto(elemento))

#o python incorporou esse "loop" dentro da funcao MAP
#para criar uma nova colecao de precos descontados, basta chamar a funcao MAP,
#passando a colecao orginal
print('Lista de precos com desconto usando o MAP')
listaPrecos = [23, 12, 55, 8, 120]
print(listaPrecos)
listaPrecosBlack = list(map(fDesconto, listaPrecos))
print(listaPrecosBlack)


#decompondo o raciocinio
#calculando desconto de 20%
def fDesconto(valor, desconto = 0.2):
    if desconto > 1:
        desconto = desconto / 100
    return(valor - valor * desconto)
print(fDesconto(60, 50))
print('Lista de precos com desconto usando o MAP')
listaPrecos = [23, 12, 55, 8, 120]
listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]
print(listaPrecos)
listaPrecosBlack = list(map(fDesconto, listaPrecos, [50, 50, 50, 50, 50]))
print(listaPrecosBlack)
listaPrecosBlack = list(map(fDesconto, listaPrecos, listaDescontos))
print(listaPrecosBlack)


def fSoma3(p1, p2, p3):
    soma = p1+p2+p3
    return (soma)
print(f'\n{fSoma3(45, 10, 10)}')

#As funcoes LAMBDA são funcoes de 1 linha,
# para serem definidas e usadas imediatamente
#Normalmente nao definimos um nome para essa funcao,
# pois ela funciona como se fosse uma variavel
#Mas quando precisamos utilizar a funcao em varios trechos
#do codigo podemos atribuir uma variavel
print('Transformando uma funcao comum em uma lambda com nome')
lSoma3 = lambda p1, p2, p3: p1+p2+p3
print(lSoma3(10, 10, 10))
print('Transformando uma funcao comum em uma lambda para uso direto')
print((lambda p1, p2, p3: p1+p2+p3)(20,20,20))
print('Criando uma funcao lambda com condicional')
lMaior = lambda x, y: x if x>y else y
print('O maior numero é', lMaior(4,3))
lMaiorStr = lambda x, y: 'O maior é ' + str(x) if x>y else 'O maior é ' + str(y)
print(lMaiorStr(5,6))

#Retorne o oposto de um número
#Oposto é vc inverter o sinal
lOposto = lambda x: -x
print(f'O oposto do numero 10 é {lOposto(10)}')

print(f'\nExercicios')
print(f'\n 1° Exercicio')

lOposto = lambda x: x - (2*x)
print(lOposto(5))


print(f'\n 2° Exercicio')
lInverso = lambda x: 1/x
print(lInverso(6))


print(f'\n 3° Exercicio')
lMetade = lambda x: x/2
print(lMetade(6))

print(f'\n 4° Exercicio')
lQuadrado = lambda x, y: (x**2) + (y**2)
print(lQuadrado(6,1))

print(f'\n 5° Exercicio')
lEsfera = lambda r: 4/(3*3.14) * (r**3)
print(lEsfera(6))

print(f'\n 6° Exercicio')
print((lambda nome, idade: 'Nome: '+ nome + ' Idade: '+str(idade))('Patricia', 52))

#Lamba e MAP sao o casamento perfeito
print('Lambda e Map')
listaOriginal = [10, 20, 95, 8, 76]
print(listaOriginal)
lMetade = lambda x: x/2
listaMetade = list(map(lMetade, listaOriginal))
print(listaMetade)
print('Usando o lambda dentro do map')
listaMetade = list(map((lambda x: x/2), listaOriginal))
print(listaMetade)

#Dada a lista abaixo, retorne uma outra lista com os proprios numeros se eles forem par
listaOriginal = [234, 64, 13467, 45.89, 23]
print(listaOriginal)
lbPar = lambda x: x if x % 2 == 0 else None
listaPares = list(map(lbPar, listaOriginal))
print(listaPares)
