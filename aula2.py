'''#print(123456)
print('Rodolpho','Franzão') #a virgula cria espaçamento para o argumento extra no print
print('Rodolpho', 'da', 'Silva', 'Franzão', sep='-') # o 'sep' cria um espaçamento com - ao invés de espaço
print('rodolpho', 'franzao', end='*') #o 'end' define o que aparece ao fim do print
'''

'''
#Exercício com CPF = 049.475.939-97
print('049', '475', '939', sep='.', end='-')
print('97')
'''
print("Essa é uma 'string' (str).")  #o comando só acaba quando tem outra "
print('Essa é uma "string" (str).')  #o comando só acaba quando tem outra '
print("Esse é meu \"texto\" (str).")  #o \" forma um caractere de escapa localizado a frente (NÃO USADO MUITO)
print('Esse é meu \'texto\' (str).')  #o \' forma um caractere de escapa localizado a frente (NÃO USADO MUITO)
print(r'Esse é meu \n (str).')  #o \n trabalha com quebra de linha (o "r" informa que nada dentro deve ser exe)