# Quando usamos um conjunto de caracteres [abca-zA-Z0-9] podemos achar qlq um dentro desse range
# (abc) significa que é um grupo de abc, ou seja, só encontra abc
# um grupo (qualquer coisa) define um grupo determinado que fica dentro, ou seja, 1
# () é um grupo \1
# () () são dois grupos \1 \2  (1 2 e 3 são retrovisores pra acessar o que foi salvo
# (())() são dois grupos \1 \2 \3
# ?: indica que ele quer criar um grupo porém não quer que ele seja salvo
import re
from pprint import pprint
texto = ''' <p>Frase 1</p> <p>Eita </p> <p>Qualquer frase</p> <div></div> '''

#print(re.findall(r'<([pdiv]{1,3})>.*?<\/\1>', texto))
tags = re.findall(r'(<([pdiv]{1,3})>(.*?)<\/\2>)', texto)  #esse grupo tem 3 grupos
#pprint(tags)
for tag in tags:
    um, dois, tres = tag
    print(um, dois, tres)

cpf = '147.852.369-54'
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

#print(re.findall(r'<([pdiv]{1,3})>.*?<\/\1>', texto))
tags = re.findall(r'<(?P<au>[pdiv]{1,3})>(.*?)<\/(?P=au)>', texto)  #esse é um exemplo de grupo nomeado
                                                                      #grupo nomeado (?P<nomequalquer>...)
frase_normal = re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'Cagado\1\3\4Cagado', texto)
print(frase_normal)

