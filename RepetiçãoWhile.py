"""
while/else em Python - Aula 7
Utilizado para realizar ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores
"""

x = 0
acumulador = 1
while x<=5:
    print(x, acumulador)
    x += 1
    if x > 3:
        break
else:       #com o break em cima, ele não passa no else/ porém sem o break, ao fim do while, ele passa no else
    print("Cheguei no else")
print("Executou sem o else")  #porque tem o break em cima

x = 0
acumulador = 1
while x<=5:
    print(x, acumulador)
    x += 1
    if x > 3:
        print("estou no if")
else:       #com o break em cima, ele não passa no else/ porém sem o break, ao fim do while, ele passa no else
    print("Cheguei no else")

