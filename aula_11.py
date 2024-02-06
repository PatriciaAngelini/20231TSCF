print('Conjuntos\n\n')

# o conjunto funciona como se fosse uma sacola, ou seja, não há
# garantias que o primeiro elemento adicionado será o primeiro
# elemento da coleção
# Porque no conjunto não há indice. São elementos aleatórios
# Todas as operções de procura dentro da sacola precisam ser feitas
# examinando o elemento e não mais sua posição.
# não é indexado
# não permite repeticoes

meuConjunto = {'rosa', 'camelia', 'geranio', 'artemisia'}
print(meuConjunto)
print(type(meuConjunto))

maisumConjunto = {'rosa', 'camelia', 'geranio', 'artemisia', 'geranio'}
print('O conjunto permite repeticoes (2x geranio)?')
print(maisumConjunto)
#O comportamento é não aparecer um erro, mas ele elimina a repeticao

#como o conjunto não é indexado, não é possivel substituir os itens.
#meuConjunto[0] = 'jasmim'
#como o conjunto não é indexado, eu não sei em que posicoes vao estar os itens
# e por isso não é possivel fazer adicao ao final - NAO HÁ APPEND
#mas é ´possivel adicionar elementos na sacola, pois conjunto É MUTÁVEL
#adicionando itens
print('\nConjunto Original')
print(meuConjunto)
meuConjunto.add('jasmim')
print(meuConjunto)

#eliminar itens
print('\nConjunto Original')
print(meuConjunto)
meuConjunto.remove('artemisia')
print(meuConjunto)
meuConjunto.discard('geranio')
print(meuConjunto)
print(meuConjunto)
#o pop é um sorteio de quem ele vai eliminar
meuConjunto.pop()
print(meuConjunto)

#apagando todos os itens do meu conjunto
print('\nLimpando todos os itens')
print(meuConjunto)
meuConjunto.clear()
print(meuConjunto)

print('\nApagando o conjunto')
del meuConjunto

#truque - tenho duplicados na lista, converto para conjunto, ele elimina

minhaLista = ['rosa', 'camelia', 'geranio', 'rosa', 'artemisia', 'geranio']
print(minhaLista)
meuConjunto = set(minhaLista)
print(meuConjunto)

print('\nOperacoes com conjuntos:UNION')
maisumConjunto = {'rosa', 'bromelia', 'orquidea'}
#O UNION continua com as caracteristicas de conjunto, ele ELIMINA OS DUPLICADOS
#mas precisamos criar um novo conjunto
print(meuConjunto)
print(maisumConjunto)
novoConjunto = meuConjunto.union(maisumConjunto)
print(novoConjunto)

#já o metodo UPDATE é aquele que permite modificar o proprio conjunto
print('\nOperacoes com conjuntos:UPDATE')
print(meuConjunto)
print(maisumConjunto)
maisumConjunto.update(meuConjunto)
print(maisumConjunto)

print('\nOperacoes com conjuntos:INTERSECT')
maisumConjunto = {'rosa', 'bromelia', 'orquidea'}
print(meuConjunto)
print(maisumConjunto)
novoConjunto = maisumConjunto.intersection(meuConjunto)
print(novoConjunto)


print('\nOperacoes com conjuntos:INTERSECT-UPDATE')
maisumConjunto = {'rosa', 'bromelia', 'orquidea'}
print(meuConjunto)
print(maisumConjunto)
maisumConjunto.intersection_update(meuConjunto)
print(maisumConjunto)

print('\nOperacoes com conjuntos:diferentes')

meuConjunto = {'rosa', 'camelia', 'geranio', 'artemisia'}
maisumConjunto = {'rosa', 'bromelia', 'orquidea', 'artemisia'}
print(meuConjunto)
print(maisumConjunto)

nossoConjuntoDiferentes = meuConjunto.symmetric_difference(maisumConjunto)
print(nossoConjuntoDiferentes)

print('\nOperacoes com conjuntos:diferentes com update')

meuConjunto = {'rosa', 'camelia', 'geranio', 'artemisia'}
maisumConjunto = {'rosa', 'bromelia', 'orquidea', 'artemisia'}
print(meuConjunto)
print(maisumConjunto)

meuConjunto.symmetric_difference_update(maisumConjunto)
print(meuConjunto)


#o conjunto permite itens de tipos de dados diferentes
print('Outro Conjunto')
outroConjunto = set(('pinheiro', -1, 'camelia'))
print(outroConjunto)


meuConjunto = {'rosa', 'camelia', 'geranio', 'artemisia'}
maisumConjunto = {'rosa', 'bromelia', 'orquidea', 'artemisia'}

if 'bromelia' in maisumConjunto:
    print('Tem bromelia')


# Chegou o dia e você, sua irmã e sua prima estão preparando o salão de festas. Para isso tem
# que descer de carrinho no elevador com todas as coisas para arrumar a festa. Prepare uma
# coleção de coisas que precisa descer. Você está livre para usar o FOR ou o WHILE

# #Gustavo
# colecao = []
# repetir = 'S'
# while repetir == 'S':
#     item = input('Quais itens precisamos descer pelo elevador?')
#     colecao.append(item)
#     repetir = input("Tem mais alguma coisa?").upper()
# novacolecao = set(colecao)
# print(type(novacolecao))
# print(novacolecao)

#professora
colecao = set()
#colecao = {} - dicionario dict()
repetir = 'S'
while repetir == 'S':
    item = input('Quais itens precisamos descer pelo elevador?')
    colecao.add(item)
    repetir = input("Tem mais alguma coisa?").upper()
print(colecao)

if 'guardanapo' in colecao:
    print('Tem guardanapo')
else:
    print('Adicionando guardanapo')
    colecao.add('guardanapo')

colecaoLavabo = {'sabonete liquido', 'toalha', 'papel higienico'}
print(colecaoLavabo)

novacolecao = colecao.union(colecaoLavabo)
print(novacolecao)

if 'talher de prata' in novacolecao:
    print('removendo o talher de prata da lista')
    novacolecao.remove('talher de prata')
    print(novacolecao)

colecaoPrima = {'jarra', 'guardanapo', 'copos', 'pratos'}
print(colecaoPrima)
colecaoRepetidos = novacolecao.intersection(colecaoPrima)
print(colecaoRepetidos)

for elemento in colecaoRepetidos:
    novacolecao.remove(elemento)
print(novacolecao)
novacolecao.update(colecaoPrima)
print(novacolecao)

colecaoMao = {'pano de prato', 'copos', 'fósforo'}

colecaoRepetidos = novacolecao.symmetric_difference(colecaoMao)
for elemento in colecaoRepetidos:
    colecaoMao.remove(elemento)

print(novacolecao)
print(colecaoMao)
novacolecao.update(colecaoMao)
print(novacolecao)