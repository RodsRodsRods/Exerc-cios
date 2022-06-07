"""
Operadores relacionais
== > >= < <= !=
and, or, not
in e not in
"""
username = input("Digite o nome de usuário: ")
password = int(input("Digite a senha: "))
right_password = 123456
right_username = "Rodolpho"

if username == right_username and password == right_password:
    print("Você conseguiu acessar ao sistema.")
elif password != right_password and username == right_username:
    print("Sua senha é invalida")
elif username != right_username and password == right_password:
    print("Seu usuário é invalido")
else:
    print("Tudo está errado")
