import oracledb

try:
    #Estabelecendo conexao com o banco Oracle
    conn = oracledb.connect(user="seu user", password="sua pass", dsn="oracle.fiap.com.br:1521/orcl")
except Exception as e:
    print("Erro", e)
    conexao = False
else:
    conexao = True


continua = True
if conexao:
    while continua:
        print("""Escolha uma das opcoes
        1-Consulta da Tabela
        2-Insercao de Dados
        3-Sair""")
        escolha = int(input("Escolha um numero:"))
        if escolha == 1:
            print("Consultando dados da tabela")
            #Abrindo o cursor q nada mais é do que um "ponteiro"
            c_consulta = conn.cursor()
            #O cursor faz uma requisicao para o banco e o banco executa
            c_consulta.execute("select * from t_py_aluno")
            #Se for uma instrucao que recupere dados, o fetch faz esse papel
            ldados = []
            ldados = list(c_consulta.fetchall())
            print(ldados)
            #Fechando o cursor
            c_consulta.close()
        elif escolha == 2:
            print("Inserindo dados na tabela")
            #Abrindo o cursor q nada mais é do que um "ponteiro" com a instrucao with
            #com o with nao precisa fechar o cursor
            with conn.cursor() as c_insert:
                nome = input('Digite o nome:')
                idade = int(input('Digite a idade:'))
                endereco = input('Digite o endereco:')
                curso = input('Digite o curso:')
                #Montando a string do comando
                cmd = f"insert into t_py_aluno (nome, idade, endereco, curso)" \
                      f" values " \
                      f" ('{nome}', {idade}, '{endereco}', '{curso}')"
                print(cmd)
                #O cursor faz uma requisicao para o banco e o banco executa
                c_insert.execute(cmd)
                #Nao esquecer o commit
                conn.commit()
        elif escolha == 3:
            continua = False
    #Fechando a conexao com o banco
    conn.close()






import oracledb
import csv

try:
    #Estabelecendo conexao com o banco Oracle
    conn = oracledb.connect(user="seu user", password="sua pass", dsn="oracle.fiap.com.br:1521/orcl")
except Exception as e:
    print("Erro", e)
    conexao = False
else:
    conexao = True

with conn.cursor() as c_insert:
    with open('alunos.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter =';')
        #print(list(csv_reader))
        for linha in csv_reader:
            print(linha)
            cmd = f"insert into t_py_aluno (nome, idade, endereco, curso)" \
                  f" values " \
                  f"(:nome, :idade, :endereco, :curso)"
            c_insert.execute(cmd,linha)
            conn.commit()
conn.close()
