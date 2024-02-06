#DICIONARIO
#colecoes do tipo chave:valor
#Formulario
#Exemplo
#Nome: Patricia
#Sexo: Feminino
#Idade: 18
#o dicionario é mutavel ou seja eu posso acrescentar e eliminar elementos completos
#elemento aqui é o par chave:valor

print('Dicionario')
meuDicionario = {'nome':'Patricia','sexo':'feminino', 'idade': 18}
print(meuDicionario)
print(type(meuDicionario))

outroDicionario = dict((('nome','Patricia'),('sexo','feminino'),('idade',18),('vacinaCovid', True)))
print(outroDicionario)

print('\nRecuperandoValores')
meuValor = meuDicionario['idade']
print(meuValor)

meuValor = meuDicionario.get('sexo')
print(meuValor)

outroDicionario = dict((('nome','Patricia'),('sexo','feminino'),(18,'idade'),('vacinaCovid', True)))
print(outroDicionario)
meuValor = outroDicionario[18]
print(meuValor)


meuDicionario = {'nome':'Patricia','sexo':'feminino', 'idade': 18}
print(meuDicionario)
print('\nA importancia das chaves')
#uma chave identifica unicamente um valor, ou seja se eu repetir a chave
#o valor é substituido
meuDicionario = {'nome':'Patricia','sexo':'feminino', 'idade': 18, 'nome':'Janaina'}
print(meuDicionario)

print('\nSubstituindo valores - atraves da chave')
meuDicionario['idade'] = 22
print(meuDicionario)

print('\nSubstituindo valores - atraves do update, substitui o elemento todo')
meuDicionario.update({'nome':'Patricia'})
print(meuDicionario)

#o update permite incluir um item, pois caso a chave nao exista, ele inclui
print('\nIncluindo elementos - atraves do update, incluindo o elemento todo')
meuDicionario.update({'estado civil':'casada'})
print(meuDicionario)

print('\nIncluindo elementos')
meuDicionario['tipo Sanguineo'] = 'Orh-'
print(meuDicionario)

print('\nRecuperando todos os valores')
for valor in meuDicionario.values():
    print(valor)

print(meuDicionario.values())

print('\nRecuperando todas as chaves')
for chave in meuDicionario.keys():
    print(chave)

print(meuDicionario.keys())
print('equivalente')
for chave in meuDicionario:
    print(chave)

print('\nRecuperando todos os itens')
for item in meuDicionario.items():
    print(item)

#a dica é essa construcao
for chave, valor in meuDicionario.items():
    print('chave:', chave, 'valor:', valor)

print('\nRecuperando o valor a partir de uma chave')
for chave in meuDicionario:
    print(meuDicionario[chave])

print('\nApagando')
print('antes', meuDicionario)
del meuDicionario['idade']
print(meuDicionario)

print('\ncom popitem  - nao usa indice')
meuDicionario.popitem()
print(meuDicionario)

print('\ncom pop  - usa a chave')
meuDicionario.pop('estado civil')
print(meuDicionario)

print('\nlimpa todos os elementos')
meuDicionario.clear()
print(meuDicionario)

del meuDicionario

meuDicionario = {'nome': 'Patricia', 'sexo': 'feminino', 'idade': 22, 'estado civil': 'casada', 'tipo Sanguineo': 'Orh-'}
print('\nLocalizando um item especifico')
if 'Patricia' in meuDicionario.values():
    print('Achei a Patricia')
if 'tipo Sanguineo' in meuDicionario:
    print('Há informacoes de tipo Sanguineo')

#Como faz muito tempo que vocês não se veem (voce e os convidados) você está
#organizando uma agenda colocando a informação de cada pessoa. Utilize a colecao que
#imita formulario para pegar itens como nome, endereco, telefone, idade
#Gustavo
# print('\nAgenda de Convidados')
# meuDicionario = {'nome': 'n/a','telefone': 'n/a' , 'idade': 'n/a' ,'endereco': 'n/a'}
# nome = str(input("Digite o seu nome: "))
# telefone = int(input("Digite o seu telefone: "))
# idade = int(input("Digite o seu idade: "))
# endereco = str(input("Digite o seu endereco: "))
#
# meuDicionario['nome'] = nome
# meuDicionario['telefone'] = telefone
# meuDicionario['idade'] = idade
# meuDicionario['endereco'] = endereco
# print(meuDicionario)


print('\nAgenda de Convidados')
#meuDicionario = {'nome': 'n/a','telefone': 'n/a' , 'idade': 'n/a' ,'endereco': 'n/a'}
# meuDicionario = {}
# agenda = "S"
# minhaAgenda = []
# while agenda[0] == "S":
#     print("\nDigite os dados do primeiro convidado: ")
#     print()
#     nome = str(input("Digite o seu nome: "))
#     telefone = int(input("Digite o seu telefone: "))
#     # idade = int(input("Digite o seu idade: "))
#     # endereco = str(input("Digite o seu endereco: "))
#     # est_civil = str(input("Digite seu estado civil: "))
#     meuDicionario['nome'] = nome
#     meuDicionario['telefone'] = telefone
#     # meuDicionario['idade'] = idade
#     # meuDicionario['endereco'] = endereco
#     # meuDicionario['estado civil'] = est_civil
#     minhaAgenda.append(meuDicionario.copy())
#     agenda = input("Tem mais convidados para adicionar na agenda?").upper()
# print(minhaAgenda)


            #lista  0                                   1
minhaAgenda = [{'nome': 'pat', 'telefone': 987}, {'nome': 'ro', 'telefone': 987}]
for dicionario in minhaAgenda:
    print(dicionario)
    if 'ro' == dicionario['nome']:
        indice_do_dicionario_na_lista = minhaAgenda.index(dicionario)
        print(indice_do_dicionario_na_lista)
        minhaAgenda.pop(indice_do_dicionario_na_lista)
print(minhaAgenda)

copiaDicionario = meuDicionario.copy()
print(copiaDicionario)
