"""
Formatando valores com modificadores
:s - Texto (String)
:d - Inteiros (int)
:f - Números de ponto flutuantes (float)
:.(NÚMERO DE CASAS DECIMAIS)f - Qtde de casas decimais em float
:(CARACTERE)(> ou < ou ^)(Quantidade)(Tipo - s,d ou f)
> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 105
print(f"{num_1:0>10.2f}")
nome = "Rodolpho"
sobrenome = "Franzão"
nome_formatado = "{n:@^50} {y:#^50}".format(n=nome, y=nome)  #aqui se criou uma variável com alteração com format
nome_formatado2 = "{0:%^50} {1:*^50}".format(nome, sobrenome)
print(nome_formatado)
print(nome_formatado2)
print(nome.ljust(20, '#'))   #aplicação de função de strings nativas
print(nome.lower())  #tudo minusculo
print(nome.upper())  #tudo maiusculo
print(nome.title())  #primeiras letras maiusculas