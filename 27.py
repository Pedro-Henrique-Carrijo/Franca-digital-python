def a(lista_palavras):
    return [palavra for palavra in lista_palavras if palavra.lower().startswith('a')]

print(a(["amaral", "bortoleto", "galvão", "amstel", "mclaren"]))
