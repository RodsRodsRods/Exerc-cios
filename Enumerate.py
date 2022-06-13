"""
Split, Join, ENumerate em Python
* Split - Dividir uma str
* Join - Juntar uma lista # str
* Enumerate - enumerar elementos da lista # iteráveis
"""

string = "O brasil é o pais do futebol, o Brasil é penta."

lista_1 = string.split(" ")   # split() cria uma lista através da separação feita em ()
lista_2 = string.split(",")
string2 = ",".join(lista_2)  #concatena os elementos da lista_2 com vírgulas em uma str
print(lista_1)
print(lista_2)

contagem = 0
for n, valor in enumerate(lista_1):
    print(valor)
    print(n+1)
for valor in lista_1:
    print(f"A palavra {valor} apareceu {lista_1.count(valor)}x na frase")  # conta nº vezes que valor aparece em lista_1
    qtd_vezes = lista_1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f"A palavra que apareceu mais é {palavra} ({contagem}x)")