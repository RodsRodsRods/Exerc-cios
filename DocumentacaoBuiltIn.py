#O python é uma linguagem de tipagem dinâmica, ou seja, você deve sempre se converter o tipo de dado
num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

#isnumeric isdigit isdecimal
print(num1.isnumeric()) #retorna TRUE se for numero positivo
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print("ERROR")

try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
except:
    print("ERROR")