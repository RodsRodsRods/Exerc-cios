"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)   >Usado para cirar um range de números
# Pode-se ter contador ou não
# sem contador (exemplo: for letra in texto)
# com contador (exemplo: for n,letra in enumerate(texto))
"""

texto = "Python"
c = 0
for letra in texto:
    print(letra)

for n,letra in enumerate(texto):
    print(n, letra)

for n in range(20, 10, -1):  #padrão decrescente
    print(n)