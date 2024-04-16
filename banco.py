print("===================BEM VINDO AO BANCO PY===================")

clientes = {}  
clientes_autenticados = {}  

numero_conta = 0

def formatar_data(data):

    data = data.replace(" ", "").replace("/", "").replace("-", "")

    if len(data) == 8 and data.isdigit():
        dia = data[:2]
        mes = data[2:4]
        ano = data[4:]
        return f"{dia}/{mes}/{ano}"
    else:
        print("\n !! Formato de data inválido. Por favor, digite no formato DD/MM/AAAA. !!\n")
        return None

def criar_conta():
    global numero_conta
    
    cpf = input("Digite seu CPF: ")
    if cpf in clientes:
        print(" \n !! CPF já cadastrado. !! \n")
        return
    nome = input("Digite seu nome: ").capitalize()  
    logradouro = input("Digite seu logradouro: ")
    data_nascimento = input("Digite sua data de nascimento (DDMMYYYY): ")

    data_nascimento_formatada = formatar_data(data_nascimento)
    if not data_nascimento_formatada:
        return
    
    numero_conta += 1
    num_conta_str = str(numero_conta).zfill(4)  
    clientes[cpf] = {
        "nome": nome,
        "logradouro": logradouro,
        "data_nascimento": data_nascimento_formatada,
        "saldo": 0,
        "limite": 500,
        "limite_de_saque": 3,
        "saque": 0,
        "extrato": "",
        "agencia": "1447", 
        "conta": num_conta_str,  
    }
    print("\n =========Conta criada com sucesso.======\n")

def autenticar():
    while True:
        cpf = input("Digite seu CPF: ")
        if not cpf.isdigit():
            print("\n !! CPF inválido. Por favor, digite apenas números. !!\n")
            continue
        if cpf in clientes_autenticados:
            return clientes_autenticados[cpf]
        elif cpf in clientes:
            clientes_autenticados[cpf] = clientes[cpf]
            return clientes[cpf]
        else:
            print("\n !! CPF não cadastrado. !! \n")
            opcao = input("""
                          [C]riar conta
                          [Q]uit
                          Escolha uma opção: """)
            if opcao.upper() == "C":
                criar_conta()
            elif opcao.upper() == "Q":
                return None
            else:
                print("Opção inválida, escolha novamente!")

def exibir_dados_conta(cliente):
    print("\n=== DADOS DA CONTA ===\n")
    print(f"Nome: {cliente['nome']}")
    print(f"Data Nascimento: {cliente['data_nascimento']}")
    print(f"Logradouro: {cliente['logradouro']}")
    print(f"Saldo: {cliente['saldo']}")
    print("\n=======================\n")
    print(f"Agência: {cliente['agencia']}")
    print(f"Conta: {cliente['conta']}")
    print(f"Titular: {cliente['nome']}")
    print("\n=======================\n")


def Sacar(cliente):
    valor = float(input("Digite o valor que deseja sacar: "))
    if valor > cliente["limite"]:
        print("\n !! Falha: O valor de saque excede o limite !! \n")
    elif valor > cliente["saldo"]:
        print("Falha: O valor excede o saldo atual!")
    elif cliente["saque"] > cliente["limite_de_saque"]:
        print("\n !!Falha: Número máximo de saques atingido !! \n ")
    elif valor > 0:
        cliente["saque"] += 1
        cliente["saldo"] -= valor
        cliente["extrato"] += f"Saque: R$ {valor:.2f}\n"
        print("\n=========Saque realizado com sucesso.=========\n")
    else:
        print("\n !! Valor inválido. !! \n")

def Depositar(cliente):
    valor = float(input("Digite o valor que deseja depositar: "))
    if valor > 0:
        cliente["saldo"] += valor
        cliente["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido.")

def Extrato(cliente):
    print("\n================ EXTRATO ================")
    if not cliente["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        print(cliente["extrato"])
        print(f"\nSaldo: R$ {cliente['saldo']:.2f}")
    print("==========================================")

def trocar_usuario():
    global cliente_autenticado
    cliente_autenticado = None

cliente_autenticado = None  

while True:
    if not cliente_autenticado:  
        cliente_autenticado = autenticar()
        if not cliente_autenticado:  
            opcao = input("""
                          [C]riar conta
                          [Q]uit
                          Escolha uma opção: """)
            if opcao.upper() == "C":
                criar_conta()
            elif opcao.upper() == "Q":
                break
            else:
                print("Opção inválida, escolha novamente!")
        continue

    opcao = input("""
                  [I]nformações da conta
                  [S]aque
                  [D]epósito
                  [E]xtrato
                  [T]rocar usuário
                  [Q]uit
                  Escolha uma opção: """)
    opcao = opcao.upper()
    if opcao == "I":
        exibir_dados_conta(cliente_autenticado)
    elif opcao == "S":
        Sacar(cliente_autenticado)
    elif opcao == "D":
        Depositar(cliente_autenticado)
    elif opcao == "E":
        Extrato(cliente_autenticado)
    elif opcao == "T":
        trocar_usuario()
    elif opcao == "Q":
        break
    else:
        print(" \n !! Opção inválida, escolha novamente !! \n")