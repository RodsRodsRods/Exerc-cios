"""
Exercício sobre formatação de strings
"""
nome = "Rodolpho"
idade = 25
altura = 1.70
peso = 80
ano_atual = 2022
ano_nascimento = 2022 - 25
imc = peso/(altura**2)
print(f'{nome} tem {idade} anos, {peso} quilos, altura de {altura:.2f}m e seu IMC é de {imc:.2f}')
print(f'Rodolpho nasceu em {ano_nascimento}')