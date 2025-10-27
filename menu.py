usuarios = {}
saldos = {}


def Cadastro():
    print("CADASTRO")
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if nome in usuarios:
        print("Usuário já cadastrado. Escolha outro nome.")
        return
    usuarios[nome] = senha
    saldos[nome] = {"corrente": 0.0, "poupanca": 0.0}
    print(f"Usuário '{nome}' cadastrado com sucesso!")

def acoes(nome):
    while True:
        print("AÇÕES")
        print("1 - Depósito em conta corrente \n2 - Saque conta corrente \n3 - Ver saldo em conta corrente"
              " \n4 - Depósito em conta poupança \n5 - Saque conta poupança \n6 - Ver saldo em conta poupança \n7 - Sair")
        opcao = input("Escolha uma opção: ")

    if nome in usuarios and usuarios[nome] == senha:
        print(f"Login bem-sucedido! Bem-vindo, {nome}!")
        acoes(nome)
    elif nome in usuarios:
        print("Senha incorreta. Tente novamente.")
    else:
        print("Usuário não encontrado. Faça o cadastro primeiro.")

def Acoes():
        #Depósito
        if opcao == "1":
            valor = float(input("Valor do depósito:"))
            saldos[nome]["corrente"] += valor
            print(f"Deposito de {valor} realizado com sucesso.")

        #Saque
        if opcao == "2":
            valor = float(input("Valor do saque:"))
            if valor <= saldos[nome]["corrente"]:
                saldos[nome]["corrente"] -= valor
                print(f"Saque de {valor} realizado com sucesso!")
            else:
                print("Saldo insuficiente.")

        #Ver saldo
        if opcao == "3":
            print(f"Saldo em conta corrente: {saldos[nome]['corrente']}")

#---------------------------------------------------------------------------
        #Depósito (poupança)
        if opcao == "4":
            valor = float(input("Valor do depósito: "))
            saldos[nome]["poupanca"] += valor
            print(f"Depósito de {valor} realizado com sucesso.")

        #Saque (poupança)
        if opcao == "5":
            valor = float(input("Valor do saque:"))
            if valor <= saldos[nome]["poupanca"]:
                saldos[nome]["poupanca"] -= valor
                print(f"Saque de {valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")

        #Ver saldo (poupança)
        if opcao == "6":
            print(f"Saldo em conta poupança: {saldos[nome]['poupanca']}")

        #Encerrar
        if opcao == "7":
            print("Saindo do menu de ações.")
            break  # volta ao menu principal
        else:
            print("Opção invalida. Tente novamente.")

while True:
    print("MENU PRINCIPAL")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        Cadastro()
    elif escolha == "2":
        Login()
    elif escolha == "3":
        print("Encerrando o sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")