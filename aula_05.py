print("Clima - estrutura simples com AND")
nuvem = input("Tem nuvem no ceu hoje? ").lower()
frio = input("Esta frio hoje? ").lower()

if nuvem == 'sim' and frio == 'sim':
    print("Hoje chove")
else:
    print("Hoje não chove")


print("Clima estruruta encadeada")
nuvem = input("Tem nuvem no ceu hoje? ").lower().strip()

if nuvem in ('sim', 's', 'yes', 'y'):
    frio = input("Esta frio hoje? ").lower().strip()
    if frio in ('sim', 's', 'yes', 'y'):
        umido = input("Esta umido hoje? ").lower().strip()
        if umido in ('sim', 's', 'yes', 'y'):
            print("Hoje chove")
        else:
            print("Hoje nao chove")
    else:
        print("Hoje não chove")
else:
    print("Hoje não chove")


print("Dia da semana Encadeado")
mes = int(input("Qual é o numero do mes da semana? "))

# NAO EH RECOMENDAVEL FAZER DESSA MANEIRA POIS NAO EH EFICIENTE
# ELE VAI SEMPRE COMPARAR
# if mes == 1:
#     print("Domingo")
# if mes == 2:
#     print("Segunda")

if mes == 1:
    print("Domingo")
else:
    if mes == 2:
        print("Segunda")
    else:
        if mes == 3:
            print("Terca")
        else:
            if mes == 4:
                print("Quarta")
            else:
                if mes == 5:
                    print("Quinta")
                else:
                    if mes == 6:
                        print("Sexta")
                    else:
                        if mes == 7:
                            print("Sabado")
                        else:
                            print("Numero invalido")

print("Dia da semana Selecao")
dia = int(input("Qual é o numero do mes da semana? "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terca")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sabado")
else:
    print("Numero invalido")



print("Dia do Mes Selecao")
mes = int(input("Qual é o numero do mes? "))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Marco")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Numero invalido")


print("Notas")
nota = float(input("Entre com a sua media anual:"))
if nota>=0 and nota <= 10:
    if nota >= 6:
        print("Aprovado")
    elif nota >= 4:
        print("Exame")
    else:
        print("Reprovado")
else:
    print("Nota Invalida")


print("Triangulo")
l1 = float(input("Qual a medida do lado 1? "))
l2 = float(input("Qual a medida do lado 2? "))
l3 = float(input("Qual a medida do lado 3? "))

if l1 >= 0 and l2 >= 0 and l3 >= 0:
    if l1 == l2 == l3:
        print("Equilatero")
    elif l1 != l2 != l3 and l1 != l3 != l2:
        print("Escaleno")
    else:
        print("Isoceles")
else:
    print("Triangulo Invalido")


#Fabio

lados = ('A', 'B', 'C')
triangulos = ['Equilatero', 'Isósceles', 'Escaleno']
tamanhos = []
for lado in lados:
    tamanhos.append(int(input("Informe o lado " + lado)))
total = len(sorted(set(tamanhos))) - 1
print(triangulos[total])

#Adriano

print(" anos ")
ano = int(input(" Digite um ano entre 1000 e 2999: "))
if ano < 1000 or ano > 2999:
    print("Erro: ano fora da faixa permitida ")
else:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} não é bissexto")

#Lucas
print("Digite 4 Numeros")
n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))
n3 = int(input("Digite o terceiro número "))
n4 = int(input("Digite o quarto número "))
num = [n1, n2, n3, n4]
print(sorted(num))


### Gustavo
#
print("*********************")
print("*********ANO*********")
print("*********************")
n1=float(input("Digite um numero: "))
n2=float(input("Digite um numero: "))
n3=float(input("Digite um numero: "))
n4=float(input("Digite um numero: "))
list = [n1,n2,n3,n4]

print(f"Essa é o valor digitado:{list}")
print(f"Esse é o valor digitado em ordem crescente.",sorted(list))

#Victor
print('Ordem Crescente')
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
if num1 <= num2 and num1 <= num3 and num1 <= num4:
    print(num1, end=" ")
    if num2 <= num3 and num2 <= num4 and num3 <= num4:
        print(num2, num3, num4)
    elif num2 <= num3 and num2 <= num4 and num4 <= num3:
        print(num2, num4, num3)
    elif num3 <= num2 and num3 <= num4 and num2 <= num4:
        print(num3, num2, num4)
    elif num3 <= num2 and num3 <= num4 and num4 <= num2:
        print(num3, num4, num2)
    elif num4 <= num2 and num4 <= num3 and num2 <= num3:
        print(num4, num2, num3)
    else:
        print(num4, num3, num2)
elif num2 <= num1 and num2 <= num3 and num2 <= num4:
    print(num2, end=" ")
    if num1 <= num3 and num1 <= num4 and num3 <= num4:
        print(num1, num3, num4)
    elif num1 <= num3 and num1 <= num4 and num4 <= num3:
        print(num1, num4, num3)
    elif num3 <= num1 and num3 <= num4 and num1 <= num4:
        print(num3, num1, num4)
    elif num3 <= num1 and num3 <= num4 and num4 <= num1:
        print(num3, num4, num1)
    elif num4 <= num1 and num4 <= num3 and num1 <= num3:
        print(num4, num1, num3)
    else:
        print(num4, num3, num1)
elif num3 <= num1 and num3 <= num2 and num3 <= num4:
    print(num3, end=" ")
    if num1 <= num2 and num1 <= num4 and num2 <= num4:
        print(num1, num2, num4)
    elif num1 <= num2 and num1 <= num4 and num4 <= num2:
        print(num1, num4, num2)
    elif num2 <= num1 and num2 <= num4 and num1 <= num4:
        print(num2, num1, num4)
    elif num2 <= num1 and num2 <= num4 and num4 <= num1:
        print(num2, num4, num1)
    elif num4 <= num1 and num4 <= num2 and num1 <= num2:
        print(num4, num1, num2)
    else:
        print(num4, num2, num1)
else:
    print(num4, end=" ")
    if num1 <= num2 and num1 <= num3 and num2 <= num3:
        print(num1, num2, num3)
    elif num1 <= num2 and num1 <= num3 and num3 <= num2:
        print(num1, num3, num2)
    elif num2 <= num1 and num2 <= num3 and num1 <= num3:
        print(num2, num1, num3)
    elif num2 <= num1 and num2 <= num3 and num3 <= num1:
        print(num2, num4, num1)
    elif num3 <= num1 and num3 <= num2 and num1 <= num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)



a = int(input("Entre com o primeiro numero "))
b = int(input("Entre com o segundo numero "))
c = int(input("Entre com o terceiro numero "))
d = int(input("Entre com o quarto numero "))

print(f"Numeros originais {a} {b} {c} {d}")
#algoritmo de bubble sort

if a > b:
    aux = a
    a = b
    b = aux

if a > c:
    aux = a
    a = c
    c = aux

if a > d:
    aux = a
    a = d
    d = aux

if b > c:
    aux = b
    b = c
    c = aux

if b > d:
    aux = b
    b = d
    d = aux

if c > d:
    aux = c
    c = d
    d = aux

print(f"Numeros em ordem {a} {b} {c} {d}")