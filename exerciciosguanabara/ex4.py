import random

alu1 = str(input('Primeiro Aluno: '))
alu2 = str(input('Segundo Aluno: '))
alu3 = str(input("Terceiro Aluno: "))

lista = [alu1,alu2,alu3]
escolhido = random.choice(lista)
print(f"O aluno escolhido foi o {escolhido}")
