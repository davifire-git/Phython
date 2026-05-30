# Tela de Login
gmails = []
senhas = []

while True:
    print(" -- Login Site -- ")
    print("1 - Registrar-se")
    print("2 - Login")
    print("3 - Sair")

    opcao = int(input("Escolha umas das opções: "))

    match opcao:
        case 1: 
            gmail = input("Digite o seu Gmail: ")
            senha = input("Digite sua Senha: ")

            if not gmail.endswith("@gmail.com"):
                print("Digite um Gmail válido!")
                continue

            if gmail in gmails:
                print("Este Gmail já está cadastrado! 😔")
            else:
                gmails.append(gmail)
                senhas.append(senha)
                print("Gmail cadastrado com sucesso! 😁")

        case 2:
            gmail = input("Digite seu Gmail: ")
            senha = input("Digite sua Senha: ")

            if gmail in gmails and senha in senhas:
                print("Login Realizado!")
            else:
                print("Gmail errado ou Senha errado!")

        case 3:
            print("Fim da Ação")
            break
        case _:
            print("Opção inválida.")

