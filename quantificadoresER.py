# Quantificadores: Se aplicam a coisas a esquerda ele
# * 0 ou ilimitadas vezes
# + 1 ou ilimitadas vezes
# ? 0 ou 1 - Informa se a letra anterior a isso pode ou não existir
# {n}
# {min, max} - Significa min vezes até max vezes
        #r'jo{1,}ão{1,}' == re.findall(r'jo+ão+',
#  ()+ aplicando em grupos e
#  [a-zA-z0-9]+ aplicando em limites
#  [a-zA-z0-9] sem o "+" procura apenas uma letra presente no range
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm, vem"!
'''

print(re.findall(r'jo+ão+', texto, flags=re.I))  # + aplica-se entre duas coisas
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))  # + aplica-se entre duas coisas
print(re.findall(r've{3}m{1,3}', texto, flags=re.I))  # + aplica-se entre duas coisas
print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.I))

texto2 = "João ama ser amado para amar"
print(re.findall(r'ama[do]{2}', texto2, flags=re.I))  #o {2} faz o [do] procurar duas vezes
print(re.findall(r'ama[od]{0,2}', texto2, flags=re.I))  #o * procura sem o ama e com o [do]

