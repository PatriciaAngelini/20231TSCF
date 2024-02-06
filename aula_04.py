print("Trato")
dever = input("Você fez o dever de casa? ").upper()
banho = input("Você lavou o Sniff? ").upper()
if (dever == 'S' or dever == 'N') and (banho == 'S' or banho == 'N'):
    if dever == 'S' and banho == 'S':
        print("Vamos na Damp")
    else:
        print("Nao vamos tomar sorvete")
else:
    print("Resposta Invalida")



print("Trato")
dever = input("Você fez o dever de casa? ").upper()
if dever == 'S' or dever == 'N':
    if dever == 'S':
        banho = input("Você lavou o Sniff? ").upper()
        if banho == 'S' or banho == 'N':
            if banho == 'S':
                print("Vamos na Damp")
            else:
                print("Nao vamos tomar sorvete")
        else:
            print("Resposta Invalida")
    else:
        print("Nao vamos tomar sorvete")
else:
    print("Resposta Invalida")