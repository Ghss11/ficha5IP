variacoes = {
    "a": "aáàâãäAÁÀÂÃÄ", 
    "e": "eéèêëEÉÈÊË", 
    "i": "iíìîïIÍÌÎÏ", 
    "o": "oóòôõöOÓÒÔÕÖ", 
    "u": "uúùûüUÚÙÛÜ"
}

frase_original = input()
letra_consulta = input()
letras = list(frase_original)

letras_unicas = []
contagens = {}
livro = {}

#  Censo
for caractere in letras:
    if caractere.isalpha():
        letra_normal = caractere.lower()
        
        achou_vogal = False
        for chave in variacoes:
            if not achou_vogal:
                conjunto_letras = variacoes[chave]
                if caractere in conjunto_letras:
                    letra_normal = chave
                    achou_vogal = True  

        if letra_normal not in contagens:
            contagens[letra_normal] = 0
            letras_unicas.append(letra_normal)
        
        contagens[letra_normal] += 1

        # livro dos disfarces
        if letra_normal not in livro:
            livro[letra_normal] = {}
        if caractere not in livro[letra_normal]:
            livro[letra_normal][caractere] = 0
        livro[letra_normal][caractere] += 1


lista_ordenar = []
for letra in letras_unicas:
    lista_ordenar.append([letra, contagens[letra]])

tamanho = len(lista_ordenar)

for i in range(tamanho):
    for j in range(0, tamanho - i - 1):
        if lista_ordenar[j][1] < lista_ordenar[j+1][1]:
            temporario = lista_ordenar[j]
            lista_ordenar[j] = lista_ordenar[j+1]
            lista_ordenar[j+1] = temporario

resultado = ""
primeiro = True

for item in lista_ordenar:
    if not primeiro:
        resultado += " "
    resultado += f"{item[1]}{item[0]}"
    primeiro = False

print(resultado)

# Interrogatorio
disfarces = livro[letra_consulta]

total = contagens[letra_consulta]
qtd_variacoes = len(disfarces)

favorito = ""
maior = 0
for d in disfarces:
    if disfarces[d] > maior:
        maior = disfarces[d]
        favorito = d

print(f"Total de ocorrências: {total}")
print(f"Quantidade de variações: {qtd_variacoes}")
print(f"Variação mais frequente: {favorito} ({maior})")