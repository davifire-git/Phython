# Marcar uma data
#Preciso colocar as datas já preenchidas e quais estão vazias para serem preenchidas.
agenda = {}

while True:
    print("\n=== BARBEARIA ===")
    print("1 - Agendar horário")
    print("2 - Ver horários de um dia")
    print("3 - Ver todos os agendamentos")
    print("4 - Cancelar agendamento")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        dia = input("Dia (dd/mm): ")
        hora = input("Horário (hh:mm): ")

        if dia not in agenda:
            agenda[dia] = {}

        if hora in agenda[dia]:
            print("❌ Horário já ocupado.")
        else:
            agenda[dia][hora] = nome
            print("✅ Agendamento realizado!")

    elif opcao == "2":
        dia = input("Dia (dd/mm): ")

        horarios_padrao = [
            "09:00", "10:00", "11:00",
            "13:00", "14:00", "15:00",
            "16:00", "17:00"
        ]

        print(f"\nHorários de {dia}")

        for hora in horarios_padrao:
            if dia in agenda and hora in agenda[dia]:
                print(f"{hora} - OCUPADO")
            else:
                print(f"{hora} - LIVRE")

    elif opcao == "3":
        if not agenda:
            print("Nenhum agendamento encontrado.")
        else:
            print("\n=== AGENDAMENTOS ===")

            for dia in agenda:
                print(f"\nDia: {dia}")

                for hora, nome in agenda[dia].items():
                    print(f"{hora} - {nome}")

    elif opcao == "4":
        dia = input("Dia do agendamento: ")
        hora = input("Horário: ")

        if dia in agenda and hora in agenda[dia]:
            del agenda[dia][hora]
            print("✅ Agendamento cancelado.")
        else:
            print("❌ Agendamento não encontrado.")

    elif opcao == "5":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")
