
def menu():
    menu = """\n
    ---------- Sistema bancário ----------

    Digite a operação que deseja realizar:
    [1] - Depósito
    [2] - Saque
    [3] - Visualizar extrato
    [4] - Nova conta
    [5] - Listar contas
    [6] - Novo usuário
    [7] - Sair
    => """
    return input(menu)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo = saldo + valor 
        extrato += f"Depósito: R$ {valor:.2f}\n" #registra o deposito que foi feito na variavel extrato_deposito
        print(f"Depósito: R${valor:.2f}")

    else:
        print("Operação falhou: o valor informado é inválido.")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo: #verifica se existe saldo suficiente para ser sacado
        print(f"Operação negada, saldo insuficiente.\nSaldo atual: R${saldo}")
           
    elif excedeu_limite:
        print("Operação negada, o limite para saque é de R$500.00")

    elif excedeu_saques:
        print("Operação negada, número máximo de saques excedido.")

    elif valor > 0:
        saldo = saldo - valor
        extrato += f"Saque: R$ {valor:.2f}\n" #registra o saque que foi feito na variável extrato_saque
        numero_saques += 1 #conta quntos saques foram feitos
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

    else: 
        print("Operação falhou, o valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n-------------- EXTRATO ---------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("----------------------------------------")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print((linha))


def gerenciador(): #usado para chamar as outras funções
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0 #essa variável servirá para exibir o histórico dos extratos
    usuarios = []
    contas = []   

      
    while True:
        opcao = int(menu()) 
        if opcao == 1: #deposito:
            valor = float(input("Digite o valor que deseja depositar: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif opcao == 2: #saque
            valor = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato = saque(
            saldo = saldo,
            valor = valor, 
            extrato = extrato, 
            limite = limite, 
            numero_saques = numero_saques, 
            limite_saques = LIMITE_SAQUES
        ) 
        elif opcao == 3: #visualizar extrato
            exibir_extrato(saldo, extrato=extrato) 

        elif opcao == 4: #nova conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5: #listar contas
            listar_contas(contas)

        elif opcao == 6: #novo usuário
            criar_usuario(usuarios)

        
        elif opcao == 7: #sair
            print("Obrigado por usar nosso sistema bancário!")
            break

        else: #opc invalida
            print("Opção inválida, tente novamente!")

gerenciador()
            
    
    
