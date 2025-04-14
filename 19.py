def nome_existe(lista, nome):
    return nome in lista

nomes = input("Digite os nomes separados por espaço: ").split()
nome_busca = input("Digite o nome a buscar: ")

resultado = nome_existe(nomes, nome_busca)
print("O nome existe na lista?", resultado)
