def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

valores = input("Digite os números inteiros separados por espaço: ")
lista = [int(x) for x in valores.split()]
resultado = filtrar_pares(lista)
print("Números pares da lista:", resultado)
