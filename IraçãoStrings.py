phrase = "O rato roeu a roupa do rei de roma"
size_phrase = len(phrase)
new_string = ""
new_string2 = ""
x = 0
upper_letter = input("Qual letra deseja colocar maiúscula?")

while x < size_phrase:
    if phrase[x] == upper_letter:
        new_string += phrase[x].upper()
        new_string2 += phrase[-size_phrase + x].upper()
    else:
        new_string += phrase[x]
        new_string2 += phrase[-size_phrase+x]
    x += 1
else:
    print(new_string)
    print(new_string2)