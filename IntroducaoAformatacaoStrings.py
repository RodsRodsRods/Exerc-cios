#Utilização de Fstrings

nome = "Rodolpho"  # "=" é um operador de atribuição
idade = 32
altura = 1.70
e_maior = idade > 18
peso = 80
imc = peso/(altura**2)
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("É maior?", e_maior)
print("IMC = ", imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # :.2f significa duas casas dec
print("{} tem {} anos de idade e seu imc é {:.2f}".format(nome, idade, imc))
print("{a} tem {b} anos de idade e seu imc é {c:.2f}".format(a = nome, b = idade, c = imc))
