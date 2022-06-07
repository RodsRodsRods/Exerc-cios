"""
Expressão Regular (re) em linguagem de programação é usada para descrever um padrão de pesquisa
Usado para se extrair informação de um texto/arquivo/
"""
import re
def is_float(val):
    if isinstance(val, float): return isinstance(val,float)
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val):
        return True
    else: return False
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-?[0-9]+$', val): return True
    else: return False
def is_number(val):
    if is_float(val) or is_int(val): return True
    else: return False

numero = input("Digite um número: ")
nome = input("Digite seu primeiro nome = ")
if len(nome) >= 5 and len(nome) <=6:
    print(f"{nome} é um nome curto")
elif len(nome) > 6:
    print(f"{nome} é um nome muito grande brow")
else:
    print(f"{nome} é um nome muito curto")

if is_number(numero):
    print("É um número!")
    if is_float(numero):
        print(f"{numero} é um numero de ponto flutuante")
    elif is_int:
        print(f"{numero} é um número inteiro!")
        if int(numero)%2 != 0:
            print(f"{numero} é um numero impar")
        else:
            print(f"{numero} é um numero par")
else:
    print("Não é um número!")



