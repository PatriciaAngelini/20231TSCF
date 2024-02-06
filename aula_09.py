# Coleções
# colecoes sao variáveis que armazenam mais de um valor
# elas podem ser de um mesmo tipo ou podem ser de tipos diferentes
# toda colecao é um elemento ITERAVEL
# 
# A primeira coleção que veremos é LISTA
# A mais poderosa e flexivel das coleções
# Ela permite várias operações
# Caracteristicas
# mutaveis, expansiveis, ordenadas,permitem duplicados,
# acomodam tipos diferentes de dados, são acessadas por indice

print('Listas\n')
minhaLista = ['cafe', 'acucar', 'agua']
print(minhaLista)
                #0      #1       #2     #3      #4
minhaLista = ['cafe', 'acucar', 'agua', 'cafe', 'cafe']
print(minhaLista)

print('Criando listas a partir de outra lista')
                         #zero:ate-1
pequenaLista =minhaLista[0:2]
print(pequenaLista)

print('Acessando Elementos')
print('Elemento 0:',minhaLista[0])
print('Elemento 2:',minhaLista[2])

print('Substituindo Elementos')
#   0        #1       #2      #3       #4
#   -5       #-4      #-3     #-2      #-1
#['cafe', 'acucar', 'agua', 'cafe', 'cafe']
print('antes',minhaLista)
minhaLista[3:4+1] = ['canela', 'chantilly']
print('depois',minhaLista)

#   0        #1       #2      #3       #4
#   -5       #-4      #-3     #-2      #-1
#['cafe', 'acucar', 'agua', 'canela', 'chantilly']
print('do elemento 1 até o 2', minhaLista[1:2+1])
print('o ultimo elemento pelo lado positivo', minhaLista[4])
print('o ultimo elemento pelo lado negativo', minhaLista[-1])

print('o primeiro elemento pelo lado positivo', minhaLista[0])
print('o primeiro elemento pelo lado negativo', minhaLista[-5])

print('Slicing do lado negativo do -4 até o -2', minhaLista[-4:-2+1])

print('Acrescentando um elemento no final')
minhaLista.append('baunilha')
print(minhaLista)
print('Acrescentando um elemento numa determinada posicao')
minhaLista.insert(3,'nibs de cacau')
print(minhaLista)
print('Removendo Elementos')
print('Eliminando o ultimo')
minhaLista.pop()
print(minhaLista)
print('Eliminando um item especifico pelo indice')
minhaLista.pop(3)
print(minhaLista)
del minhaLista[-1]
print(minhaLista)
print('Eliminando um item especifico pelo proprio item : canela')
minhaLista.remove('canela')
print(minhaLista)



print('Removendo TODOS elementos')
minhaLista.clear()
print(minhaLista)

minhaLista = ['cafe', 'acucar', 'agua', 'cafe', 'cafe']
print(minhaLista)
print('Eliminando um item especifico pelo proprio item : cafe')
minhaLista.remove('cafe')
#o remove faz um a um
print(minhaLista)

#del minhaLista
#print(minhaLista)

#['cafe', 'acucar', 'agua', 'nibs de cacau', 'canela', 'chantilly']

#Construtures
print('Outra lista')
outraLista = []
print(outraLista)
outraLista = list(('chantilly', 'baunilha'))
print(outraLista)
print(type(outraLista))

print('Extendendo uma lista')
minhaLista = ['cafe', 'acucar', 'agua']
print(minhaLista)
minhaLista.extend(outraLista)
print(minhaLista)

print('Criando uma lista a partir de duas listas')
pequenosMimos=['raspas de limao', 'flor de sal']
minhaListaComplementos = outraLista + pequenosMimos
print('outra lista', outraLista)
print('pequenos mimos', pequenosMimos)
print('minhaListaComplementos', minhaListaComplementos)

print('Achar um item')
print('Descobrindo a localizacao')
onde = minhaLista.index('acucar')
print(minhaLista)
print('Onde esta o acucar?', onde)

if 'chantilly' in minhaLista:
    print('oba tem Chantilly')

print('percorrendo toda a lista e imprimindo os elementos uma a um')
for elemento in minhaLista:
    print(elemento)

print('Ordenar')
# a ordenacao so ocorre se todos os elementos forem do mesmo tipo
minhaLista.sort()
print(minhaLista)

minhaListaDevaneios = ['apresentacao Minsait', 7, True, 'eliminar o cafe']
print(minhaListaDevaneios)
#a ordenacao nao é possivel
#print(minhaListaDevaneios.sort())

#Exercicios
# Acabou a pandemia, chegou o dia e você está ajudando a montara lista
# de uma pequenareuniã ono seu a partamento.
# Conversando com o seu síndico ele proibiu
# que houvesse mais de 15 pessoas no seu apartamento.
# Façaum algorimo que peçaa quantidadede pessoas da sua reunião.
# E utilizando a função FOR peça o nome dos convidados um a um.
# Certifique-se que seu melhor amigo João está na sua lista