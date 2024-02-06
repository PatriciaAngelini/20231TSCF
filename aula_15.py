#Manipulacao de arquivos
#O python tem em sua biblioteca nativa algumas funcoes para
# ABERTURA E FECHAMENTO DE ARQUIVOS
# LEITURA
# ESCRITA

#Vamos tratar dois tipos de arquivo .txt e o .csv
#No material de aula temos o tipo .JSON

#Para manipular qq arquivo no sistema operacional precisamos
# sinalizar que estamos fazendo essa maninpulacao
#Assim nasce a funcao de ABERTURA de ARQUIVOS
print('Abrindo o arquivo')
arqAlunos = open('alunos_idade.txt', 'r', encoding='UTF-8')

print('Imprimindo Linhas')
linha = arqAlunos.readline()
print(linha)
linha = arqAlunos.readline()
print(linha)

print('Imprimindo o restante das Linhas com for')
for linha in arqAlunos:
    print(linha)

#para eu voltar a ler o arquivo desde o inicio
# eu preciso voltar o cursor para a posicao inicial

print('Ler arquivo a partir do inicio')
arqAlunos.seek(0)
print(arqAlunos.readline())

#colocando o arquivo em uma colecao do tipo lista
listaLinhas = arqAlunos.readlines()
print(listaLinhas)

print('Linha 2:', listaLinhas[2])

print('Ler o arquivo a partir de uma posicao e ate o fim da linha')
arqAlunos.seek(104)
print(arqAlunos.readline())

#temos o recurso de ler o arquivo to do e colocar em memoria
#ATENCAO: isso só é legal em arquivos pequenos, pq vc pode sobrecarregar a memoria
print('Imprindo o arquivo completo')
arqAlunos.seek(0)
texto = arqAlunos.read()
print(texto)

print('Descobrindo a localizacao do meu cursor apos uma leitura')
print('posicao:',arqAlunos.tell())

#quando lemos o arquivo inteiro, podemos usar as funcoes de slicing
#slicing divide um pedaco da string / texto
#variavel[incio:fim:passo]
#passo = pulo

print('Lendo um trecho do arquivo')
arqAlunos.seek(0) #posicionado o arquivo no inicio
texto = arqAlunos.read(50)
print(texto)

#fazendo o mesmo agora com a funcao de slicing
arqAlunos.seek(0)
texto = arqAlunos.read()
trechoTexto = texto[0:49] #lendo 50 posicoes
print(trechoTexto)

#se abrimos um arquivo temos A OBRIGACAO DE FECHAR O ARQUIVO
print('Fechando o Arquivo')
arqAlunos.close()
print('Verificando se o arquivo esta fechado')
if arqAlunos.closed:
    print('Arquivo fechado')

#Vamos escrever o nosso primeiro arquivo
arqOlaMundo = open('ola_mundo.txt', 'a')

print('Escrevendo uma frase no arquivo Ola Mundo')
arqOlaMundo.write('Ola Mundo ')
arqOlaMundo.write('Bem vindo')
arqOlaMundo.write('\n')
arqOlaMundo.write('Pat e \n')
arqOlaMundo.write('Rafael')

arqOlaMundo.close()

#assim como temos a escrita de uma linha com write q equivale a o readline
#temos tambem a escrita de uma colecao de linhas com o writelines q equivale ao readlines

print('Escrevendo um arquivo a partir de uma lista')
listaHobby = ['estudar', 'ler', 'jogar basquete', 'viajar']
arqHobby = open('arq_hobby.txt', 'w')
arqHobby.writelines(listaHobby)
arqHobby.close()

print('Escrevendo um arquivo a partir de uma lista com quebra de linha')
listaHobby = ['\n','estudar', '\n', 'ler\n', 'jogar basquete','\n', 'viajar']
arqHobby = open('arq_hobby.txt', 'a')
arqHobby.writelines(listaHobby)
arqHobby.close()

#tudo q fizemos ate agora é com as funç~es built-in do python
#mas se quisermos manipular dados em arquivos mais especializados podemos ]
#utilizar outras bibliotecas
#para arquivos do tipo .csv vamos usar a biblioteca .csv

import csv

print('Abrir o arquivo e usar a biblioteca especializada para pegar o conteudo')
arqAlunos = open('alunos_idade.csv', 'r', encoding='UTF-8')
csvTabAluno = csv.reader(arqAlunos, delimiter = ';')
#esse print nao funciona pois estamos tentando imprimir um objeto
print(csvTabAluno)
for linha in csvTabAluno:
    print(linha)
arqAlunos.close()

#para nao cometermos o sacrilegio de nao fecharmos um arquivo o python
# disponibiliza a funcao with que faz a abertura e o fechamento fica implicito
#arqAlunos = open('alunos_idade.csv', 'r', encoding='UTF-8')
print('Abrindo arquivo com o with e transformando em lista de listas')
with open('alunos_idade.csv', 'r', encoding='UTF-8') as arqAlunos:
    csvTabAluno = csv.reader(arqAlunos, delimiter = ';')
    listaAlunos = list(csvTabAluno)
    print(listaAlunos)
    print('Imprimindo a 1a linha - header', listaAlunos[0])
    print('Imprimindo a 1a linha - dados', listaAlunos[1])
    print('Imprimindo a uma coluna especifica', listaAlunos[2][1])
    for linha in listaAlunos:
        print(linha)


print('Abrindo arquivo com o with e transformando em lista de tuplas')
with open('alunos_idade.csv', 'r', encoding='UTF-8') as arqAlunos:
    csvTabAluno = csv.reader(arqAlunos, delimiter = ';')
    tuplaAlunos = list(map(tuple, csvTabAluno))
    print(tuplaAlunos)
    print('Imprimindo a 1a linha - header', tuplaAlunos[0])
    print('Imprimindo a 1a linha - dados', tuplaAlunos[1])
    print(f'Imprimindo a uma coluna especifica {tuplaAlunos[2][1]}')

#o nosso objetivo agora é ler no seguinte formato
#{'nome':'Patricia', 'sobrenome': 'Angelini', 'idade': 50}
#{'nome':'Ricardo', 'sobrenome': 'Jesus', 'idade': 25}
print('Abrindo arquivo com o with e transformando em DICIONARIOS')
with open('alunos_idade.csv', 'r', encoding='UTF-8') as arqAlunos:
    csvTabAluno = csv.DictReader(arqAlunos, delimiter = ';')
    listDictAlunos = list(csvTabAluno)
    print(listDictAlunos)
    print(f'Imprimindo a 1a linha - dados: {listDictAlunos[0]}')
    print(f'Imprimindo a uma coluna especifica: {listDictAlunos[1]["sobrenome"]}')
    #quando nao sabemos o que é o header do meu arquivo, podemos usar a funcao fielnames
    print(f'O nosso header / chaves: {csvTabAluno.fieldnames}')

#Escrevendo um arquivo CSV
#Os dois jeitos mais usados sao: a partir de uma lista escrever num arquivo,
# ou a partir de um dicionario escrever no arquivo
print('Escrevendo um arquivo CSV a partir de uma lista')
with open('alunos_idade.csv', 'a+', encoding='UTF-8') as arqAlunos:
    csvTabAluno = csv.writer(arqAlunos, delimiter = ';')
    lAluno = ['Gustavo', 'Semenuk', 23]
    csvTabAluno.writerow(lAluno)


print('Escrevendo um arquivo CSV a partir de um dicionario')
chaves = ['nome', 'sobrenome', 'idade']
with open('alunos_idade.csv', 'a+', encoding='UTF-8') as arqAlunos:
    csvTabAluno = csv.DictWriter(arqAlunos, delimiter = ';', fieldnames=chaves)
    lAluno = {'nome':'Arthur', 'sobrenome':'Chagas', 'idade': 23}
    csvTabAluno.writerow(lAluno)

#Leia o arquivo disponibilizado em aula e
# imprima os primeiros 10 carateres

arqEx = open('Fiap_aula_arquivos.txt', 'r', encoding='UTF-8')
texto10 = arqEx.read(10)
print(texto10)
arqEx.close()

arqEx = open('Fiap_aula_arquivos.txt', 'r', encoding='UTF-8')
texto = arqEx.read()
print(texto[0:10])
print(texto[10])
arqEx.close()


arqEx = open('Fiap_aula_arquivos.txt', 'r', encoding='UTF-8')
linhas = arqEx.readlines()
cont = 0
for linha in linhas:
    #para nao pular uma linha na hora imprimir
    #eu escolho tirar da funcao print o pular linha automatico
    #assim eu informo que o meu final de linha é uma string vazia
    #end = ''
    #lembrando que o python apresenta em linhas separadas porque
    #ele esta lendo do arquivo o \n
    print(linha, end='')
    cont += 1
print(f'Total linhas {cont}')
arqEx.close()
if arqEx.closed:
    print('Arquivo fechado')

#Leia um arquivo e imprima suas linhas uma a uma. (não use lista)
print('Leia um arquivo e imprima suas linhas uma a uma. (não use lista)')
arqEx = open('Fiap_aula_arquivos.txt', 'r', encoding='UTF-8')
texto = arqEx.readlines()
for linha in texto:
    print(linha)

#voltando para o inicio do arquivo
arqEx.seek(0)
for linha in texto:
    print(linha)
arqEx.close()
