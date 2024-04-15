print("-=-=-=-=-=-BEM VINDO AO BANCO PY-=-=-=-=-=-")
nome = input("\nPor favor, digite seu nome: ")
print(f"Seja bem vindo, {nome}!")

saldo = 0
limite = 500
LIMITE_DE_SAQUE = 3
saque = 0
extrato = ""


def Sacar():
    global saldo, extrato, saque

    valor = float(input("Digite o valor que deseja sacar: "))
    
    if valor > limite:
        print("Falha: O valor de saque excede o limite!")
    elif valor > saldo:
        print("Falha: O valor excede o saldo atual!")
    elif saque > LIMITE_DE_SAQUE:
        print("Falha: Número máximo de saques atingido!")
    elif valor > 0:
        saque += 1
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
    else:
        print("Valor inválido.")


def Depositar():
    global saldo, extrato
    
    valor = float(input("Digite o valor que deseja depositar: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor inválido.")


def Extrato():
    global saldo
    
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


while True:
    opcao = input("""
                  [S]aque
                  [D]epósito
                  [E]xtrato
                  [Q]uit
                  """)
    if opcao.upper() == "S":
        Sacar()
    elif opcao.upper() == "D":
        Depositar()
    elif opcao.upper() == "E":
        Extrato()
    elif opcao.upper() == "Q":
        break
    else:
        print("Opcao inválida, escolha novamente!")