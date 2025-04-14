def somar_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        return "As listas tem que ter o mesmo tamanho."
    return [lista1[i] + lista2[i] for i in range(len(lista1))]

l1 = input("Digite os números da primeira lista separados por espaço: ")
l2 = input("Digite os números da segunda lista separados por espaço: ")

lista1 = [float(x) for x in l1.split()]
lista2 = [float(x) for x in l2.split()]

resultado = somar_listas(lista1, lista2)
print("Soma das listas:", resultado)
