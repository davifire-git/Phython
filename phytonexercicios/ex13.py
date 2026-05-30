print("Escolha as Opções")
print("1 - CATETO e HIPOTENUSA")
print("2 - CATETO e CATETO")

opcao = int(input())

print("Digite agora os valores respectivamente")
val1 = float(input())
val2 = float(input())

match opcao:
    case 1:
        calc = (val1 ** 2 - val2 ** 2) ** (1/2)
        print(f"O valor do outro CATETO é {calc:.2f} ")
    case 2:
        calc = (val1 ** 2 + val2 ** 2) ** (1/2)
        print(f"O valor da HIPOTENUSA é {calc:.2f} ")