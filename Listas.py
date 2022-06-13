"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

empty_list = []
# ÍNDICES 0    1    2    3    4   POSITIVOS
lista = ["A", "Bacana", "C", "D", "E"]
# ÍNDICES-1    -2   -3   -4   -5   NEGATIVOS
string = "ABCDE"

lista.append("b")  #insere valor no final da lista
lista.insert(0, "Coco")  #insere o valor em qlq local da lista e passa os outros pra frente
print(lista)
lista.pop()  #deleta o ultimo item da lista
print(lista)
del(lista[0])
print(lista)
print(max(lista))
print(min(lista))

lista2 = list(range(0,100))
print(lista2)

for n, num in enumerate(lista2):
    print(f"Na contagem {n} da lista2 o elemento é {num}")

secret_pass = "rodolpho"
digitadas = [" "]*len(secret_pass)
count = 0;
while True:
    letra = input("Digite uma letra qualquer: ")
    if len(letra) > 1:
        print(f"Ei, {letra} não é uma letra!")
        continue
    if letra in secret_pass and letra not in digitadas:
        print(f"{letra} é uma letra!")
        for n,word in enumerate(secret_pass):
            if letra == word:
                digitadas.insert(n, word)
                del(digitadas[n+1])
                count += 1
            #print(digitadas)
    print(f"Agora faltam {len(secret_pass) - count}")
    if count == len(secret_pass):
        print(f"Você acertou todas as letras de {secret_pass}")
        break
