valor = str(input("Digite o valor do produto: "))

valor = valor.replace("R$" , "")
valor = valor.replace("," , ".")

valor = float(valor)

desconto = valor * 0.10
novo_valor = valor - desconto

print(f"Novo valor: {novo_valor}")