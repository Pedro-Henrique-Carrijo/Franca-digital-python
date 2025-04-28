def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = sum(1 for letra in texto if letra in vogais)
    return contador

print(contar_vogais("Pedro"))
