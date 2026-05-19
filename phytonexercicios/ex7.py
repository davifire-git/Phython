cargo = str(input("Digite o seu Cargo: ").lower())
dia = int(input("Dia da Semana: "))

match cargo:
    case "admin":
        print("Acesso Liberado")
    case "suporte":
        if dia <= 6 and dia > 1:
            print("Acesso Liberado")
        else:
            print("Acesso Negado")
    case "estagiario":
        if dia <= 4 and dia > 1:
            print("Acesso Liberado")
        else:
            print("Acesso Negado")
