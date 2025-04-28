def nomemaiscinco(lista_nomes):
    return [nome for nome in lista_nomes if len(nome) > 5]

print(nomemaiscinco(["Pedro", "Felipe", "Eduardo", "José"]))
