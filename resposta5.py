# define a string a ser invertida
string = "Exemplo de string a ser invertida"

# converte a string em uma lista de caracteres
lista_caracteres = list(string)

# inverte a ordem dos caracteres na lista
for i in range(len(lista_caracteres)//2):
    lista_caracteres[i], lista_caracteres[-i-1] = lista_caracteres[-i-1], lista_caracteres[i]

# converte a lista de caracteres de volta para uma string
string_invertida = "".join(lista_caracteres)

# imprime a string invertida
print(string_invertida)
