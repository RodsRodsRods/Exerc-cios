# Expressão regular meio ambígua = Porque se pode terminar a expressão regular em diversos pontos
#  Comportamento GREEDY (guloso): Comportamento que continua procurando na string
#? em .*? indica para o código se comportar de maneira não gulosa (LAZY = preguiçoso)
import re

texto = ''' <p>Frase 1</p> <p>Eita </p> <p>Qualquer frase</p> <div></div> '''

print(re.findall(r'<[pdiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))  #.* significa qualquer coisa com exceção de quebra de linha
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))  #.+ significa qualquer coisa com exceção de quebra de linha
#Esse algoritmo mostra a diferença entre o .+? (de 1 a n LAZY) e .*? (de 0 a n LAZY)