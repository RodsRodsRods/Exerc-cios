"""
Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
"""
# | significa ou
# . significa qualquer caractere (com exceção de quebra de linha)
# [ ] significa conjunto de caracteres [a-z] faz um range de a a z

# Quantificadores:
# * 0 ou ilimitadas vezes
# + 1 ou ilimitadas vezes
# ? 0 ou 1
# {n}
# {min, max}
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'João|Maria|ad.ltos', texto))
print(re.findall(r'[Jj]oão|[Mm]aria|adultos', texto))
print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão', texto))
print(re.findall(r'jOãO|MaRiA',texto, flags= re.IGNORECASE))  #esse caso se ignora diferença entre maiscula e minuscula