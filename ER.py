import re

string = 'Este é um teste de expressões teste regulares'
print(re.search(r'teste', string))  #o 'r' permite que usemos somente uma barra '\' para escapar uma ER
                                    #ele encontra apenas a primeira ocorrência
print(re.findall(r'teste', string))  #encontra todas as ocorrências de teste na string
print(re.sub(r'teste', 'ABCD', string, count=0)) #count = 1 troca somente a primeira ocorrencia

regexp = re.compile(r'teste')  #dessa forma se compila apenas uma vez a expressão regular 'teste'
                               #regexp se torna um objeto de expressão regular
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('ABCD', string))