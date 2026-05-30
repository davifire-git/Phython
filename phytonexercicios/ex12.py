valor = int(input("Digite um valor inteiro: ")) # 10

contador = 0

while contador < 6:
    if valor % 2 != 0:
        print(valor)
        # contador = contador + 1
        contador += 1

    valor += 1