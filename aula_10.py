#Material aula 08

minhaLista = ['cafe', 'acucar', 'agua']
print(minhaLista)
#0            1         2
#-3         -2      -1
#['cafe', 'acucar', 'agua']
print(minhaLista[0])
print(minhaLista[-1])

pequenaLista=minhaLista[0:2]
print(pequenaLista)

pequenaLista.append('leite')
print(pequenaLista)

pequenaLista.insert(1,'chantilly')
print(pequenaLista)

pequenaLista.pop()
print(pequenaLista)

pequenaLista.pop(1)
print(pequenaLista)

pequenaLista.remove('acucar')
print(pequenaLista)

print(pequenaLista.index('cafe'))

minhaLista = ['cafe', 'acucar', 'agua']

for elemento in minhaLista:
    print(elemento)

if 'cafe' in minhaLista:
    print('Tem cafe')

meusLivros = [['Guia do mochileiro da Galaxia', 300],['Senhor dos Aneis', 4000]]
print(meusLivros)
for carac_livro in meusLivros:
    print(carac_livro)
    print('titulo:',carac_livro[0])


# #Exercicios
# # Acabou a pandemia, chegou o dia e você está ajudando a montar a lista
# # de uma pequena reuniã ono seu a partamento.
# # Conversando com o seu síndico ele proibiu
# # que houvesse mais de 15 pessoas no seu apartamento.
# # Façaum algorimo que peçaa quantidadede pessoas da sua reunião.
# # E utilizando a função FOR peça o nome dos convidados um a um.
# # Certifique-se que seu melhor amigo João está na sua lista
#
# # Falando com a portaria, foi pedido que adicionasse o número do RG em frente cada um dos
# # nomes dos convidados. Altere seu algoritmo para colocar esses documentos na ordem
# # solicitada. Exemplo ['Pat', 345453, 'Hamilton', 924504]
# #Victor
#
# print('Reunião do condomínio com for')
# convidados = []
# convidado = []
# qt_anfitrioes = 2
# num_pessoas = int(input('Quantas pessoas vão para a reunião?: '))
# if num_pessoas > 15 - qt_anfitrioes:
#     print('Convide menos pessoas')
# else:
#     for i in range(1,num_pessoas + 1):
#         nome_convidado = input('Digite o nome da pessoa que vai para a lista: ').upper()
#         convidado.append(nome_convidado)
#         rg_convidado = int(input('Digite o RG da pessoa que vai para a lista: ').upper())
#         convidado.append(rg_convidado)
#         convidados.append(convidado)
#         convidado = []
#     if "JOÃO" in convidados:
#         print(convidados)
#     else:
#         print('João não está na lista')
#
# #Você vai precisar dos nomes em ordem alfabética para poder enviar a portaria. Altere seu
# #algoritmo e ordene a sua lista. Depois apresente o resultado
#
# print(convidados)
# #Esse sort ele modifica a propria lista pois é um método da classe list
# #convidados.sort()
# #print(convidados)
#
# #Mas existe uma funcao built-in do python q tb ordena, sem alterar a lista original
# print(sorted(convidados))
# print('Manteve a ordem da lista original', convidados)
#
# #Outra solucao de adicao de RG na lista
# print('Reunião do condomínio com for')
# convidados = []
# qt_anfitrioes = 2
# num_pessoas = int(input('Quantas pessoas vão para a reunião?: '))
# if num_pessoas > 15 - qt_anfitrioes:
#     print('Convide menos pessoas')
# else:
#     for i in range(1,num_pessoas + 1):
#         nome_convidado = input('Digite o nome da pessoa que vai para a lista: ').upper()
#         convidados.append(nome_convidado)
#
# #Você vai precisar dos nomes em ordem alfabética para poder enviar a portaria. Altere seu
# #algoritmo e ordene a sua lista. Depois apresente o resultado
#
# print(convidados)
# #Esse sort ele modifica a propria lista pois é um método da classe list
# #convidados.sort()
# #print(convidados)
#
# #Mas existe uma funcao built-in do python q tb ordena, sem alterar a lista original
# print(sorted(convidados))
# print('Manteve a ordem da lista original', convidados)
#
# listTmp = []
# for elemento in convidados:
#     convidado_rg = int(input('Entre com o RG do convidado ' + elemento + ' '))
#     listTmp.append(elemento)
#     listTmp.append(convidado_rg)
# print(listTmp)
# convidados = listTmp

# Você percebeu que esse primeira reunião vai passar de 20 pessoas e você alugou o salão de
# festas do seu condomíno. Sendo assim você vai precisar alterar seu algoritmo e agora não
# vai mais utilizar o comando FOR, vai utilizar o comando WHILE e enquanto a resposta da
# pergunta “Tem mais convidados” for igual a SIM você cadastrará um novo amigo na sua lista.


print('Reunião do condomínio com while')
convidados = []
convidado = []
resp = 's'
while resp in ('s', 'sim', 'y', 'yes'):
    nome_convidado = input('Digite o nome da pessoa que vai para a lista: ').upper()
    convidado.append(nome_convidado)
    rg_convidado = int(input('Digite o RG da pessoa que vai para a lista: ').upper())
    convidado.append(rg_convidado)
    convidados.append(convidado)
    convidado = []
    resp = input('Quer cadastrar mais um convidado? ').lower()
print(convidados)

# A cada dia mais perto da sua festa, alguns amigos ainda estão meio noiados com a
# transmissão do virus (e não é para menos com tantas variantes de depois de tantos mortos).
# Seu amigo João é um deles. Infelizmente ele pediu para ser retirado da lista. Remova o João
# a Lista

for elemento in convidados:
    print('elemento', elemento)
    print('nome', elemento[0])
    print('rg', elemento[1])
    if 'JOÃO' in elemento[0]:
        convidados.remove(elemento)
        break
print(convidados)


#Tuplas

#São coleções imutaveis
#Não se pode tirar elementos, nem acrecentar
#Indexaveis
#Permitem repeticao / duplicados
#São muito usadas no for

print('TUPLAS')
minhaTupla = ('sono', 'comida', 'sol', 'cafe', 'sono')
print(minhaTupla)
print(type(minhaTupla))
#Indice maroto
#0          1       2       3       4
#-5         -4      -3      -2      -1
#('sono', 'comida', 'sol', 'cafe', 'sono')
print('Primeiro Item:', minhaTupla[0])
print('Ultimo Item:', minhaTupla[-1])
                         #[de:ate-1]
pequenaTupla = minhaTupla[2:4]
print(pequenaTupla)

print('Tupla de um unico elemento')
pequenaTupla = minhaTupla[2:3]
print(pequenaTupla)
print(type(pequenaTupla))

tuplaUnicaFalsiane = (('falsinha'))
print(tuplaUnicaFalsiane)
print(type(tuplaUnicaFalsiane))

tuplaUnicaVerdadeira = ('verdadeira',)
print(tuplaUnicaVerdadeira)
print(type(tuplaUnicaVerdadeira))

minhaNovaTupla = tuple(('sono', 'comida', 'sol', 'cafe', 'sono'))
print(minhaNovaTupla)

#sera q eu consigo ordernar uma tupla?
#por ela ser imutavel, eu nao consigo ordenar ela modificando-a
#minhaNovaTupla.sort()
#mas eu consigo criar uma NOVA TUPLA ordenada
print(minhaTupla)
minhaNovaTupla = tuple(sorted(minhaTupla))
print(minhaNovaTupla)

#inicializadores
minhaTuplaVazia = ()
print(minhaTuplaVazia)
#nao é usado pq a tupla é imutavel

#usando operadores aritmeticos para CRIAR NOVAS TUPLAS
meusBrinquedos = ('patins', 'bola de basquete', 'skate')
minhasNecessidades = minhaTupla + meusBrinquedos
print(minhasNecessidades)

print('Muitas necessidades')
muitasNecessidades = minhasNecessidades * 5
print(muitasNecessidades)

print(minhaTupla)
#minhaTupla.append('praia')
#simulando o append
minhaTupla = list(minhaTupla)
minhaTupla.append('praia')
minhaTupla = tuple(minhaTupla)
print(minhaTupla)

#todas as manipulacoes de elementos acrescimo(append, insert), retirada(pop, remove, del), sort
#precisam ser convertidos em lista e depois reconvertidos em tupla

if 'praia' in minhaTupla:
    print('Temos praia')
    print('Localizacao', minhaTupla.index('praia'))

print('Tamanho/Quantidade de itens', len(minhaTupla))
del muitasNecessidades
#print(muitasNecessidades)


# # Com esse grande evento você está planejando agora o cardápio. Você deve inicialmente
# # montar uma lista de entradas para que sua irmã possa te ajudar. Monte uma lista com
# # usando o WHILE com todas as delicias gourmets. Não se esqueça de colocar o queijo
# # Roquefort.
# # ▪ Sua irmã não quer providenciar mais nada e para não chateá-la você transformou essa lista
# # em uma coleção imutável. Apresente a coleção
# #Você esqueceu das azeitonas e não tem como pedir para sua irmã providenciar mais nada. A
# # não ser que ela não note que você colocou mais esse item na sua coleção. Para garantir isso
# # coloque a azeitona logo após o queijo Roquefort. Continue o seu algoritmo anterior
# print('Lista de delicias')
# colecaoDelicias = []
# resp = 's'
# while resp in ('s','sim','y','yes'):
#     colecaoDelicias.append(input('Entre com a delicia a ser servida: ').lower())
#     resp = input('Deseja acrescentar mais delicias? ')
# if 'queijo roquefort' in colecaoDelicias:
#     print('Que bom q vc nao esqueceu do queijo')
# colecaoDelicias = tuple(colecaoDelicias)
# print(colecaoDelicias)
#
# if 'queijo roquefort' in colecaoDelicias:
#     indice_roquefort = colecaoDelicias.index('queijo roquefort')
# else:
#     indice_roquefort = len(colecaoDelicias)
# colecaoDelicias = list(colecaoDelicias)
# colecaoDelicias.insert(indice_roquefort + 1, 'azeitonas')
# print(colecaoDelicias)
# colecaoDelicias = tuple(colecaoDelicias)
# print(colecaoDelicias)
#
#
# #A sua prima resolveu ajudar quando sua irmã já estava dando um PITI. Altere seu algoritmo
# #para fornecer uma coleção com os 3 últimos itens da coleção da sua irmã.
# if len(colecaoDelicias) > 3:
#     #comandos equivalentes
#     colecaoPrima = colecaoDelicias[-3:]
#     colecaoPrima = colecaoDelicias[len(colecaoDelicias)-3:len(colecaoDelicias)]
#     print(colecaoPrima)
# else:
#     print('sua irmã da conta')
#
# # Sua prima é muito nova ainda e não tem noção da quantidade de cada item! Você deve
# ajuda-la criando pequenas listas com as quantidades dentro da coleção imutável dela.
# #Adriano
# delicias = [
#     "Banana Split",
#     "Banana Frita",
#     "Banana com calda de Banana",
#     "Banana Flambada",
#     "Queijo Roquefort"
# ]
# delicias.insert(delicias.index("Queijo Roquefort") + 1, "Azeitonas")
# delicias_imutaveis = tuple(delicias)
# ultimas_entradas = delicias[-3:]
# ultimas_entradas_imutaveis = tuple(ultimas_entradas)
# print("Ultiams 3 Delicias Gourmet: ")
# for delicia in ultimas_entradas_imutaveis:
#     print("- " + delicia)
#
# delicias_quant = [
#     2,
#     3,
#     5,
#     2,
#     4,
#     5
# ]
# delcias_com_quantidades = tuple(([delicias[i], delicias_quant[i]] for i in range(len(delicias))))
# print(delcias_com_quantidades)
# print("Delicias Gourmet com Quantidades:")
# for item, quantidade in delcias_com_quantidades:
#     print("- {} ({})".format(item, quantidade))

#Fabio
colecaoDelicias = []
resposta = 's'
while resposta in ('s', 'sim', 'y', 'yes'):
    colecaoDelicias.append(input("Informe um item para o cardápio"))
    resposta = input("Deseja cadastrar mais uma delícia gourmet").lower()
if 'queijo roqueford' in colecaoDelicias:
    indice_roquefort = colecaoDelicias.index('queijo roqueford')
else:
    indice_roquefort = len(colecaoDelicias)
colecaoDelicias.insert(indice_roquefort + 1, 'azeitonas')

if len(colecaoDelicias) > 3:
    colecaoPrima = colecaoDelicias[-3:]
colecaoQtdPrima = []
for delicia in colecaoDelicias:
    quantidade = input("Informe a quantidade de itens de " + delicia).lower()
    colecaoQtdPrima.append([delicia, quantidade])
print(colecaoQtdPrima)
colecaoPrima = tuple(colecaoQtdPrima)
print(colecaoPrima)
colecaoPrimaDuplicada = colecaoPrima * 2
print(colecaoPrimaDuplicada)

print('Entradas Gourmet')
cardapio = []
resp = 's'
while resp in ('s', 'sim', 'y', 'yes'):
    comida = input('Digite o nome da comida: ').upper()
    qtde = int(input('Digite a quantidade da comida que irá: '))
    cardapio.append([comida, qtde])
    resp = input('Vai adicionar mais comida?: ')
if len(cardapio) > 3:
    for i, sublista in enumerate(cardapio):
        if sublista[0] == 'QUEIJO ROQUEFORT':
            indice = cardapio.index(sublista)
            print(sublista)
            print(i, indice)
            cardapio.insert(i+1, ['AZEITONAS', 20])
            break

    nova_colecao = cardapio[-3:]
    cardapio = tuple(cardapio)
    nova_colecao = tuple(nova_colecao)
    print(cardapio)
    print(nova_colecao)
else:
    print('Esqueceu do queijo ou poucos itens no cardápio')