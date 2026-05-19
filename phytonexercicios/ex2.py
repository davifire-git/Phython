nota1 = float(input("Digite a sua Nota: "))
nota2 = float(input("Digite a sua Nota: "))

calculo = (nota1 + nota2) / 2

if calculo >= 7:
    print(f"A sua nota foi de : {calculo} (APROVADO)")
else:
    print(f"A sua nota foi de : {calculo} (REPROVADO)") 