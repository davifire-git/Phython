salario = float(input("Digite o seu Sálario: "))
imp = float(input("Digite o valor do Impréstimo: "))

if salario * 0.3 > imp:
    print("APROVADO")
else:
    print("NEGADO")