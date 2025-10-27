from acoes import acoes

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

def Login():
    print("LOGIN")
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if nome in usuarios and usuarios[nome] == senha:
        print(f"Login bem-sucedido! Bem-vindo, {nome}!")
        acoes(nome)
    elif nome in usuarios:
        print("Senha incorreta. Tente novamente.")
    else:
        print("Usuário não encontrado. Faça o cadastro primeiro.")

def Acoes():

while True:
    print("MENU PRINCIPAL")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastro()
    elif escolha == "2":
        login()
    elif escolha == "3":
        print("Encerrando o sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")