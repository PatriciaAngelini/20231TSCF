# Media das notas
nota1 = float(input("Informe sua primeira nota "))
nota2 = float(input("Informe sua segunta nota "))
media =(nota1 + nota2) / 2
print(type(media))
print("A média das notas é", media)

#Taximetro
#Lucas
preco_km = 4.23
print(type(preco_km))
km_rodado = float(input("Quantos quilometros você rodou? "))
total = preco_km * km_rodado
print("O custo total foi " + str(round(total, 2)))
print(f"O custo total foi {total}")

#Direito a voto
idade = int(input("Qual sua idade? "))
print("A idade é " + str(idade))
if idade >= 16:
    print("Você tem direito a voto")
else:
    print("Você não tem direito a voto")

#Viajar
dinheiro = bool(input("Informe se vc tem dinheiro (1 - sim, nao- deixe em branco)"))
feriado = bool(input("Informe se é feriado (1 - sim, nao- deixe em branco)"))
# print("dinheiro", dinheiro)
# print("feriado", feriado)

if dinheiro and feriado:
    print("Vou viajar")
else:
    print("Pena, nao vou viajar")