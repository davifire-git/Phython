val = int(input("Coloque um valor"))
val1 = int(input("Coloque um valor"))

print("1 - Multiplicação")
print("2 - Divisão")
calculo = int(input())

match calculo:
    case 1:
        if val == 0 or val1 == 0:
            print("O seu valor é igual a 0")
        else: 
            print(f"O seu valor é igual a {val * val1}")
    case 2:
        if val == 0:
            print("O seu valor é igual a 0")
        elif val1 == 0:
            print("Não foi possivel dividir por 0")
        else:
            print(f"O seu valor é igual a {val / val1}")