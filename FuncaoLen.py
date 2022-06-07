usuario = input("Qual o nome de usuario?")
qtd_caracteres = len(usuario)
#__len__ só funciona com string

print(usuario, qtd_caracteres, type(qtd_caracteres))  #retorna uma qtde_caracteres em inteiros
print(usuario.__len__()) #usuario chama o método .__len__ dentro da string