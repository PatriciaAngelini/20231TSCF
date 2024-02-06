print("Sindico")
bloco = int(input("Qual bloco vc mora? "))
if bloco <= 10:
    print("O sindico é o Sr José")
else:
    print("O sindico é o Sr Hamilton")

print("Sindico")
bloco = int(input("Qual bloco vc mora? "))
if bloco >= 1 and bloco <= 10:
    print("O sindico é o Sr José")

if bloco >= 11 and bloco <= 20:
    print("O sindico é o Sr Hamilton")


print("Compras")
valor_mercadoria = float(input("Quanto custa o que vc quer comprar? "))
carteira = float(input("Quanto vc tem na carteira? "))
if valor_mercadoria >= 0 and carteira >= 0:
    if (carteira >= valor_mercadoria):
        print("Posso Comprar")
    else:
        print("Preciso economizar")
else:
    print("Valor invalido")