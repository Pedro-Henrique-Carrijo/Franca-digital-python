def media_lista(lista):
    if len(lista) == 0:
        return "Lista vazia!"
    return sum(lista) / len(lista)

valores = input("Digite os números separados por espaço: ")
lista = [float(x) for x in valores.split()]
resultado = media_lista(lista)
print("Média dos números:", resultado)
