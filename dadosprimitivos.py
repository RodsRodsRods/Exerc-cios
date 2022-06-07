"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False 10 == 10
"""
print("Rodolpho", type('Rodolpho'))  #o type() evidencia o tipo de variavel que chama a função
print("10", type(10))
print("25.23", type(25.23))
print("10 = 10", "10" == "10", type(10 == 10))
print("L = l", "L" == "l", type("L" == "l"))

#maneiras de se converter um tipo variável para outro
print("Rodolpho", type('Rodolpho'), bool('Rodolpho'))
print("10", type("10"), type(int("10")))
#não tem como converter string em inteiro ou float em int
print("10.0", type(int(10.5)))

#EXERCÍCIO
#String: nome
print("Rodolpho", type("Rodolpho"))
#Idade: int
print("25", type(25))
#Altura: float
print("1.70", type(1.70))
#É maior de idade?
print("É maior de idade?", bool(25>18), type(25>18))
