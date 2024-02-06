print("Abastecimento Caixa DAgua")
bloco = int(input("Qual bloco voce mora? (1-4) "))
if (bloco == 1) or (bloco == 3): #blocos impares
    print("O abastecimento é feito pela caixa dagua B")
else:
    print("O abastecimento é feito pela caixa dagua A")