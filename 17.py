def maior_menor(lista):
    if not lista:
        return "Lista vazia!"
    return max(lista), min(lista)

valores = input("Digite os números separados por espaço: ")
lista = [float(x) for x in valores.split()]
maior, menor = maior_menor(lista)
print(f"Maior número: {maior} | Menor número: {menor}")
