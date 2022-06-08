"""
Manipulando Strings - Aula 6
* String índices
* Fatiamento de strings [início:fim:passo]
* Funções built-in len, abs, type, ´print, etc...
Essas funções podem ser usadas diretamente em cada tipo
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""
#índices positivos [012345678]
texto = "Python s2"
#índices negativos [987654321]
print(texto[-9])
url = "www.google.com.br/"
print(url[-18:-1])  #você define o inicio e fim da string que deseja
print(texto[0:6])  #exemplo igual ao de cima usando indice positivo
nova_string = url[0::4]  #ele vai até o final da string pulando de 4 em 4
nova_string2 = url[0:9:4]  #ele vai até o final da string pulando de 4 em 4, porém só vai até o caracter 9
nova_string3 = url[:]  #ele vai até o final da string por padrão
print(nova_string)
print(nova_string2)
print(nova_string3)

